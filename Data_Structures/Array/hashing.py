num = "aabbhi"


hashmap = {}

for i in range(len(num)):
    if num[i] in hashmap:
        hashmap[num[i]] += 1
    else:
        hashmap[num[i]] = 1


print(hashmap)