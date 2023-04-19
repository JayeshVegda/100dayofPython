colors = ["voilet", "indigo", "blue", "green"]
num = [4,2,5,3,6,1,2,1,2,8,9,7]
add = ["baby", "dog", "old"]

#METHODS

#SORT METHODS
#This method sorts the list in ascending order. The original list is updated
colors.sort()
print(colors)

num.sort(reverse=True)
print(num)


#reverse() Method
#This method reverses the order of the list.
num.reverse()
print(num)


#index()
#This method returns the index of the first occurrence of the list item.
index = colors.index('green')
print(index)

#Count()
#Returns the count of the number of items with the given value.
print(num.count(1))

#copy()
#Returns copy of the list. This can be done to perform operations on the list without modifying the original list.
copy = colors.copy()
print(copy)

#append()
#This method appends items to the end of the existing list.

colors.append('black')
print(colors)

#insert()
#This method inserts an item at the given index. 
#User has to specify index and the item to be inserted within the insert() method.

colors.insert(1, "white")
print(colors)

#extend():
#This method adds an entire list or any other collection datatype (set, tuple, dictionary) to the existing list.

colors.extend(add)
print(colors)

