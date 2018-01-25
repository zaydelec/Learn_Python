import imp
try:
    imp.find_module('distribute')
    found = True
except ImportError:
    found = False
    
    
print found


