# consider the list as arraylist in java
# can be store any type of value , string , ....
# its value can be duplicate
# store multiple items in a single variable


weeks = ['Monday', 'Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
# printing list of week
print ( weeks)
#access list element
weeks[0] = '1'
print (weeks)
print(weeks[-1])#display first last index
print(weeks[-2])#display second last index
# display between list index element
print(weeks[0:2]) # display from index 0 to 2 but not include 2
#or we can write as the same 
print(weeks[:2]) #the same result , by default from index 0 to not last 2 index
#display from specifix to the end element
print (weeks[2:])

############there many ways to remove element in list
del weeks[0]# delete element where index
print (weeks)
# remove by element value name
weeks.remove('Friday')
print (weeks.pop())#remove last index
print (weeks.pop(2))#remove specifix index

print (weeks)
# length list
print (len(weeks))
#repeat list element twice
print(weeks*2)
#reverse list element
print(weeks[::-1])
# sort list
sort = weeks.sort()
print(sort)
#we can make list by its own constructor
list = list(('Dog', 'Cat',1,True))
print (list)
#get type of list
print(type(weeks)) # display <type 'list'>
# add new item to last index
weeks.append('new_item')
print(weeks)
# insert new value by specifix index
weeks.insert(0, 'insert')
print(weeks)
###### copy list to other list######
fistlist = weeks.copy() # 1.option
secondlist = list(weeks) # 2.option
###### join list ######
list1 = [1,2,3]
list2 = ['A','B','C']
list3 = list1 + list2   # 1-join option
for x in list1:         # 2- join by loop
    list2.append(x)
list1.extend(list2)     # 3- join by extend method
















