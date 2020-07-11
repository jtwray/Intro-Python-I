# # Write a function is_even that will return true if the passed-in number is even.

# # YOUR CODE HERE
# def is_even(num):
#     if (num == int(num) and (num%2)==0): 
#         return True 
#     return False
#     # Read a number from the keyboard


#    if num in (num%2)==0:
#         return "EVEN!"
#     if num in (num%2) !=0:
#          return "Odd"

# # # Print out "Even!" if the number is even. Otherwise print "Odd"
# def printEven():
#     global num
#     if num%2==0
#         return print("Even!")

# printEven(3)
# # YOUR CODE HERE
# is_even(num)


def is_even():
    num = input("Enter a number: ")
    num = int(num)
    if (num%2)==0:
        print("Even!")
        return print(True)
    print("Odd")

is_even()