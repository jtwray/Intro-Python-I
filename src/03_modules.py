"""
In this exercise, you'll be playing around with the sys module,
which allows you to access many system specific variables and
methods, and the os module, which gives you access to lower-
level operating system functionality.
"""
import sys
import os
import platform

# def printCommandLineArguments( module ):     # creates a function to print off a directory listing of all the methods for any module passed in as an argument
#     for i in dir( module ):                  # dir(module) returns a list
#         methodIndex = dir( module ).index(i) # for each index in the module's list of methods
#         print(f'dir({ module }) at index of[{methodIndex}] = {i}  ')

          
# See docs for the sys module: https://docs.python.org/3.7/library/sys.html

# Print out the command line arguments in sys.argv, one per line:
# YOUR CODE HERE
# printCommandLineArguments(sys.argv)
def printtheCLArgs():
    for (x,arg) in enumerate(sys.argv):
        print(f'CommandLine Arg #{x+1}: {arg}')

printtheCLArgs( )

# Print out the OS platform you're using:
# YOUR CODE HERE
print(f'---|| line 30  os.name={os.name}')
print(f'---|| line 31  platform.platform():{platform.platform()}')
print(f'---|| line 32  platform.system():{platform.system()}')
print(f'---|| line 33  sys.platform:{sys.platform}')


# Print out the version of Python you're using:
# YOUR CODE HERE
print(f'---|| line 38 current version : python { sys.version}')


# print(f'---|| line 2===========================0  OS={os.system()}')
os.sys
# See the docs for the OS module: https://docs.python.org/3.7/library/os.html
print(f'---|| line 44 os {os}')


# Print the current process ID
# YOUR CODE HERE
print(f'---|| line 49 current process id is : {os.getpid()}')


# Print the current working directory (cwd):run
# YOUR CODE HERE
print(f'---|| line 54 print the current working directory : {os.getcwd()}')


# Print out your machine's login name
# YOUR CODE HERE
print(f'---|| line 59 My Machine\'s Login name is : {os.getlogin()}')

