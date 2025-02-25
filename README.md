# Coding Standards MCP Server

This MCP server provides tools for accessing coding style guidelines and best practices for various technologies.

## Installation

Using `uv`:
```bash
uv venv
source .venv/bin/activate
uv pip install -e .
```

## Available Tools

1. `java_style_guide()`: Get Java coding style guidelines
2. `python_style_guide()`: Get Python coding style guidelines
3. `java_best_practices()`: Get Java application best practices
4. `react_best_practices()`: Get React application best practices

## Usage

To run the server in development mode:
```bash
mcp dev server.py
```

To install the server in Claude Desktop:
```bash
mcp install server.py
```
