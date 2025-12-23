# mdepub

**A powerful, configuration-driven tool to convert Markdown documents into beautifully styled EPUB files.**

`mdepub` is a command-line tool designed to streamline the creation of professional-quality EPUBs from Markdown. It leverages the power of Pandoc and is designed for maximum customization through simple YAML configuration, CSS, and Lua filters.

---

## ✨ Features

- **System-Wide Installation:** Install `mdepub` once and run it from any directory.
- **Pandoc-Powered Conversion:** Reliably converts Markdown to high-quality EPUB.
- **Advanced Styling:** Comes with a default stylesheet for a clean, modern look.
- **Custom Page Structure:** Uses a Lua filter to automatically create specially formatted "Part" pages from level-1 headers.
- **YAML Configuration:** Easily customize the output with a central `config/default.yaml` and per-project `metadata.yaml` files.
- **Makefile-Driven Workflow:** Simple `make` commands handle setup, building, and system-wide installation.

## 🚀 Getting Started

### Prerequisites

- Python 3.6+
- Pandoc

### Installation

1.  **Clone the Repository**

    ```bash
    git clone https://github.com/ucli-tools/mdepub
    cd mdepub
    ```

2.  **Set Up the Environment**

    This command creates a virtual environment and installs all dependencies.

    ```bash
    make setup
    ```

3.  **Build the Wrapper Script**

    This creates the `mdepub` executable script with proper path handling:

    ```bash
    make build
    ```

4.  **Install System-Wide (Recommended)**

    To make the `mdepub` command available from any directory:

    ```bash
    make install-system
    ```

    This installs the wrapper to `/usr/local/bin/mdepub`. You can uninstall it anytime with:

    ```bash
    make uninstall-system
    ```

## 🔧 Usage

After installation, you can use `mdepub` from any directory:

### System-Wide Usage (Recommended)

Once installed with `make install-system`, you can run `mdepub` from anywhere:

```bash
# Navigate to your documents folder
cd /path/to/my/books

# Generate an EPUB - output will be saved in current directory
mdepub my-book.md

# Or specify a different output location
mdepub my-book.md --output-dir /path/to/output
```

### Local Usage (Development)

If you haven't installed system-wide, use the local wrapper:

```bash
# From the mdepub project directory
./mdepub /path/to/your/document.md

# The EPUB will be saved in your current working directory
```

### Alternative: Direct Python Module

```bash
# Activate the virtual environment first
source /path/to/mdepub/venv/bin/activate

# Run the module directly
python -m mdepub.cli my-book.md --output-dir .
```

### Important Notes

- **Output Location**: By default, EPUBs are saved in your current working directory
- **Shell Compatibility**: The wrapper works with both bash and fish shells
- **Path Handling**: Both relative and absolute paths are supported
- **Automatic Path Resolution**: The wrapper handles path conversion automatically

## ⚙️ Configuration

`mdepub` uses a combination of a default configuration file and per-project metadata to give you full control over the output.

### Default Configuration

The main configuration is stored in `config/default.yaml`. This file defines the default settings for all conversions.

### Document Metadata

You can override the default settings and add metadata (like title, author, etc.) by creating a `metadata.yaml` file in the same directory as your Markdown file. The tool will automatically detect and use it.

Here is an example `metadata.yaml`:

```yaml
---
title: "My Awesome Book"
author: "A. U. Thor"
---
```

## 📁 Project Structure

```
mdepub/
├── Makefile                 # Build and automation commands
├── README.md                # This documentation
├── requirements.txt         # Python dependencies
├── setup.py                 # Python package setup
├── .gitignore              # Git ignore rules (excludes user wrappers)
├── src/
│   └── mdepub/              # Main source code
│       ├── __init__.py
│       └── cli.py           # Command-line interface
├── config/
│   └── default.yaml         # Default EPUB conversion settings
├── assets/
│   └── stylesheet.css       # Default EPUB styles
├── filters/
│   └── part-filter.lua      # Lua filter for 'Part' pages
├── documents/
│   ├── analysis.md          # Example content
│   └── metadata.yaml        # Example metadata
├── tests/                   # Test suite (in development)
└── venv/                    # Virtual environment (created by make setup)
```

## 🔧 Troubleshooting

### Common Issues and Solutions

**Shell Compatibility**: The tool has been tested with both bash and fish shells. If you encounter shell-related issues, ensure your wrapper script uses bash-compatible syntax.

**Missing sys Import**: If you see import errors related to `sys`, this has been fixed in the latest version. Make sure you're using the updated `cli.py`.

**Output Directory Issues**: Always use the `--output-dir` argument to specify where you want the EPUB file saved. This prevents path-related issues and ensures consistent behavior.

**Path Handling**: The tool correctly handles both relative and absolute paths. If you encounter path issues, try using absolute paths.

### Development Notes

- User-specific wrapper scripts are automatically excluded from version control via `.gitignore`
- The tool uses proper argument parsing to handle file paths and output directories
- All fixes maintain backward compatibility while improving reliability

## 📄 License

**This project is licensed under the Apache 2.0 License** - see the [LICENSE](LICENSE) file for details.

### 🌐 Free and Open Source Software (FOSS)

This universal EPUB conversion tool is part of the Universalis ecosystem's **dual licensing model**:

- **🌐 This Tool (FOSS)**: Freely available under Apache 2.0 for anyone to use
- **🔒 Particular Implementations**: Organizations may use this tool in their own projects with any licensing

You are free to:
- ✅ Use this tool for any purpose (commercial or non-commercial)
- ✅ Modify and customize it for your needs
- ✅ Distribute your modifications
- ✅ Integrate it into proprietary workflows

*Part of the Universalis Project - Where universal tools meet particular implementations*

