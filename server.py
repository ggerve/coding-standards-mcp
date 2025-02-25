from mcp.server.fastmcp import FastMCP
import os

# Create an MCP server
mcp = FastMCP("coding_standards")

def read_template(filename: str) -> str:
    """Read content from a template file"""
    template_path = os.path.join(os.path.dirname(__file__), "templates", filename)
    try:
        with open(template_path, "r") as f:
            return f.read()
    except FileNotFoundError:
        return f"Error: Template file {filename} not found"
    except Exception as e:
        return f"Error reading template {filename}: {str(e)}"

@mcp.tool()
def java_style_guide() -> str:
    """Get Java coding style guidelines in Markdown format"""
    return read_template("java_style_guide.md")

@mcp.tool()
def python_style_guide() -> str:
    """Get Python coding style guidelines in Markdown format"""
    return read_template("python_style_guide.md")

@mcp.tool()
def java_best_practices() -> str:
    """Get Java application best practices in Markdown format"""
    return read_template("java_best_practices.md")

@mcp.tool()
def react_best_practices() -> str:
    """Get React application best practices in Markdown format"""
    return read_template("react_best_practices.md")
