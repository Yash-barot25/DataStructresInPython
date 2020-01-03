cars = {"Lambo": "A glamorous look with power",
        "Tesla": "A very first driver less electrical car",
        "Bugatti": "A very high speed car of the century, also very expensive",
        "Maserati": "A luxuries car"}
bikes = {"Bmw": "A most advanced moterbike",
         "splender": "A ride of a common man",
         "harleydevidson": "A sporty ride"}

print(cars)
print(bikes)
print(cars.keys())
print(cars.values())
cars.update(bikes)
print(cars)
newcars = cars.copy()
print(newcars)

print(cars["Tesla"].split())
print(cars["Bugatti"].split(","))
print(" ".join(cars["Tesla"].split()))
