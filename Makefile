.PHONY: help setup install test lint clean build

# Default target
help:
	@echo "mdepub - Markdown to EPUB Converter"
	@echo ""
	@echo "Available targets:"
	@echo "  setup    - Set up the development environment"
	@echo "  install  - Install the package in editable mode"
	@echo "  test     - Run tests (not yet implemented)"
	@echo "  lint     - Lint the code (not yet implemented)"
	@echo "  clean    - Remove temporary build files"
	@echo "  build    - Build the package"
		@echo "  epub     - Convert a Markdown file to EPUB (e.g., make epub SOURCE=documents/analysis.md)"

# Environment and setup
setup:
	@echo "Setting up virtual environment..."
	python3 -m venv venv
	@echo "Installing dependencies..."
	. venv/bin/activate && pip install -r requirements.txt
	@echo "Setup complete. Activate with: source venv/bin/activate"

install:
	pip install -e .

# Testing and quality assurance
test:
	@echo "Tests are not yet implemented."

lint:
	@echo "Linter is not yet implemented."

# Build and clean
clean:
	@echo "Cleaning up..."
	rm -rf build dist *.egg-info __pycache__ */__pycache__

build:
	python setup.py sdist bdist_wheel

# Conversion
epub:
	@if [ -z "$(SOURCE)" ]; then echo "Usage: make epub SOURCE=<path_to_markdown_file>"; exit 1; fi
	mdepub $(SOURCE)
