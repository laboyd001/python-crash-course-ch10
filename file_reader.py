#Reading from a text file

filename = 'pi_digits.txt'

with open(filename) as file_object:
    # for line in file_object:
    #     print(line.rstrip())

#making a list of lines from a file

    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())