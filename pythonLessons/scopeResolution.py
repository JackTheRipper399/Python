# variable scope = where a variable is visible and accessible
# scope resolution = (LEBG) Local -> Enclosed -> Global -> Built-in

# Local
from math import e


def func1L():
    a = 1
    print(a)


def func2L():
    b = 2
    print(b)


# func1L()
# func2L()

# Enclosed


def func1E():
    y = 1

    def func2E():
        y = 2
        print(y)
    func2E()


# func1E()

# Global
x = 3


def func1G():
    print(x)


def func2G():
    print(x)


# func1G()
# func2G()

# Built-in
def func1B():
    print(e)


e = 3

func1B()
