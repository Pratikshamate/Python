def reverse(s): 
    str = "" 
    for i in s: 
        str = i + str
    return str
  
s = "pratiksha"
  
print ("The original string  is : ") 
print (s) 
  
print ("The reversed string(using loops) is : ") 
print (reverse(s)) 


#short cut method for reverse string
'''
print(string[::-1])
'''