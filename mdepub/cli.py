import argparse
import os
import pypandoc
import yaml
import frontmatter
from datetime import datetime

def get_project_root():
    """Find the project root by looking for the setup.py file."""
    current_path = os.path.abspath(os.path.dirname(__file__))
    while current_path != os.path.dirname(current_path):
        if os.path.exists(os.path.join(current_path, 'setup.py')):
            return current_path
        current_path = os.path.dirname(current_path)
    return os.getcwd()

def merge_configs(base, override):
    """Recursively merge two dictionaries, overwriting keys in base with keys from override."""
    for key, value in override.items():
        if isinstance(value, dict) and key in base and isinstance(base[key], dict):
            base[key] = merge_configs(base[key], value)
        else:
            base[key] = value
    return base

def load_configuration(input_file_path, project_root):
    """Load and merge configurations from default, project, and frontmatter."""
    # 1. Load default config
    default_config_path = os.path.join(project_root, 'config', 'default.yaml')
    config = {}
    if os.path.exists(default_config_path):
        with open(default_config_path, 'r') as f:
            config = yaml.safe_load(f) or {}

    # 2. Load and merge project-specific metadata (if it exists)
    metadata_path = os.path.join(os.path.dirname(input_file_path) or '.', 'metadata.yaml')
    if os.path.exists(metadata_path):
        print(f"Found project metadata at: {metadata_path}")
        with open(metadata_path, 'r') as f:
            project_meta = yaml.safe_load(f) or {}
            config = merge_configs(config, project_meta)

    # 3. Load and merge frontmatter metadata (highest priority)
    post = frontmatter.load(input_file_path)
    if post.metadata:
        print("Found frontmatter metadata.")
        config = merge_configs(config, post.metadata)
    
    # Set date if not provided
    if config.get('date') is None:
        config['date'] = datetime.now().strftime('%Y-%m-%d')

    return config, post.content

def build_pandoc_args(config, project_root):
    """Build the list of extra arguments for Pandoc from the config."""
    extra_args = []
    
    # --- Processing Options ---
    if config.get('table_of_contents'):
        extra_args.append('--toc')
        extra_args.append(f"--toc-depth={config.get('toc_depth', 3)}")

    # --- EPUB Options ---
    if config.get('chapter_level'):
        extra_args.append(f"--epub-chapter-level={config['chapter_level']}")
    if config.get('stylesheet'):
        css_path = os.path.join(project_root, config['stylesheet'])
        if os.path.exists(css_path):
            extra_args.append(f'--css={css_path}')
    if config.get('lua_filter'):
        filter_path = os.path.join(project_root, config['lua_filter'])
        if os.path.exists(filter_path):
            extra_args.append(f'--lua-filter={filter_path}')

    # --- Metadata ---
    # All remaining keys in the config are treated as metadata
    known_args = ['table_of_contents', 'toc_depth', 'chapter_level', 'stylesheet', 'lua_filter', 'output_directory', 'output_filename_template']
    for key, value in config.items():
        if key not in known_args and value is not None:
            extra_args.append(f'--metadata={key}:{value}')
    
    return extra_args

def get_output_path(config, input_path):
    """Determine the output path based on the configuration."""
    output_dir = config.get('output_directory') or os.path.dirname(input_path) or '.'
    os.makedirs(output_dir, exist_ok=True)

    filename_template = config.get('output_filename_template', '{title} - {author}')
    # All config keys are available for the template
    filename = filename_template.format(**config) + '.epub'

    return os.path.join(output_dir, filename)

def main():
    parser = argparse.ArgumentParser(description="Convert a Markdown file to EPUB.")
    parser.add_argument("input_file", help="The path to the input Markdown file.")
    args = parser.parse_args()

    input_path = args.input_file
    if not os.path.exists(input_path):
        print(f"Error: Input file not found at {input_path}")
        return

    project_root = get_project_root()
    config, content = load_configuration(input_path, project_root)
    
    extra_args = build_pandoc_args(config, project_root)
    output_path = get_output_path(config, input_path)

    print(f"Converting {input_path} to {output_path}...")

    try:
        pypandoc.convert_text(
            source=content,
            to='epub',
            format='md',
            outputfile=output_path,
            extra_args=extra_args
        )
        print("Conversion successful!")
    except Exception as e:
        print(f"An error occurred during conversion: {e}")
