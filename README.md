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

    This creates the `mdepub` executable script that can be installed system-wide.

    ```bash
    make build
    ```

4.  **Install System-Wide (Optional)**

    To make the `mdepub` command available from any directory, install it to `/usr/local/bin`.

    ```bash
    sudo make install-system
    ```

    You can uninstall it at any time with `sudo make uninstall-system`.

## 🔧 Usage

Once installed system-wide, you can run `mdepub` directly on any Markdown file. The output `.epub` file will be created in your **current working directory**.

```bash
# Navigate to your documents folder
cd /path/to/my/books

# Generate an EPUB from a Markdown file
# The output will be saved in the current directory
mdepub my-book.md
```

If you prefer not to install it system-wide, you can run the local wrapper script from the project root:

```bash
# From the mdepub project directory
./mdepub /path/to/your/document.md
```

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
├── Makefile                 # Main automation script
├── README.md                # This file
├── requirements.txt         # Main dependencies
├── requirements-dev.txt     # Development dependencies
├── setup.py                 # Python package setup
├── src/
│   └── mdepub/              # Source code
│       ├── __init__.py
│       └── cli.py             # Command-line interface
├── config/
│   ├── default.yaml         # Default EPUB settings
│   └── part_title.lua       # Lua filter for part titles
└── documents/
    └── example.md           # Example content
```

├── Makefile                 # Build and processing commands
├── requirements.txt         # Python dependencies
├── setup.py                 # Package setup
├── config/
│   └── default.yaml       # Default conversion settings
├── assets/
│   └── stylesheet.css     # Default EPUB styles
├── filters/
│   └── part-filter.lua    # Lua filter for 'Part' pages
├── mdepub/
│   ├── __init__.py
│   └── cli.py             # Main command-line script
├── documents/
│   ├── analysis.md
│   └── metadata.yaml
└── tests/                     # (Not yet implemented)
```

## 📄 License

This project is licensed under the Apache 2.0 License. See the [LICENSE](LICENSE) file for details.
