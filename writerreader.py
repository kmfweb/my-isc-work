# How many characters has a string?

with open('haiku.text', 'r') as reader: # reads in haiku in read mode; reader is a variable
    data = reader.read()
    
with open('temp.txt', 'w') as writer:
    writer.write('elements\n')
    writer.writelines(['He\n', 'Ne\n', 'Ar\n', 'Kr\n'])
