#Checking for the Existence of Keys
"""
When working with large dictionaries like a library system with thousands of movies, you need to verify 
if specific keys exist before accessing their values. 
Attempting to access a non-existent key will cause an error.
"""
#Using the in Keyword The simplest way to check if a key exists:
inception_movie = {
    "director": "Chirstopher Nolan",
    "relased_year": "2010",
    "rating" : 8.8,
}

# Check if movie language is exist or not in the dict 
if "language" in inception_movie:
    print(f"Found! langauge: {inception_movie['lanaguge']}")
else:
    print("lanaguage not found of that movie") 
#output: lanaguage not found of that movie

# Check if movie rating is exist or not in the dict 
if "rating" in inception_movie:
    print(f"Found! Rating: {inception_movie['rating']}")
else:
    print("rating not found for this movie") 
#output: Found! Rating: 8.8