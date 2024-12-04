import os

def print_tree(root_dir, excluded_dirs):
    for root, dirs, files in os.walk(root_dir):
        dirs[:] = [d for d in dirs if d not in excluded_dirs]
        level = root.replace(root_dir, "").count(os.sep)
        indent = " " * 4 * level
        print(f"{indent}{os.path.basename(root)}/")
        sub_indent = " " * 4 * (level + 1)
        for file in files:
            print(f"{sub_indent}{file}")

project_path = r"C:\Users\Y.CHEHBOUB\Downloads\myYoutube\Project"
excluded = {"node_modules", "vendor"}
print_tree(project_path, excluded)
