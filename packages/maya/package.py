name = "maya"
version = "2024"

build_command = "echo skipping build"

def commands():
    env.MAYA_VERSION.set("2024")
    env.REZ_MAYA_ROOT.set("{root}")
