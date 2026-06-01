movies = [
    {
        "name": "Inception",
        "director": "Christopher Nolan",
        "year": 2010,
        "language": "English"
    },
    {
        "name": "Bahubali",
        "director": "S. S. Rajamouli",
        "year": 2015,
        "language": "Telugu"
    },
    {
        "name": "Interstellar",
        "director": "Christopher Nolan",
        "year": 2014,
        "language": "English"
    }
]

def search_movies_by_language(language):
    result = []
    
    for movie in movies:
        if movie.get("language") == language:
            result.append(movie["name"])
    
    return result

print(search_movies_by_language("English"))

#output: ['Inception', 'Interstellar']

#in with LIST
print("Inception" in ["Inception", "Bahubali"]) #True

#in with DICTIONARY
if "name" in movies[0]:
    print("Key exists")


#in with .values()
if "English" in movies[0].values():
    print("Value exists")

#in with LOOP 
for movie in movies:
    if "English" in movie.values():
        print(movie["name"])

# Reordering Dictionary Keys by Inserting a New Key at Specific Position
# ## Adding 'rating' key after 'director' by converting dictionary to ordered list
items = list(movies[0].items())

items.insert(2, ("rating", 8.8))  # position after director

movies[0] = dict(items)

print(movies[0])

#Since dictionaries don’t support positional insertion, so convert it to a list of items, insert at the required index, and reconstruct the dictionary.