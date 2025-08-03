#created an empty list
my_list=[]
#appending elements to the list 
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
#inserting an element at a specific position
my_list.insert(1,15)
#extending the list with another list
my_list.extend([50, 60,70])
#removing an element from the list
my_list.remove(my_list[-1])
my_list.sort()
print(my_list)
index_30 = my_list.index(30)
print("Index of value 30:", index_30)

   