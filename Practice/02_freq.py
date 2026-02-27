x = [5,3,2,2,1,5,5,7,3,10]
y = [10,111,1,9,5,67,2]

freq = {}

# Build frequency dictionary
for num in x:
    freq[num] = freq.get(num, 0) + 1

print(freq)

# Query part
for j in y:
    print(freq.get(j, 0))
