sample = [1, 1, 2, 3, 5, 8, 13]

# Using Python way
sample = set(sample)
sample = list(sample)
print(sample)

# Using manual checking method
for i in sample:
    if sample.count(i) > 1:
        sample.remove(i)
print(sample)
