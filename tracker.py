import ast
import subprocess
import sys


def find_changed_lines(file_path):
    
    cmd = ["git", "diff", "--unified=0", "HEAD~1", "HEAD", "--", file_path]
    diff_output = subprocess.check_output(cmd, text=True)
    changed_lines = set()

    for line in diff_output.splitlines():
        if line.startswith("@@"):
            parts = line.split(" ")
            new_file_range = parts[2]
            start_line = int(new_file_range.split(",")[0][1:])
            line_count = int(new_file_range.split(",")[1]) if "," in new_file_range else 1

            for i in range(start_line, start_line + line_count):
                changed_lines.add(i)

    return changed_lines


def map_lines_to_func(file_path):

    with open(file_path, "r") as f:
        tree = ast.parse(f.read(), filename=file_path)

    funct = {}

    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            funct[node.lineno] = node.name

    return funct


def get_func_name_for_line(line_num, func_lines):
    candidates = [ln for ln in func_lines if ln <= line_num]
    if not candidates:
        return None
    
    return func_lines[max(candidates)]


def get_author_of_line(file_path, line_num):

    cmd = ["git", "blame", "-L", f"{line_num},{line_num}", "--line-porcelain", file_path]
    output = subprocess.check_output(cmd, text=True)

    for line in output.splitlines():
        if line.startswith("author "):
            return line[len("author "):]
        
    return "Unknown"


def main(file_path):

    changed_lines = find_changed_lines(file_path)
    function_lines = map_lines_to_func(file_path)
    line_to_func = {line: get_func_name_for_line(line, function_lines) for line in changed_lines}

    reported = set()

    for line, func in line_to_func.items():
        if func and func not in reported:
            author = get_author_of_line(file_path, line)
            print(f"Function '{func}' was added/removed/modified by {author}")
            reported.add(func)


if __name__ == "__main__":
    file_path = sys.argv[1]
    main(file_path)
