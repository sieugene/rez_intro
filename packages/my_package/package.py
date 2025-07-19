name = "my_package"
version = "1.0.0"
requires = [
    "python-3.11",
    "setuptools",
    "rez"
]
build_command = "python {root}/setup.py install --prefix={install}"

def commands():
    env.PYTHONPATH.append("{root}/mymodule")
