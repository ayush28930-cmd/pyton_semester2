# Create dictionary of n persons (name : city)

n = int(input("Enter number of persons: "))
persons = {}

for i in range(n):
    name = input("Enter name: ")
    city = input("Enter city: ")
    persons[name] = city

# a) Display all names
print("\nNames:")
for name in persons.keys():
    print(name)

# b) Display all city names
print("\nCities:")
for city in persons.values():
    print(city)

# c) Display student name and city
print("\nName and City:")
for name, city in persons.items():
    print(name, "->", city)

# d) Count students in each city
city_count = {}

for city in persons.values():
    city_count[city] = city_count.get(city, 0) + 1

print("\nNumber of students in each city:")
for city, count in city_count.items():
    print(city, ":", count)