import csv


def func_to_read() :
    #with syntax to automatically close
    with open('aapl.csv',mode='r') as csv_file:

        #object of reader
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        print(f"This is the output of csv_reader = {csv_reader}")

        next(csv_reader)  # used over an iterable
        for row in csv_reader:
            print(row)
            # if line_count == 0:
            #     print(f'Column names are {", ".join(row)}')
            #     line_count += 1
            # else:
            #     print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
            #     line_count += 1
        # print(f'Processed {line_count} lines.')


def func_to_read_as_dict() :
    #with syntax to automatically close
    with open('aapl.csv',mode='r') as csv_file:
        csv_reader_as_dict = csv.DictReader(csv_file)
        print(csv_reader_as_dict)
        line_count = 0
        for row in csv_reader_as_dict:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            print(f'\t{row["name"]} works in the {row["department"]} department, and was born in {row["birthday month"]}.')
            line_count += 1
        print(f'Processed {line_count} lines.')



func_to_read_as_dict()