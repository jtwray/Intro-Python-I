"""
Dictionaries are Python's implementation of associative arrays.
There's not much different with Python's version compared to what
you'll find in other languages (though you can also initialize and
populate dictionaries using comprehensions just like you can with
lists!).

The docs can be found here:
https://docs.python.org/3/tutorial/datastructures.html#dictionaries

For this exercise, you have a list of dictionaries. Each dictionary
has the following keys:
 - lat: a signed integer representing a latitude value
 - lon: a signed integer representing a longitude value
 - name: a name string for this location
"""

waypoints = [
    {
        "lat": 43,
        "lon": -121,
        "name": "a place"
    },
    {
        "lat": 41,
        "lon": -123,
        "name": "another place"
    },
    {
        "lat": 43,
        "lon": -122,
        "name": "a third place"
    }
]

# Add a new waypoint to the list
# YOUR CODE HERE
waypoints.append({"lat":43,"lon":-130,"name":"a new waypoint place" })
# # waypoints[-1]=({"lat":43,"lon":-130,"name":"a new waypoint place" })
# waypoints[-1]=({"lat":43,"lon":-130,"name":"a new waypoint place" })
print(waypoints.index(waypoints[-1]), waypoints[-1])

# Modify the dictionary with name "a place" such that its longitude
# value is -130 and change its name to "not a real place"
# Note: It's okay to access the dictionary using bracket notation on the
# waypoints list.

# YOUR CODE HERE
firstWP=waypoints[0]


firstWP.update({"lon":-130,"name":"not a real place" })
print(firstWP)
print(waypoints)
# Write a loop that prints out all the field values for all the waypoints
# YOUR CODE HERE


for i in waypoints:
    print('\nline 60', (i["lat"],i["lon"],i["name"]))
    print('line 61',i)


# latlon=[( i["lat"],i["lon"]) for i in waypoints]

# print(f'waypoints[lat&lon]:{latlon}')

print('\n')
latlon=[print(f'\n waypoints[lat-lon-name][{waypoints.index(i)}]:=>> {i["lat"],i["lon"],i["name"],}') for i in waypoints]

