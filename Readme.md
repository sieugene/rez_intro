## Project Structure

```
packages/
└── *_package/
    ├── package.py
    ├── setup.py
    └── *module/
        └── __init__.py
```

## What is this?

This is a simple Rez package example containing a Python module `mymodule`.
The Rez package definition (`package.py`) configures the build and environment for this module.

## How to build and use

1. **Build and install the package:**

```bash
cd packages/my_package
rez-build -i
```

2. **Activate Rez environment with your package:**

```bash
rez env my_package -- python
```

3. **Use the Python module:**

```python
from mymodule import hello

hello()  # Should print "Hello from Rez package!"
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