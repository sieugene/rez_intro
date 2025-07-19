name = "my_tool"
version = "1.0.0"
requires = ["maya-2024"]

build_command = "echo skipping build"

def commands():
    env.PYTHONPATH.append("{root}/my_tool")
