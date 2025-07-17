.PHONY: build build-audiobook build-all publish upload clean

# Build the article in PDF LaTeX
build:
	@dir_name=$$(basename $$(pwd)); \
	target_file="$$dir_name.md"; \
	if [ -f "$$target_file" ]; then \
		echo "Building $$target_file with metadata"; \
		mdtexpdf convert "$$target_file" --read-metadata; \
	else \
		echo "No target file $$target_file found in $$(pwd)"; \
	fi

# Publish the article
publish:
	@dir_name=$$(basename $$(pwd)); \
	target_file="$$dir_name.md"; \
	if [ -f "$$target_file" ]; then \
		echo "Publishing $$target_file"; \
		bash ../lib/publish_article.sh .; \
	else \
		echo "No target file $$target_file found in $$(pwd)"; \
	fi

# Build the audiobook (new)
build-audiobook:
	@dir_name=$$(basename $$(pwd)); \
	target_file="$$dir_name.md"; \
	if [ -f "$$target_file" ]; then \
		echo "Building audiobook: $$target_file"; \
		mdaudiobook "$$target_file"; \
	else \
		echo "No target file $$target_file found in $$(pwd)"; \
	fi

# Build both PDF and audiobook (new)
build-all: build build-audiobook
	@echo "Built both PDF and audiobook for $(basename $(pwd))"

# Complete workflow for single article: build + publish (publish handles PDF transfer)
upload: build publish
	@echo "Single article upload complete: $(basename $(pwd))"

# Clean generated files (new)
clean:
	@dir_name=$$(basename $$(pwd)); \
	rm -f "$$dir_name.pdf" "$$dir_name.m4b"
	@echo "Cleaned generated files for $(basename $(pwd))"
