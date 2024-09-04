import ast
import json

def create_ast(code_str):
  """Parses Python code and returns the AST representation."""
  tree = ast.parse(code_str)
  return tree

def write_code_and_ast(code_str, filename):
  """Writes Python code and its AST to separate files."""
  tree = create_ast(code_str)

  # Write the original code
  with open(f"{filename}.py", "w") as f:
      f.write(code_str)

  # Convert AST to a dictionary (optional)
  ast_dict = ast.dump(tree)

  # Write the AST dictionary to a JSON file
  with open(f"{filename}.ast", "w") as f:
      json.dump(ast_dict, f, indent=4)  # For readability with indentation

# Example usage
code = """
def add(x, y):
  return x + y

print(add(5, 3))
"""

write_code_and_ast(code, "my_code")

