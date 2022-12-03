"""
with syntax

automatically closing file once the usage is done

"""


def func_for_with() :

    filename = "withsyntax_example1.txt"

    with open(file=filename,mode = 'w+') as with_syntax_object :
        with_syntax_object.write("abc or file1")


func_for_with()