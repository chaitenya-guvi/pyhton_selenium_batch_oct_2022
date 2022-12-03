"""
this i s to write to a function

1. create a object to open a file in write mode - 'w'
2. perform the write actions
3. close the object

"""

def fnc_to_write() :

    filename_to_write = "write_file.txt"

    #creating the writer object
    writer_object_example1 = open(file=filename_to_write , mode= 'w')

    list_1 = ["This is line 1",
    "This is line 2",
    "This is line 3",
    "This is line 4"]

    # for line in list_1 :
    # # method to write to the object
    #     writer_object_example1.write(line)


    # method to accept list \ tuple or any iterable as arguement
    writer_object_example1.writelines(list_1)



    #close the file after writing
    writer_object_example1.close()

fnc_to_write()