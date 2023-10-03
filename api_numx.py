#from .numx import Numx
from numx.Numx import Numx


def prc_numx():
    numz = input("Enter a number: ")
    numx = Numx(numz)
    numx.get_fact()

if __name__ == "__main__":
    flag = True
    while flag:
        prc_numx()
        strx = input("Continue (y/n) : ")
        if strx.lower() == "n":
            flag = False