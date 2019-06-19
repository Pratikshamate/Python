ss = input("enter any string = ")
print(ss)

frequency = {}
  
for i in ss: 
    if i in frequency: 
        frequency[i] += 1
    else: 
        frequency[i] = 1
    
print ("Count of all characters is :\n " +  str(frequency)) 