'''
a = set([0, "a", 1, 2, 3, 5, 4])
b = set([2, 4, 6, 8])

print(a.union(b))
print(a.intersection(b))
'''

band = ["mel", "geri", "victoria", "mel", "emma"]
counts = {}

for member in band:
	if member not in counts:
		counts[member] = 1
	else:
		counts[member] += 1
		
for member in counts:
	print(member, counts[member])
