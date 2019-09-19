import sys
import os

# Adds "src" to sys.path
# "src" contains a package "example"
# Now you can do import with "from example.Sub-Package ..."
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', "src")))
