# 一块代码学python
# 异常处理

# <<定义异常>>
def p1():
    raise Exception("aaa", "bbb")


def p2():
    raise Exception()


def p3():
    raise IOError()


def p4():
    pass


err = {
    1: p1,
    2: p2,
    3: p3,
    4: p4
}

# <<处理异常>>
for m in err.values():  # 依次尝试...
    try:
        print("test func:{0}".format(m.__name__))
        m()
    except Exception as e:
        print("error, e={0}".format(e))
    except IOError:
        print(IOError)
    else:
        print("okay")
    finally:
        print("finnaly")
        print("\n")

# <<可以参考的>>
# doc: https://docs.python.org/3/tutorial/errors.html
# built in exceptions: https://docs.python.org/3.7/library/exceptions.html
