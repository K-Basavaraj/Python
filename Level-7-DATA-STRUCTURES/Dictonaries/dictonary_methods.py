#Using the .get() Method The .get() method safely retrieves values without causing errors:
inception_movie = {
    "director": "Chirstopher Nolan",
    "relased_year": "2010",
    "rating" : 8.8,
}

# Returns None if key doesn't exist
movie = inception_movie.get("Language") #it wont print anything in the terminal
print(movie) # it will print None 

# Or provide a default value
movie = inception_movie.get("Language", "Not in dictonary")
print(movie)  # Output: Not in dicronary