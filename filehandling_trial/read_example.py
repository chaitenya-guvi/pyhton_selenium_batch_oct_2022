"""
how to read a file
create a read object
1. open a file in read mode 'r'
2. read it word by word

"""

def fnc_to_read() :
    file_to_read = "test1.txt"

    read_object = open(file = file_to_read , mode= 'r')

    print(type(read_object.readlines()))

    # # method to read file object line by line
    # print(read_object.readline())
    # print(read_object.readline())
    # print(read_object.readline())
    # print(read_object.readline())


    # method to read as lines
    # print(read_object.readlines())

    # reading line by line :
    # for line in read_object.readlines() :
    #     print(line)



    read_object.close()


fnc_to_read()