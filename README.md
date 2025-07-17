# mdepub

**A powerful, configuration-driven tool to convert Markdown documents into beautifully styled EPUB files.**

`mdepub` is a command-line tool designed to streamline the creation of professional-quality EPUBs from Markdown. It leverages the power of Pandoc and is designed for maximum customization through simple YAML configuration, CSS, and Lua filters.

---

## ✨ Features

- **Pandoc-Powered Conversion:** Reliably converts Markdown to high-quality EPUB.
- **Advanced Styling:** Comes with a default stylesheet for a clean, modern look, including distinct title and part pages.
- **Custom Page Structure:** Uses a Lua filter to automatically create specially formatted "Part" pages from level-1 headers.
- **YAML Configuration:** Easily customize the output with a central `config/default.yaml` and per-project `metadata.yaml` files.
- **Makefile-Driven Workflow:** Simple `make` commands handle setup, building, and conversion.

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

    The `setup` command will create a Python virtual environment and install all necessary dependencies.

    ```bash
    make setup
    ```

3.  **Activate the Environment**

    ```bash
    source venv/bin/activate
    ```

4.  **Install for Development**

    To make the `mdepub` command available in your shell, install the package in editable mode:

    ```bash
    make install
    ```

## 🔧 Usage

Once installed, you can run `mdepub` directly on any Markdown file. The output `.epub` file will be created in the same directory.

```bash
# Generate an EPUB from a Markdown file
mdepub /path/to/your/document.md
```

You can also use the `Makefile` for convenience:

```bash
# Use the Makefile to convert a file
make epub SOURCE=documents/analysis.md
```

## ⚙️ Configuration

`mdepub` uses a combination of a default configuration file and per-project metadata to give you full control over the output.

### Default Configuration

The main configuration is stored in `config/default.yaml`. This file defines the default settings for all conversions, including:

- **Chapter Splitting:** Control how chapters are divided.
- **Stylesheet:** The default CSS file for styling.
- **Lua Filter:** The default filter for custom structures.

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
├── README.md                # This file
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
