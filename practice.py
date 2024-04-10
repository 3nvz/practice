

nums = [3,2,3] 
target = 6
result = []

mapMeBaby = {}
counter = 0

for i, v in enumerate(nums):
    diff = target - v
    
    print("Value: ", v)
    print("Index: ", i)
    print("Difference: ", diff)

    counter = counter + 1

    print(mapMeBaby, " Inside for")

    if diff in mapMeBaby:
        print(mapMeBaby[diff], i, " Inside if")
        print("Hit", counter)
    mapMeBaby[v] = i
    print("Map at the end of loop", mapMeBaby)


print("Last print", mapMeBaby)

