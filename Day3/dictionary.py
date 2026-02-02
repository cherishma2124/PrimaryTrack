trip={
    "source": "hyd",
    "destination": "dubai",
    "fare":3500.50,
    "status" : "completed"
}
# print(trip["status"])
# print(trip["fare"])

# print(trip.get("fare"))
# print(trip.keys())
# print(trip.values())

# for key,value in trip.items():
#     print(f"Key: {key}, Value :{value}")


#UPDATE, POP, CHANGING THE VALUE OF KEY, ITERATION
trip.update({"distance_km":150})
print(trip)

trip.pop("distance_km")
print(trip)

trip["fare"]=4000.00
print(trip)

for key in trip:
    print(key,"->", trip[key])

