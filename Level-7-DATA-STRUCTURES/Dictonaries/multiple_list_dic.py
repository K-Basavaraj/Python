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