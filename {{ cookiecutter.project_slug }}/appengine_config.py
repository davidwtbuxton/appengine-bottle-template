import os
import sys


project_dir = os.path.dirname(__file__)
libs_dir = os.path.join(project_dir, 'libs')


if libs_dir not in sys.path:
    sys.path.insert(1, libs_dir)
