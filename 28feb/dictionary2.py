movies = {}

n = int(input("\nEnter number of movies: "))

for i in range(n):
    name = input("\nMovie name: ")
    year = int(input("Year: "))
    director = input("Director: ")
    cost = float(input("Production cost: "))
    collection = float(input("Collection: "))

    movies[name] = {
        "year": year,
        "director": director,
        "cost": cost,
        "collection": collection
    }

# a) Print all movie details
print("\nAll Movie Details:")
for name, details in movies.items():
    print(name, ":", details)

# b) Movies released before 2015
print("\nMovies released before 2015:")
for name, details in movies.items():
    if details["year"] < 2015:
        print(name)

# c) Movies that made profit
print("\nProfitable Movies:")
for name, details in movies.items():
    if details["collection"] > details["cost"]:
        print(name)

# d) Movies by a particular director
dname = input("\nEnter director name to search: ")

print("Movies by", dname)
for name, details in movies.items():
    if details["director"].lower() == dname.lower():
        print(name)