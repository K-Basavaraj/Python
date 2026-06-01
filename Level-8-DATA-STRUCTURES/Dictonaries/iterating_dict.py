"""
Efficiently managing substantial collections, like a library with thousands of books or articles, is essential. 
Here's a simple way to iterate through a Python dictionary which organizes titles and genres:
"""

inception_movie = {
    "director": "Chirstopher Nolan",
    "relased_year": "2010",
    "rating" : 8.8,
    "language" : "English"
}

print(inception_movie) #{'director': 'Chirstopher Nolan', 'relased_year': '2010', 'rating': 8.8, 'language': 'English'}

#Loop Through Keys: Use: for key in inception_movie Output: Prints all movie info
for keys in inception_movie:
    print(keys)

"""
output: 
director
relased_year
rating
language
"""
#Loop Through Values:  Use: for key in inception_movie.values()  Output: Prints all key data
for value in inception_movie.values():
    print(value)
"""
output: 
Chirstopher Nolan
2010
8.8
English
"""
#Loop Through Both Keys and Values: Use: for key, value in inception_movie.items() Output: Prints titles with corresponding values
for key, value in inception_movie.items():
    print(f"{key}: {value}")
"""
output: 
director: Chirstopher Nolan
relased_year: 2010
rating: 8.8
language: English
"""