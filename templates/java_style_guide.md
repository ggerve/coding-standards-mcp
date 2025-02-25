# Java Coding Style Guidelines

## Naming Conventions
- Class names: PascalCase (e.g., `CustomerService`)
- Method names: camelCase (e.g., `getUserById`)
- Variables: camelCase (e.g., `firstName`)
- Constants: UPPER_SNAKE_CASE (e.g., `MAX_CONNECTIONS`)
- Packages: all lowercase (e.g., `com.company.project`)

## Code Structure
- One class per file
- Class order: static fields → instance fields → constructors → methods
- Methods should be grouped by functionality
- Keep methods focused and concise (< 30 lines recommended)

## Formatting
- Use 4 spaces for indentation (no tabs)
- Line length limit: 120 characters
- One statement per line
- Use braces with all control structures (if, for, while, etc.)

## Best Practices
- Always specify access modifiers (public, private, protected)
- Favor immutability (use final where possible)
- Document public APIs with Javadoc
- Use meaningful variable names
- Avoid magic numbers, use named constants

## Exception Handling
- Never catch Exception (too broad)
- Don't ignore exceptions (at minimum, log them)
- Use try-with-resources for AutoCloseable resources
- Document thrown exceptions in Javadoc
