import random
names = input("names of people-> \n")
names = names.split(",")
l=[]
random_n = random.randint(0,len(names))

for i in range (len(names)):
  if random_n == i:
    l.append(names[i])
print(f'{l[0]} is paying')