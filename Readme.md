## Project Structure

```
packages/
└── my_package/
    ├── package.py      # Rez package definition
    ├── setup.py        # Optional setuptools script
    └── hello_world/    # Python module directory
        ├── __init__.py
        └── hello.py    # Example Python module
```

## What is this?

This is a simple Rez package example containing a Python module `mymodule`.
The Rez package definition (`package.py`) configures the build and environment for this module.

## How to build and use

1. **Build and install the package:**

```bash
cd packages/my_package
rez-build --install
rez-env my_package -- hello
```

2. **Activate Rez environment with your package:**

```bash
rez env my_package -- python
```

3. **Use the Python module:**

```python
from hello_world import hello

hello()
```

4. **Check package**

```bash
rez search my_package
```

5. **Run with version**

```bash
rez env my_package-1.0.0 -- python
```


6. **Check root folder**
```bash
rez env my_package-1.1.0 -- printenv REZ_MY_PACKAGE_ROOT
```

7. **Activate an environment with multiple packages**

You can activate a Rez environment with several packages at once. For example:

```bash
rez-env my_package my_tool -- python
import hello_world
hello_world.hello() # Should print Hello World from my_package!
import test
test.hello() # Should print Hello from my_tool
```

This allows you to use Python modules from both `my_package` and `my_tool` in the same session, which is useful for testing integration and compatibility between packages.

