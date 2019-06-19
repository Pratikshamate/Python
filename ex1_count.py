ss = input("Enter any string = ")

letter = sum(count.isalpha() for count in ss)
print('letters ' +str(letter))

digit = sum(count.isdigit() for count in ss)
print('digits ' + str(digit))



