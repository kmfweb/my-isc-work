def readHeader(fname):
	"Reads a data file `fname` and returns a dictionary of header metadata."
	with open(fname) as f:
		header = {}
		
		i = 0
		while i < 3:
			line = f.readline()
			# Strip any white space from line
			line = line.strip()
			print(line)
			print(line.split(":"))
			key, value = line.split(":")
			header[key] = value
			i += 1
			
	return header
	
# Test it with
head = readHeader("/home/user01/ncas-isc/python/exercises/example_data/weather_meta.csv")
print(head)
