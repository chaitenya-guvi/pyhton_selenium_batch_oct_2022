import pytest

"""
py.test -s -v test_filename.py
py.test -s -v test_filename.py::test_methodA
-- deocrators = programiz, geeksforgeeks
"""
@pytest.fixture()
def setUP():
    print("\n This is a setup lien\n")
    yield
    print("\nThis is a teard down step \n")


def test_functionA(setUP) :
    print("This is method A")


def test_functionB(setUP) :
    print("This is method B")