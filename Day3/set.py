# myset={1,2,3,5,5,4}
# print(myset)

# uber_cities={"chennai", "banglore", "mumbai", "delhi", "hyderabad"}
# # print(uber_cities)

# uber_cities.add("pondicherry")
# print(uber_cities)

# list_cities=list(uber_cities)
# print(list_cities)
# print(type(list_cities))


uber_cities={"chennai", "banglore", "delhi", "hyderabad"}
uber_cities2={"mumbai", "kolkata","delhi","chennai"}


#UNION, INTERSECTION, DIFFERENCE
# print(uber_cities.union(uber_cities2))
# print(uber_cities.intersection(uber_cities2))
# print(uber_cities.difference(uber_cities2))


#ADD, REMOVE METHOD
uber_cities.add("pune")
print(uber_cities)

uber_cities.remove("pune")
print(uber_cities)




add=lambda a,b:a+b
print(add(5,3))


numbers=[1,2,3,4,5,6,7,8,9]
even_numbers=list(filter(lambda x: x%2==0, numbers))
print(even_numbers)

data=[
    {"name":"alice", "age":30},
    {"name":"Bob", "age":25},
    {"name":"Charlie", "age":35}
]

youngest_person=min(data, key=lambda x:x["age"]<26)
print(youngest_person)