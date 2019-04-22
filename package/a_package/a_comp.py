def a_func():
    print("a_func")


def b_func():
    print("b_func with:")
    import submodules
    submodules.submodules_func.submodules_func()

