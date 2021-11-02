import numpy as np

orbits = np.loadtxt('day6/input2.txt', dtype=str, delimiter="\n")

objects = []
for orbit in orbits:
    parent, child = orbit.split(")")

    if parent not in objects:
        objects.append(parent)
    if child not in objects:
        objects.append(child)

obj_indices = {"COM": 0}
objects.remove("COM")
obj_indices.update({name:index+1 for index, name in enumerate(objects)})

objects = [0] * len(obj_indices)
for orbit in orbits:
    parent, child = orbit.split(")")
    objects[obj_indices[child]] = obj_indices[parent]

san_path = []
obj = obj_indices["SAN"]
while obj != 0:
    obj = objects[obj]
    san_path.append(obj)

you_path = []
obj = obj_indices["YOU"]
while obj != 0:
    obj = objects[obj]
    you_path.append(obj)

shared = None
for obj in you_path:
    if obj in san_path:
        shared = obj
        break

you_len = you_path.index(shared)
san_len = san_path.index(shared)

print(you_len + san_len)