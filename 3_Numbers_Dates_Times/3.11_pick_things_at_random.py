import random
values=[1,2,3,4,5]
print(random.choice(values))
print(random.choice(values))
print(random.choice(values))
print(random.sample(values,2))
print(random.sample(values,4))
print(random.sample(values,5))

random.shuffle(values)
print(values)

a=random.randint(0,20)
print(a)
print(random.random())

