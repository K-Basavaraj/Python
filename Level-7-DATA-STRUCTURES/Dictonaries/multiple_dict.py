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

print(movies)
"""
[ {'name': 'Inception', 'director': 'Christopher Nolan', 'year': 2010, 'language': 'English'}, 
  {'name': 'Bahubali', 'director': 'S. S. Rajamouli', 'year': 2015, 'language': 'Telugu'}, 
  {'name': 'Interstellar', 'director': 'Christopher Nolan', 'year': 2014, 'language': 'English'}
]
"""

#access any one movie 
print(movies[0]) #{'name': 'Inception', 'director': 'Christopher Nolan', 'year': 2010, 'language': 'English'}
print(movies[1]) #{'name': 'Bahubali', 'director': 'S. S. Rajamouli', 'year': 2015, 'language': 'Telugu'}
print(movies[2]) #{'name': 'Interstellar', 'director': 'Christopher Nolan', 'year': 2014, 'language': 'English'}

#access any two movies 
print(movies[0:2]) #it print 0th and 1st dictronory items
print(movies[0:3:2])
print([movies[0], movies[2]])

for i in [0, 2]:
    print(movies[i])

#Access specific value
print(movies[0]["name"])   # Inception

#Add new movie 
movies.append({
    "name": "Salaar",
    "director": "Prashanth Neel",
    "year": 2023,
    "language": "Telugu"
})

print(movies)

#Add new key inside movie
movies[0]["rating"] = 8.8
print(movies)

#Remove key 
del movies[0]["rating"] 
print(movies)

#Remove movie
movies.pop(3)
print(movies)

# Loop basic 
for movie in movies:
    print(movie)
"""
{'name': 'Inception', 'director': 'Christopher Nolan', 'year': 2010, 'language': 'English'}
{'name': 'Bahubali', 'director': 'S. S. Rajamouli', 'year': 2015, 'language': 'Telugu'}
{'name': 'Interstellar', 'director': 'Christopher Nolan', 'year': 2014, 'language': 'English'}
"""

#Loop through KEYS 
for key in movies[0]:
    print(key)

#Loop through values 
for values in movies[0].values():
    print(values)

#Loop through keys: values 
for key, values in movies[0].items():
    print(f"{key}: {values}")

for key, value in movies[1].items():
    print(key, ":", value)

#Using .get() 
print(movies[0].get("name"))        # Inception
print(movies[0].get("rating"))      # None (no error)

#Using == (condition check)
if movies[0]["language"] == "English":
    print("This is an English movie")

#Condition inside loop (real use)
for movie in movies:
    if movie["language"] == "English":
        print(movie["name"])

#Using .get() + condition 
for movie in movies:
    if movie.get("director") == "S. S. Rajamouli":
        print(movie["name"])