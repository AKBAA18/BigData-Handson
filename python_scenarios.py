"""
Python scenarios 

Collections: List, Dictionary, Tuple and Set
"""
"""
23. Create a list with a range of 10 values starting from 2 to 11 and prove mutability by updating the 3rd element 
with 100 and prove resizable properties by adding 100 in the 5th position.

listt=list(range(2,12))
print(listt)

#mutability by the updating the 3rd element with 100
listt[2] = 100
print("The list after the modification " , listt)

#add the element (100) in the 5th position 
listt.insert(4,100)
print("LIst after the insertion of the fifth element " , listt)


24. Create a tuple of 2 fields eg. ("Inceptez","Technologies","Pvt","Ltd"), 
prove immutability and non resizable nature, access the 2nd and 4th fields and store in another tuple.

tuple1=("Inceptez","Technologies","Pvt","Ltd")
print("Original tuple is : ",tuple1)

#cant be done due to python tuple immutable nature 
#tuple1.insert(2,"12") 
tuple_new = (12,23)
tuple2=tuple1.__add__(tuple_new)

print("Tuple after the adding with new tuple  :  " , tuple2)

#The tuple after the deletion is 
tuple3=tuple(i for i in tuple2 if i!=23 )
print("The tuple after the deletion is  :  " , tuple3 )

#the tuple after the insertion 
tuple4=tuple(i for i in tuple1 if i!="Technologies")

print("The tuple after the deletion is :  ",tuple4)


25. Convert the list of tuples [("Inceptez","Technologies"),("Apple","Incorporation")] 
to list of dictionary type, using for loop as given below [{"Inceptez":"Technologies"},{"Apple":"Incorporation"}] , 
once the list of dictionary is arrived print only "Incorporation" by passing "Apple" as a key using dict["Apple"] and 
dict.get("Apple") and try with dict["Apple1"] and dict.get("Apple1") then find the difference between get and using[] notation.

list1=[("Inceptez","Technologies"),("Apple","Incorporation")]
list2=[{ i[0] : i[1] } for i in list1 ]
print("The original list is  :  " , list1)
print("List after converting to dictionary  :  " , list2)

#difference between get and [] 
print("The apple key has value : " , list2[1].get("Apple") )
print("The apple key has value : " , list2[1]["Apple"] )


26. Create a list of tuple as given below and delete all duplicate tuples of the list
lst=[("Inceptez","Technologies"),("Apple","Incorporation"),("Inceptez","Technologies"),("Inceptez","Technologies")]

lst=[("Inceptez","Technologies"),("Apple","Incorporation"),("Inceptez","Technologies"),("Inceptez","Technologies")]
print("The original tuple is :  " , lst)
list2=list(set(lst))
print(set1)


27. Append ("Intel","Corp") in the above de duplicated list

lst=[("Inceptez","Technologies"),("Apple","Incorporation"),("Inceptez","Technologies"),("Inceptez","Technologies")]
print("The original tuple is :  " , lst)
list2=list(set(lst))
print(list2)
tuple1=("Intel","Corp")
list2.append(tuple1)
print("The list after the appending  :  " , list2)


28. Convert the lst_dict= [{"Inceptez":"Technologies"},{"Apple":"Incorporation"}] to 
lst1=["Inceptez","Apple"] , think about using for loop, list() function, keys function and list append functions to achieve this.

lst_dict= [{"Inceptez":"Technologies"},{"Apple":"Incorporation"}] 
print("The original list of dictionary : " , lst_dict)
list_of_key=[]
for i in lst_dict:
    list_of_key.extend(i.keys())
print(list_of_key)


29. Create a list of values lst=[10,20,40,30,20], find the first, last values of the list, 
sort the list in ascending order, sort in descending order, print the minumum and maximum values of the descending sorted list, 
find the sum of all elements in the list, remove the number 30 and 20 from the list.

from functools import reduce 
lst=[10,20,40,30,20]
print("The first value of the list is " , lst[0])
print("The last value of the list is " , lst[::-1])
#for sorting the list we use the sort function 
lst.sort()
print("The sorted list is " , lst)
lst.reverse()
print("The sorted list in reversae is " , lst)
# Max and minimun element in array is 
print("The Max element in the array is " , lst[0])
print("The min element in an array is " , lst[::-1])
#sum of element in the list
max=reduce(lambda x,y : x+y , lst)
print("The Sum of all element in list is  " , max)
#remove 30 and 20 from the list using the delete function 
set1=set(lst)
print("The list after converting to the set  " , set1)
lst=list(set1) # converting back the set to list 
lst.remove(30)
#here the 20 is 2 times in the list so we have converted the list to set and again to list 
lst.remove(20)
print("The list now is " , lst)


30. Do the above same (step 25) operation in the tuple of elements tup=(10,20,40,30,20)


31. Convert the string to list from str1="Inceptez Technologies Pvt Ltd" to lst_str1=['Inceptez', 'Technologies', 'Pvt', 'Ltd']

str1="Inceptez Technologies Pvt Ltd"
lst_str1=list(str1.split(" "))
print("The list after the string split " , lst_str1)
lst_str2=list(str1)
print("The list after directly converting it to list using list function  " , lst_str2)


32. With the below given data in the format of list(list(elements))

emplstlst= [["1", ("Arun","Kumar"), "10000"],["2", ("Bala","Mohan"), "12000"]]

Display the below output for all of the 5 given simple scenarios

a. Convert the first element of the above list into tuple

("1", ("Arun","Kumar"), "10000")

b. Print the second element's second element and reverse the first and last name as given below

("Mohan","Bala")

c. Convert the emplstlst into tuples(tuples)

emplstlst= (("1", ("Arun","Kumar"), "10000"),("2", ("Bala","Mohan"), "12000"))

d. Add all salary of the above list

22000

emplstlst= [["1", ("Arun","Kumar"), "10000"],["2", ("Bala","Mohan"), "12000"]]
tuple1=tuple(emplstlst[0])
print("The first element is converted to tuple type " , tuple1)
#the below is error because tuple is not mutable 
#print("second element's second element and reverse the first and last name  " , emplstlst[1][1].reverse())
lst2=list(emplstlst[1][1])
# reversing the list 
lst2.reverse()
tuple1 = tuple(lst2) 
print("second element's second element and reverse the first and last name  " , tuple1)
emplstlst[0] = tuple(emplstlst[0])
emplstlst[1] = tuple(emplstlst[1])
main_tuple= tuple(emplstlst)
print(main_tuple)
"""