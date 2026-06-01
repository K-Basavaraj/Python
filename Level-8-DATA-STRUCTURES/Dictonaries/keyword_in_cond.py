# Practical Application Combining iteration and key checking to search through your movies:
"""
Use in keyword to check if a key exists
Use .get() method to safely retrieve values without errors

Always verify keys exist before accessing them in large datasets
Combine with iteration to efficiently search through dictionaries

Checking for key existence prevents errors and allows graceful handling of missing data—crucial when working with 
large collections like library systems.
"""
inception_movie = {
    "director": "Chirstopher Nolan",
    "relased_year": "2010",
    "rating" : 8.8,
    "language": "English"
}

#method1
def search_movie_language(avl_lan):
    if avl_lan in inception_movie:
        return f"'{avl_lan}' is {inception_movie[avl_lan]}."
    else:
        return f"'{avl_lan}' not found."

print(search_movie_language("language"))
#method2
def search_movie_language(language):
    for key in inception_movie:
        if language in [inception_movie[key]]:
            return f"'{language}' is a {key} of this movie."
    return f"'{language}' not found in library."

print(search_movie_language("English"))

#method3
def search_movie_language(language):
    if language in inception_movie.values():
        return f"'{language}' is the language of this movie."
    else:
        return f"'{language}' not found."

print(search_movie_language("English"))

#method4 
def search_movie_language(language):
    if inception_movie["language"] == language:
        return f"Movie is in {language}."
    else:
        return f"Movie is not in {language}."

print(search_movie_language("English"))

#method5
def search_movie_language(language):
    if inception_movie.get("language") == language:
        return f"Movie is in {language}."
    else:
        return f"Movie is not in {language}."

print(search_movie_language("English"))
"""
if x in my_dict:

What it checks?
ONLY KEYS, not values

for x in my_dict:
What it gives
Keys only
"""