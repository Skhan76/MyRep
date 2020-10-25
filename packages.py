# package is a container for multiple modules
# module should have __init__ file in it

'''
import Pkg.pn   # PKg is the pacjage name and .pn is the file in the package

Pkg.pn.print_message()
'''

# alternate approach

from Pkg.pn import print_message    # This way print_message function can be used with referening full path
                                    # we can import from Pkg import pn to import whole package 
print_message()

