from mcp.server.fastmcp import FastMCP
import os
from typing import Dict, List, Optional
import re

# Create an MCP server
mcp = FastMCP("coding_standards")

def get_template_info(filename: str) -> Optional[Dict[str, str]]:
    """Extract template type and language from filename"""
    pattern = r"^(\w+)_(style_guide|best_practices)\.md$"
    match = re.match(pattern, filename)
    if match:
        language, template_type = match.groups()
        return {
            "language": language,
            "type": "style_guides" if template_type == "style_guide" else "best_practices"
        }
    return None

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
def list_templates() -> Dict[str, Dict[str, List[str]]]:
    """List all available templates grouped by type and language"""

    template_dir = os.path.join(os.path.dirname(__file__), "templates")
    templates = {
        "style_guides": {"languages": [], "files": []},
        "best_practices": {"languages": [], "files": []}
    }
    
    try:
        for filename in os.listdir(template_dir):
            if filename.endswith('.md'):
                template_info = get_template_info(filename)
                if template_info:
                    template_type = template_info["type"]
                    templates[template_type]["languages"].append(template_info["language"])
                    templates[template_type]["files"].append(filename)
        
        # Sort the lists for consistent output
        for template_type in templates:
            templates[template_type]["languages"].sort()
            templates[template_type]["files"].sort()
            
        return templates
    except Exception as e:
        return {"error": f"Failed to list templates: {str(e)}"}

@mcp.tool()
def get_style_guide(language: str) -> str:
    """Get coding style guidelines for the specified language in Markdown format"""

    filename = f"{language}_style_guide.md"
    return read_template(filename)

@mcp.tool()
def get_best_practices(language: str) -> str:
    """Get application best practices for the specified language in Markdown format"""
    filename = f"{language}_best_practices.md"
    return read_template(filename)
