#tuple are immutable

from xmlrpc.server import list_public_methods


list = (1,2,3,4,5,6)
print(dir(list_public_methods))