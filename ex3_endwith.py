ss = input("enter any string: ")
print(ss)

a='ing'

if(ss.endswith(a)):
    print('if string with ing will be = '+str(ss)+'ly')

elif(len(ss)>=3):
    print('if string withoout ing then it will be = ' + str(ss) + 'ing')

else:
    print("string is not longer than 3 characters \n " +str(ss))

