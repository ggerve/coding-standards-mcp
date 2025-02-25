# Java Style Guide

## Naming
- Classes: PascalCase (`UserService`)
- Methods/Variables: camelCase (`getUserById`)
- Constants: UPPER_SNAKE_CASE (`MAX_RETRY_COUNT`)
- Packages: lowercase (`com.company.project`)

## Code Layout
- Use 4 spaces for indentation
- Line length: 120 characters max
- One statement per line
- Use blank lines to separate logical blocks
- Keep methods short (< 30 lines)

## Classes
- One top-level class per file
- Order: static fields → instance fields → constructors → methods
- Use appropriate access modifiers
- Avoid public fields

## Methods
- Clear and descriptive names
- Single responsibility
- Document public APIs
- Return early to avoid nesting

## Variables
- One variable per line
- Initialize at declaration when possible
- Use final for constants
- Meaningful names

## Comments
- Use Javadoc for public APIs
- Keep comments meaningful
- Explain "why" not "what"
- Use TODO for temporary code

## Exception Handling
- Use specific exceptions
- Don't ignore exceptions
- Use try-with-resources
- Log exceptions properly

## Collections
- Use interface types (List over ArrayList)
- Use diamond operator
- Use enhanced for loop when possible
- Consider collection capacity

## Testing
- Test class name: [Class]Test
- Test method: [method]_[scenario]_[expectedResult]
- One assertion per test
- Use meaningful test data
