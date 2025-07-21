name = "my_tool"
version = "1.0.0"
requires = ["python-3.11", "maya-2024"]

build_command = 'python {root}/build.py {install}'

def commands():
    env.PYTHONPATH.append("{root}/python")
