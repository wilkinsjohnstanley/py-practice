def func_1():
    raise KeyError("We forced this exception for a demo.")
    return None
def func_2():
    func_1()

def func_3():
    func_2()

def 