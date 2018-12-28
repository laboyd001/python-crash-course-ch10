#writing to a file

filename = 'programming.txt'

# with open(filename, 'w') as file_object:
#     file_object.write("I love programming.\n")
#     file_object.write("I love cats.\n")


#appending to a file rather than overwriting:

with open(filename, 'a') as file_object:
    file_object.write("I love getting outside.\n")
    file_object.write("Today is my birthday!\n")


