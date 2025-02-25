# Python Best Practices

## Project Structure
```
project-root/
├── src/                    # Source code
│   └── mypackage/
│       ├── __init__.py    # Package initialization
│       ├── cli.py         # Command-line interface
│       ├── config.py      # Configuration handling
│       ├── constants.py   # Constants and enums
│       ├── models/        # Data models
│       │   ├── __init__.py
│       │   └── base.py
│       ├── services/      # Business logic
│       └── utils/         # Helper functions
├── tests/                 # Test suite
│   ├── __init__.py
│   ├── conftest.py       # pytest fixtures
│   ├── test_models.py
│   └── test_services.py
├── docs/                  # Documentation
├── scripts/              # Maintenance scripts
├── .env.example         # Environment template
├── .gitignore
├── README.md
├── pyproject.toml       # Project metadata (PEP 621)
└── requirements.txt     # or poetry.lock

## Python-Specific Practices
- Use virtual environments (venv, poetry)
- Follow PEP guidelines
- Use type hints for larger projects
- Leverage duck typing and EAFP
- Use iterators and generators
- Implement context managers

## Dependency Management
- Use modern tools (poetry, pip-tools)
- Lock dependencies (poetry.lock, requirements.txt)
- Specify version ranges appropriately
- Use setup.py for libraries
- Use pyproject.toml for applications

## Pythonic Code
- Use list/dict comprehensions
- Leverage generator expressions
- Use context managers (with statement)
- Follow EAFP (Easier to Ask for Forgiveness)
- Use magic methods when appropriate
- Leverage standard library

## Error Handling
```python
# Yes
try:
    value = data['key']
except KeyError:
    value = default

# No
if 'key' in data:
    value = data['key']
else:
    value = default
```

## Configuration
- Use environment variables
- Use .env files for development
- Use configuration objects
- Validate configuration at startup
- Keep secrets out of code

## Testing
- Use pytest
- Write fixtures
- Use parametrized tests
- Mock external services
- Test edge cases
```python
@pytest.mark.parametrize("input,expected", [
    (1, 1),
    (2, 4),
    (3, 9),
])
def test_square(input, expected):
    assert square(input) == expected
```

## Logging
- Use structured logging
- Configure proper log levels
- Include context in logs
- Use logging handlers
- Implement log rotation

## Performance
- Profile before optimizing
- Use appropriate data structures
- Consider asyncio for I/O
- Implement caching
- Use PyPy for CPU-bound tasks

## Documentation
- Write clear docstrings
- Generate API docs (sphinx)
- Maintain README.md
- Include examples
- Document gotchas

## Development Tools
- Use black for formatting
- Use flake8 for linting
- Use mypy for type checking
- Use pre-commit hooks
- Use tox for testing
