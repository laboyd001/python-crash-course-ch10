#working with multiple files

def count_words(filename):
    """Count the approx number of words in a file."""
    try:
        with open(filename, encoding='utf-8') as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        msg = "Sorry, the file " + filename + " does not exist."
        print(msg)
        #the word 'pass' could be used here instead of the 3 lines above so the user never sees the error.
    else:
        #Count approx number of words in the file.
        words = contents.split()
        num_words = len(words)
        print("The file " + filename + " has about " + str(num_words) + " words.")

# filename = 'alice.txt'
# count_words(filename)

filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']
for filename in filenames:
    count_words(filename)