
import math # Importing math library 
import math as m # Import with alias
from math import pi, sqrt # Import specific items from a module
from math import * # Import all items from a module
import importlib # Import module members dynamically
math_module = importlib.import_module('math')

def hello_world():
    print(sqrt(20))

hello_world()

import os