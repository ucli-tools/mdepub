import argparse
import os
import sys
import pypandoc
import yaml
import frontmatter
from datetime import datetime
from importlib import metadata

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
    
    # --- Math Processing ---
    # Use MathML for better EPUB compatibility
    math_method = config.get('math_method', 'mathml')
    if math_method == 'mathml':
        extra_args.append('--mathml')
    elif math_method == 'webtex':
        extra_args.append('--webtex')
    elif math_method == 'katex':
        extra_args.append('--katex')
    elif math_method == 'mathjax':
        extra_args.append('--mathjax')
    else:
        # Default to MathML for EPUB
        extra_args.append('--mathml')
    
    # --- Processing Options ---
    if config.get('table_of_contents'):
        extra_args.append('--toc')
        extra_args.append(f"--toc-depth={config.get('toc_depth', 3)}")

    # --- EPUB Options ---
    if config.get('chapter_level'):
        # Use --split-level instead of deprecated --epub-chapter-level
        extra_args.append(f"--split-level={config['chapter_level']}")
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
    known_args = ['table_of_contents', 'toc_depth', 'chapter_level', 'stylesheet', 'lua_filter', 'output_directory', 'output_filename_template', 'math_method']
    for key, value in config.items():
        if key not in known_args and value is not None:
            extra_args.append(f'--metadata={key}:{value}')
    
    return extra_args

def get_output_path(config, input_path, output_dir=None):
    """Determine the output path based on the configuration."""
    # Use provided output_dir, then config, then current working directory
    if output_dir:
        output_dir = output_dir
    elif config.get('output_directory'):
        output_dir = config.get('output_directory')
    else:
        output_dir = os.getcwd()
    
    os.makedirs(output_dir, exist_ok=True)

    # Sanitize title and author for the filename
    sanitized_config = {k: str(v).replace('/', '-') for k, v in config.items()}

    filename_template = config.get('output_filename_template', '{title} - {author}')
    filename = filename_template.format(**sanitized_config) + '.epub'

    return os.path.join(output_dir, filename)

def get_version():
    """Get the version of the package."""
    try:
        return metadata.version('mdepub')
    except metadata.PackageNotFoundError:
        return "0.0.0 (local development)"

def main():
    # Handle --version flag manually to avoid argparse exit issues
    if '--version' in sys.argv:
        print(f"mdepub {get_version()}")
        return

    parser = argparse.ArgumentParser(
        description="A powerful, configuration-driven tool to convert Markdown documents into beautifully styled EPUB files.",
        formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument(
        "input_file",
        help="The path to the input Markdown file."
    )
    parser.add_argument(
        "--output-dir",
        help="Directory where the EPUB file will be saved (defaults to current directory)"
    )
    
    # Check if input_file was provided
    if len(sys.argv) < 2 or sys.argv[1].startswith('-'):
        parser.print_help()
        return

    args = parser.parse_args()

    project_root = get_project_root()
    config, content = load_configuration(args.input_file, project_root)
    
    output_path = get_output_path(config, args.input_file, args.output_dir)
    extra_args = build_pandoc_args(config, project_root)

    print(f"Converting {args.input_file} to {output_path}...")
    try:
        pypandoc.convert_text(
            content,
            'epub',
            format='md',
            outputfile=output_path,
            extra_args=extra_args
        )
        print(f"✓ Successfully created {os.path.basename(output_path)}.")
    except Exception as e:
        print(f"An error occurred during conversion: {e}")

if __name__ == "__main__":
    main()
