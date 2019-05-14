file = open('Raw.txt', 'r')

sortedlist = []

for line in file:
    if 'bmRequestType: 0xc0' in line:
        sortedlist.append(line)
        sortedlist.append(next(file))
        sortedlist.append(next(file))
        sortedlist.append(next(file))
        sortedlist.append(next(file))
        
file.close()
    
file = open('Sorted.txt', 'w')

for line in sortedlist:
    file.writelines(line)
    
file.close()    
    


            
