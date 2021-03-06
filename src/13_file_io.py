from nt import close

"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"

# YOUR CODE HERE

with open('./src/foo.txt','r') as f:

    print('reading foo.txt \n', f.read(),'\n')
    # for line in f:
    #     print(line, end="")


# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain
with open('./src/bar.txt','w+') as f:
    f.write('Peter Piper picked a peck of pickled peppers\n')
    f.write('A peck of pickled peppers did Peter Piper pick\n')
    f.write('If Peter Piper picked a peck of pickled peppers\n')
    f.write('How many pickled peppers did Peter Piper pick\n')
# YOUR CODE HERE

with open('./src/bar.txt') as f:
    print("reading bar.txt\n",f.read())