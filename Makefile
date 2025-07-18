.PHONY: help setup dev-setup test lint clean clean-all epub build rebuild install-system uninstall-system

# Default target for ucli compatibility
build: install-system

# Help target
help:
	@echo "mdepub - Professional Markdown to EPUB Pipeline"
	@echo ""
	@echo "Available targets:"
	@echo "  setup           - Install dependencies and setup environment"
	@echo "  dev-setup       - Setup development environment (includes test dependencies)"
	@echo ""
	@echo "Processing Commands:"
	@echo "  epub SOURCE=file.md - Process a Markdown file into an EPUB"
	@echo ""
	@echo "Development:"
	@echo "  build            - Build mdepub executable wrapper"
	@echo "  rebuild          - Clean and rebuild"
	@echo "  install-system   - Install to /usr/local/bin (system-wide)"
	@echo "  uninstall-system - Remove from system PATH"
	@echo "  test             - Run all tests"
	@echo "  lint             - Check code quality"
	@echo "  clean            - Clean generated files"
	@echo "  clean-all        - Clean everything including venv"
	@echo ""
	@echo "Example:"
	@echo "  make epub SOURCE=documents/example.md"

# Environment and setup
setup:
	@echo "Setting up mdepub environment..."
	@if [ ! -d "venv" ]; then python3 -m venv venv; echo "Created virtual environment"; fi
	@echo "Activating virtual environment and installing dependencies..."
	. venv/bin/activate && pip install -r requirements.txt && pip install -e .
	@echo "Setup complete!"
	@echo "Note: Remember to activate the virtual environment with 'source venv/bin/activate' or use the 'make build' wrapper."

dev-setup: setup
	@echo "Setting up development environment..."
	. venv/bin/activate && pip install -r requirements-dev.txt
	@echo "Development environment ready!"

# Main processing command
epub:
	@if [ -z "$(SOURCE)" ]; then echo "Usage: make epub SOURCE=file.md"; exit 1; fi
	@echo "Processing EPUB: $(SOURCE)"
	. venv/bin/activate && python -m mdepub.cli $(SOURCE)

# Testing and quality assurance
test:
	@echo "Running tests..."
	. venv/bin/activate && python -m pytest tests/ -v

lint:
	@echo "Checking code quality..."
	. venv/bin/activate && flake8 src/ tests/
	. venv/bin/activate && black --check src/ tests/
	. venv/bin/activate && isort --check-only src/ tests/

# Installation and packaging
rebuild: clean build

install-system: setup
	@echo "Installing mdepub with pipx..."
	@# Install using pipx for isolated CLI tool installation
	pipx install .
	@echo "✓ mdepub installed successfully with pipx."
	@echo "Run 'mdepub --help' to get started."

uninstall-system:
	@echo "Uninstalling mdepub with pipx..."
	pipx uninstall mdepub
	@echo "✓ mdepub uninstalled."

# Cleanup
clean:
	@echo "Cleaning generated files..."
	rm -f mdepub
	rm -rf output/
	rm -rf __pycache__/
	rm -rf src/__pycache__/
	rm -rf tests/__pycache__/
	rm -rf .pytest_cache/
	rm -rf *.egg-info/
	find . -name "*.pyc" -delete
	find . -name "*.pyo" -delete

clean-all: clean
	@echo "Cleaning everything including virtual environment..."
	rm -rf venv/
