import random
friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
# Method 1
# print(random.choice(friends))

# Method 2
random_index = random.randint(0,4)
print(friends[random_index])
