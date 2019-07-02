list1 = [1,2,3,4,1,5,3,2,5]
list2 = []

def unique_list():
    for i in list1:
        if i not in list2:
            list2.append(i)
    print(list2)


unique_list()            
