# Coding Standards MCP Server

This MCP server provides tools for accessing coding style guidelines and best practices for various technologies (Java, Python, React).

## Prerequisites

- Python 3.8 or higher
- MCP package (`pip install mcp`)
- UV package manager (recommended)

## Quick Start

1. Install the server in Claude:
```bash
mcp install server.py
```

2. Run in development mode:
```bash
mcp dev server.py
```
The MCP inspector will start on port 3000.

## Available Tools

### Style Guides
Access language-specific coding style guidelines:
- Java: Clean code practices, naming conventions, code organization
- Python: PEP 8 based guidelines, Pythonic code practices
- React: Component structure, hooks usage, TypeScript integration

### Best Practices
Access language-specific application best practices:
- Java: Project structure, architecture, testing, security
- Python: Project layout, dependency management, testing practices
- React: Component patterns, state management, performance optimization

## API Reference

1. `java_style_guide`: Get Java coding style guidelines
   - Returns: Markdown formatted style guide
   - Example: `nortal_coding_standards_java_style_guide()`

2. `java_best_practices`: Get Java application best practices
   - Returns: Markdown formatted best practices
   - Example: `nortal_coding_standards_java_best_practices()`

3. `python_style_guide`: Get Python coding style guidelines
   - Returns: Markdown formatted style guide
   - Example: `nortal_coding_standards_python_style_guide()`

4. `python_best_practices`: Get Python application best practices
   - Returns: Markdown formatted best practices
   - Example: `nortal_coding_standards_python_best_practices()`

5. `react_best_practices`: Get React application best practices
   - Returns: Markdown formatted best practices
   - Example: `nortal_coding_standards_react_best_practices()`

## Configuration

### MCP Client Configuration

Add this to your MCP client configuration file (e.g., `~/.codeium/windsurf/mcp_config.json`):

```json
{
  "mcpServers": {
    "nortal_coding_standards": {
      "command": "uv",
      "args": [
        "run",
        "--with",
        "mcp[cli]",
        "mcp",
        "run",
        "/absolute/path/to/coding-standards-mcp/server.py"
      ]
    }
  }
}
```

Replace `/absolute/path/to/coding-standards-mcp/server.py` with your actual server path.