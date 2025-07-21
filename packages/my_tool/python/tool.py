import os

def getMayaInfo():
    maya_version = os.environ.get("MAYA_VERSION")
    print(f"MAYA_VERSION: {maya_version}")