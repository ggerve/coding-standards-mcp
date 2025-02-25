# Python Style Guide

## The Zen of Python
- Explicit is better than implicit
- Simple is better than complex
- Readability counts
- Flat is better than nested
- Sparse is better than dense

## Naming
- Modules: short, lowercase (`users.py`, `db.py`)
- Packages: short, lowercase, no underscores (`mypackage`)
- Classes: PascalCase, nouns (`UserProfile`, `DatabaseConnection`)
- Functions: snake_case, verbs (`get_user`, `connect_to_db`)
- Variables: snake_case, nouns (`user_list`, `connection_pool`)
- Constants: UPPER_SNAKE_CASE (`MAX_CONNECTIONS`, `DEFAULT_TIMEOUT`)
- Protected: single underscore (`_internal_method`)
- Private: double underscore (`__very_private`)

## Code Layout
- 4 spaces indentation (no tabs)
- 88 chars line length (black default)
- Surround top-level functions and classes with two blank lines
- Use blank lines to separate logical sections
- No trailing whitespace
- End files with a single newline

## Functions
```python
def process_data(
    data: list[str],
    *,                    # Force keyword arguments
    timeout: int = 30,
) -> dict[str, any]:
    """Process the input data.

    Args:
        data: List of strings to process
        timeout: Operation timeout in seconds

    Returns:
        Processed data as dictionary
    """
```

## Type Hints
- Use for function arguments and return values
- Use for complex variables
- Use typing module for complex types
- Optional for simple scripts
```python
from typing import Optional, Sequence

def find_user(id: int) -> Optional[User]: ...
def process_items(items: Sequence[str]) -> list[str]: ...
```

## Imports
```python
# Standard library
import os
from pathlib import Path

# Third party
import requests
from fastapi import FastAPI

# Local
from .models import User
from .utils import get_logger
```

## String Formatting
```python
# Yes
name = "World"
print(f"Hello {name}")

# No
print("Hello %s" % name)
print("Hello {}".format(name))
```

## Collections
```python
# Use list comprehension for simple transformations
squares = [x * x for x in range(10)]

# Use generator expressions for large sequences
sum(x * x for x in range(1000000))

# Use dict comprehension where appropriate
user_ids = {user.name: user.id for user in users}
```

## Context Managers
```python
# Yes
with open('file.txt') as f:
    data = f.read()

# No
f = open('file.txt')
try:
    data = f.read()
finally:
    f.close()
```

## Testing
```python
# test_users.py
def test_user_creation():
    """Test user creation with valid data."""
    user = User(name="test", email="test@example.com")
    assert user.name == "test"
    assert user.email == "test@example.com"
```

## Documentation
- Use docstrings for modules, classes, functions
- Follow Google style docstrings
- Include type hints in docstrings when not using annotations
- Document exceptions raised
- Add examples for complex functions
