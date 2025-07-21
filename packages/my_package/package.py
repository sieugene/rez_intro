name = "my_package"

version = "1.0.0"

description = \
    """
    Python-based hello world example package.
    """

tools = [
    "hello"
]

requires = [
    "python-3.11",
    "rez"
]

uuid = "packages.my_package"

build_command = 'python {root}/build.py {install}'

def commands():
    env.PYTHONPATH.append("{root}/python")
    env.PATH.append("{root}/bin")
