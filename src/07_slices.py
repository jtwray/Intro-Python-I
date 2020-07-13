"""
Python exposes a terse and intuitive syntax for performing 
slicing on lists and strings. This makes it easy to reference
only a portion of a list or string. 

This Stack Overflow answer provides a brief but thorough
overview: https://stackoverflow.com/a/509295

Use Python's slice syntax to achieve the following:
"""

a = [2, 4, 1, 7, 9, 6]

# Output the second element: 4:
secondelement=a[slice(1,2)]
print(secondelement)
# print(a[1])
# Output the second-to-last element: 9
# print(a[-1])
# secondToLast=a[slice(4,5)]
# print(secondToLast)
# secondToLast=a[4:5]
# print(secondToLast)
# secondToLast=a[slice(-2,-3,-1)] # start from the 2nd to last, stop before the 3rd to last, go backwards i.e. right to left
# print(secondToLast)
# secondToLast=a[-2:-3:-1]        # start from the 2nd to last, stop before the 3rd to last, go backwards i.e. right to left
# print(secondToLast)
# secondToLast=a[slice(4,-1)]
# print(secondToLast)
# secondToLast=a[4:-1]
# print(secondToLast)
# secondToLast=a[slice(-2,-1)]# start at the 2nd to last item: stop before the last item
# print(secondToLast)
secondToLast=a[-2:-1]       # start at the 2nd to last item: stop before the last item
print(secondToLast)

# Output the last three elements in the array: [7, 9, 6]
#slice(start,stop,step)
lastThree= a[slice(3,6,1)]

print(lastThree)
lastThree= a[-3:]
print(lastThree)

# Output the two middle elements in the array: [1, 7]
middle2=a[slice(2,4,1)]
print(middle2)


# Output every element except the first one: [4, 1, 7, 9, 6]
notNum1=a[slice(1,6,1)]
print(notNum1)


# Output every element except the last one: [2, 4, 1, 7, 9]
notLastNum=a[slice(0,-1,1)]
print(notLastNum)

# For string s...

s = "Hello, world!"

# Output just the 8th-12th characters: "world"

werld=s[slice(7,12)]
print(werld)