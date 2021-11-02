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

counts = 0
for obj in objects:
    counts += 1
    while obj != 0:
        obj = objects[obj]
        counts += 1
print(counts - 1)