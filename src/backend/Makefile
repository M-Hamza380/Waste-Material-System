.PHONY: setup upgrade run sort format lint pre-commit pre-commit-clean pre-commit-uninstall pre-commit-install clean update

# Setup development environment
setup:
	uv sync

# Upgrade uv.lock file
upgrade:
	uv lock --upgrade

# Sort imports using isort
sort:
	isort src --verbose

# Format code using black
format:
	black src --verbose

# Lint code using flake8
lint:
	flake8 src --verbose

# Run pre-commit hooks
pre-commit:
	pre-commit run --all-files

# Clean pre-commit hooks
pre-commit-clean:
	pre-commit clean

# Uninstall pre-commit hooks
pre-commit-uninstall:
	pre-commit uninstall

# Install pre-commit hooks
pre-commit-install:
	pre-commit install

# Update pre-commit hooks
update:
	pre-commit autoupdate

# Run application
run:
	uv run python main.py

# Clean .pyc and cache files in all directories
clean:
	@echo Cleaning up Python cache files....
	@for /r "." %%d in (*__pycache__) do @if exist "%%d" rmdir /s /q "%%d"
	@for /r "." %%f in (*.pyc) do @if exist "%%f" del /q "%%f"
	@for /r "." %%f in (*.pyo, *.pyd, .pytest_cache .coverage htmlcov .tox) do @if exist "%%f" rmdir /s /q "%%f"
	@echo Cleanup complete!
