print("import...")

import comp
comp.com_func_a()
comp.com_func_b()

print(comp.__name__)

del comp


print("\nfrom ...import...")
from comp import com_func_a
com_func_a()

del com_func_a

print("\nimport as...")
import comp as a
a.com_func_a()
from comp import com_func_b as b
b()
del a
del b

print("\nsearch path:")
import sys
# your sys.path include:
# 1.work folder's path
# 2.PYTHONPATH
# 3.python install path
print(sys.path)

print("\ndir() func")
import comp
print(dir(comp))
