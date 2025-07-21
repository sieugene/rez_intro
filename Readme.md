# Rez Intro Project

## Overview

This project demonstrates a basic structure for Python development using Rez packages. It includes two example packages: `my_package` and `my_tool`, as well as a sample integration script.

## Project Structure

```
packages/
├── my_package/
│   ├── package.py      # Rez package definition
│   ├── setup.py        # Optional setuptools script
│   └── hello_world/    # Python module
│       ├── __init__.py
│       └── hello.py
├── my_tool/
│   ├── package.py
│   └── test.py
├── maya/
│   ├── package.py
│   └── ...
scripts/
└── main.py             # Example script for running packages
Makefile                # Automation for build and run tasks
```

## Quick Start

### 1. Build and Install Packages

You can use the Makefile for common tasks:

- **Build all packages:**
    ```bash
    make build-all
    ```
- **Clean all build directories:**
    ```bash
    make clean
    ```
- **Run the main script with all packages:**
    ```bash
    make run
    ```

### 2. Manual Usage

- **Build and install a package:**
    ```bash
    cd packages/my_package
    rez-build --install
    ```
- **Check if the package is available:**
    ```bash
    rez search my_package
    ```
- **Activate a Rez environment with your package:**
    ```bash
    rez env my_package -- python
    ```
- **Use the Python module:**
    ```python
    from hello_world import hello
    hello()
    ```
- **Check the package root folder:**
    ```bash
    rez env my_package-1.1.0 -- printenv REZ_MY_PACKAGE_ROOT
    ```

### 3. Using Multiple Packages

You can activate an environment with several packages for integration testing:

- **Interactive Python session:**
    ```bash
    rez env my_package my_tool -- python
    ```
    ```python
    import hello_world
    hello_world.hello()  # Should print Hello World from my_package!
    import test
    test.hello()         # Should print Hello from my_tool
    ```
- **Run the main script:**
    ```bash
    rez env my_package my_tool -- python ./scripts/main.py
    ```

## Makefile Description

The Makefile automates common development tasks:

- **build-all** — Builds all packages (`maya`, `my_package`, `my_tool`)
- **clean** — Cleans all build directories
- **run** — Cleans, builds, and runs the main script with the required packages

**Usage examples:**
```bash
make build-all   # Build all packages
make clean       # Clean build directories
make run         # Full cycle: clean, build, and run
```

## Conclusion

This project is a simple template for organizing and integrating Python packages using Rez and Makefile automation. Use it as a starting point for your own dependency management and build automation workflows.