# Python Coding Style Guidelines

## PEP 8 Basics
- Use 4 spaces for indentation
- Line length limit: 79 characters for code, 72 for docstrings
- Use spaces around operators and after commas
- Use two blank lines before top-level classes/functions

## Naming Conventions
- Function names: snake_case (e.g., `get_user_by_id`)
- Variable names: snake_case (e.g., `first_name`)
- Class names: PascalCase (e.g., `UserProfile`)
- Constants: UPPER_SNAKE_CASE (e.g., `MAX_ITEMS`)
- Protected attributes: _single_underscore
- Private attributes: __double_underscore

## Imports
- Imports on separate lines
- Order: standard library → third party → local
- Absolute imports preferred over relative
- No wildcard imports (from module import *)

## String Formatting
- Use f-strings for string formatting (Python 3.6+)
- Use r-strings for regular expressions
- Use """triple quotes""" for docstrings

## Best Practices
- Follow the Zen of Python (import this)
- Use type hints (Python 3.5+)
- Write descriptive docstrings
- Keep functions focused (single responsibility)
- Use context managers (with statement) when applicable
