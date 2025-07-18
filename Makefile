.PHONY: help setup dev-setup test lint clean clean-all epub build rebuild install-system uninstall-system

# Default target
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
build: install-system

rebuild: clean build

install-system: setup
	@echo "Installing mdepub to /opt/ucli-tools/mdepub..."
	@# Create installation directory
	sudo mkdir -p /opt/ucli-tools/mdepub
	@# Copy entire project to permanent location
	sudo cp -r . /opt/ucli-tools/mdepub/
	@# Set proper ownership
	sudo chown -R root:root /opt/ucli-tools/mdepub
	@# Create system wrapper script
	@echo '#!/bin/bash' | sudo tee /usr/local/bin/mdepub > /dev/null
	@echo '# mdepub - System wrapper for mdepub.py' | sudo tee -a /usr/local/bin/mdepub > /dev/null
	@echo '' | sudo tee -a /usr/local/bin/mdepub > /dev/null
	@echo '# Set mdepub directory (permanent installation)' | sudo tee -a /usr/local/bin/mdepub > /dev/null
	@echo 'MDEPUB_DIR="/opt/ucli-tools/mdepub"' | sudo tee -a /usr/local/bin/mdepub > /dev/null
	@echo '' | sudo tee -a /usr/local/bin/mdepub > /dev/null
	@echo '# Store current working directory' | sudo tee -a /usr/local/bin/mdepub > /dev/null
	@echo 'ORIGINAL_CWD="$$(pwd)"' | sudo tee -a /usr/local/bin/mdepub > /dev/null
	@echo '' | sudo tee -a /usr/local/bin/mdepub > /dev/null
	@echo '# Convert relative paths to absolute paths' | sudo tee -a /usr/local/bin/mdepub > /dev/null
	@echo 'args=()' | sudo tee -a /usr/local/bin/mdepub > /dev/null
	@echo 'for arg in "$$@"; do' | sudo tee -a /usr/local/bin/mdepub > /dev/null
	@echo '    # Check if argument looks like a file path (contains . or / and doesnt start with -)' | sudo tee -a /usr/local/bin/mdepub > /dev/null
	@echo '    if [[ "$$arg" == *.* || "$$arg" == */* ]] && [[ "$$arg" != -* ]]; then' | sudo tee -a /usr/local/bin/mdepub > /dev/null
	@echo '        # Convert to absolute path if its relative' | sudo tee -a /usr/local/bin/mdepub > /dev/null
	@echo '        if [[ "$$arg" != /* ]]; then' | sudo tee -a /usr/local/bin/mdepub > /dev/null
	@echo '            args+=("$$ORIGINAL_CWD/$$arg")' | sudo tee -a /usr/local/bin/mdepub > /dev/null
	@echo '        else' | sudo tee -a /usr/local/bin/mdepub > /dev/null
	@echo '            args+=("$$arg")' | sudo tee -a /usr/local/bin/mdepub > /dev/null
	@echo '        fi' | sudo tee -a /usr/local/bin/mdepub > /dev/null
	@echo '    else' | sudo tee -a /usr/local/bin/mdepub > /dev/null
	@echo '        args+=("$$arg")' | sudo tee -a /usr/local/bin/mdepub > /dev/null
	@echo '    fi' | sudo tee -a /usr/local/bin/mdepub > /dev/null
	@echo 'done' | sudo tee -a /usr/local/bin/mdepub > /dev/null
	@echo '' | sudo tee -a /usr/local/bin/mdepub > /dev/null
	@echo '# Activate virtual environment and execute Python script with absolute paths' | sudo tee -a /usr/local/bin/mdepub > /dev/null
	@echo 'cd "$$MDEPUB_DIR"' | sudo tee -a /usr/local/bin/mdepub > /dev/null
	@echo '. venv/bin/activate && python src/mdepub/cli.py "$${args[@]}" --output-dir "$$ORIGINAL_CWD"' | sudo tee -a /usr/local/bin/mdepub > /dev/null
	@sudo chmod +x /usr/local/bin/mdepub
	@echo "✓ mdepub installed successfully."
	@echo "Run 'mdepub --help' to get started."

uninstall-system:
	@echo "Uninstalling mdepub from /usr/local/bin..."
	sudo rm -f /usr/local/bin/mdepub
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
