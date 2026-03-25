"""
Building, Indexing, Adding, and Removing Keys
"""
#example1: Building Dictonaries 

inception_movie = {
    "director": "Chirstopher Nolan",
    "relased_year": "2010",
    "rating" : 8.8
}

print(inception_movie) #output: {'director': 'Chirstopher Nolan', 'relased_year': '2010', 'rating': 8.8}

#example2: indexing access with key to find the value of the rating of that movie 
print(inception_movie["rating"]) #8.8
"""
#example3: where you will get error if you access like tuples and list 
print(inception_movie[0])
    print(inception_movie[0])
          ~~~~~~~~~~~~~~~^^^
KeyError: 0
"""

#adding the data to the dict where as adding language of the movie 
inception_movie["Language"] = "English"
print(inception_movie)
#output: {'director': 'Chirstopher Nolan', 'relased_year': '2010', 'rating': 8.8, 'Language': 'English'}

#modify the existing data in the dict 
inception_movie["rating"] = 9.0
print(inception_movie)
#output: {'director': 'Chirstopher Nolan', 'relased_year': '2010', 'rating': 9.0, 'Language': 'English'}

#example5: remove the data from the dictonry using "del" key word 
del inception_movie["rating"]
print(inception_movie)
#output: {'director': 'Chirstopher Nolan', 'relased_year': '2010', 'Language': 'English'}