

# the title of map
def new_dow(n):
	return n*2


dowbles3 = [new_dow(x) for x in range(100)]
print("================")
dowbles4 = [2*x for x in range(10)]

print("+++++++++++++++++")
print('sajid Main app')



def update(n):
	return n*2

dowbles = [i for i in range(10)]

newdowbles = list(map(update, dowbles))

#print(newdowbles)

newdowbles2 = list(map(lambda n: n*2, dowbles))



def new_map(n):
	return n*10000


new_array = [new_map(x)  for x in range(10)]


for i in list(new_array):
	print(i)











