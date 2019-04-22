# just import a package
import a_package

a_package.a_comp.a_func()

del a_package

# just import from
from a_package import a_comp

a_comp.a_func()

del a_comp

# package inner import
import a_package

print(dir(a_package))
print(dir(a_package.a_comp))
print(dir(a_package.submodules))

a_package.submodules.submodules_func.submodules_func()
a_package.a_comp.b_func()

# !bad
from a_package import *
# may not init properly
