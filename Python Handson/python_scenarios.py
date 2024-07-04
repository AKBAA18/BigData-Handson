"""
Created on Sun Mar 31 08:40:36 2024

@author: aksha

BigData Scenarios 
"""
"""
Variables
1. Create 2 variables with x as 100 & y as 10 respectively and find the Multiplication and division of both and store in some val as z and z1.

x=100
y=10
z=x*y
z1=x/y
print(z)
print(z1)

2. Create a as 2000 and find the division of a by y (created in step 1) and reassign a with the divided result (200).

a=2000
print("Entered value is " , a)
y=10
a=int(a/y)
print("After operation " , a)


3. Prove Python is Dynamically Typed Language: Create x:int=100, then assign the x to y, but the datatype of y has to be of type string. (think about using some function like str()). Print the type of y and x

x:int=100
y:str=str(x)
print(type(x))
print(type(y))


4. Prove Python has dynamic inference feature 

x=5
print(type(x)) # without any datatype x is automatically identified as integer 
y="String"
print(type(y)) # without any datatype y is identified as string 


5. Prove Python is Strongly Typed Language

x = 18   # automatically x is identified as integer by python due to dynamix inference 
y = "2"

#Python's strong typing nature where operations between incompatible types result in errors
z=x+int(y) # converting the string to integer 

print( z ) # Here the operations cant be done because the x is integer and y is string 


6. Create variables a,b,c,d assigned with 10,20,30,40 respectively

a,b,c,d=10,20,30,40
print(a)
print(b)
print(c)
print(d)


7. Prove Python variables are case sensitive

#These variable are case sensitive 
var=12 # var is a variable 
Var=23 # Var is another variable 
print(var)
print(Var)


8. Prove variable name can’t start with numbers or cannot contains special character other than _

#9var=34  The variable cant start with numbers

#$var=34  The variable cant start with special charecters 


9. Show some examples of when do we use single, double and triple (single/double) quotes

string1='Akshaya Baalaji'
print(string1) # with single quote
string2="Akshaya Baalaji"
print(string2) # with double quote which work as same as single quote
##string3="""#This is a multi line value 
#    HI 
#    Bye 
#    See 
#    you 
"""
print(string3) # for multi line value 


10. Show an examples to use arithmetic, comparison, relational and logical operators.

# Arithmetic operators
x = 10
y = 3

print("Arithmetic operators:")
print("x + y =", x + y)  # Addition
print("x - y =", x - y)  # Subtraction
print("x * y =", x * y)  # Multiplication
print("x / y =", x / y)  # Division
print("x // y =", x // y)  # Floor Division
print("x % y =", x % y)  # Modulus
print("x ** y =", x ** y)  # Exponentiation
print()

# Comparison operators
print("Comparison operators:")
print("x == y is", x == y)  # Equal to
print("x != y is", x != y)  # Not equal to
print("x > y is", x > y)  # Greater than
print("x < y is", x < y)  # Less than
print("x >= y is", x >= y)  # Greater than or equal to
print("x <= y is", x <= y)  # Less than or equal to
print()

# Relational operators
print("Relational operators:")
a = [1, 2, 3]
b = [1, 2, 3]
c = a
print("a is b is", a is b)  # Identity - checks if a and b reference the same object
print("a is c is", a is c)  # Identity - checks if a and c reference the same object
print("a == b is", a == b)  # Equality - checks if the values of a and b are the same
print()

# Logical operators
print("Logical operators:")
p = True
q = False
print("p and q is", p and q)  # Logical AND
print("p or q is", p or q)    # Logical OR
print("not p is", not p)       # Logical NOT


Conditional Structures

11. Write a program to find the greatest of 3 numbers

#using list built in functions 
make_list=[a,b,c] # making the list from the variables 
print(max(make_list));
#we can take the greatest by sorting and taking the last element in list 
make_list.sort(); #sort will sort the list 
print("Taking the last elemrent from the list ",make_list[-1])

#using simple conditional structure 
a=10
c=10
b=30
if a==b and a==c :
    print("All are same ")
elif a>=b and a>=c :
    print(a, " is the greatest ")
elif b>=a and b>=c :
    print(b, " is the greatest ")
else :
    print(c, " is the greatest ")

#using nested conditional structure 
a=900
b=900
c=100

if a==b and b==c:
    print("All are same ")
else :
    if a>=b and a>=c:
        print("A is greater ")
    elif b>=a and b>=c :
        print("B is greater ")
    else :
        print("C is greater ")


12. Write a single program to find the given number is even or 
whether it is negative and print the output as 
(the given number is even but not negative or the given number is not even but negative or 
the given number is neither negative nor even) 

number=int(input("Enter a number : "))
if number%2==0 and number>0 :
    print("The given number is even but not negative")
elif number<0 and number%2!=0 : 
    print("The given number is not even but negative")
elif number>0 and number%2!=0:
    print("The given number is not negative and not even")
else:
    print("The given number is neither negative nor even")


13. Write a nested if then else to print the course fees - check if student choosing bigdata, then fees is 25000, 
if student choosing spark then fees is 15000, if the student choosing datascience then check if machinelearning then 25000 
or if deep learning then 45000 otherwise if both then 25000+25000.

course=input("Enter the course you want to register : ")
subcourse:str
if course in 'bigdata':
    print("Your fees is 25000")
elif course in 'spark':
    print("Your fees is 15000")
elif course in 'datascience':
    subcourse=input("..............Subcourses available................\nmachine learning or deep learning want or both \nEnter the course want to register in data science : ")
    if subcourse in 'machine learning':
        print("Your fees is 25000")
    elif subcourse in 'deep learning':
        print("Your fees is 45000")
    else :
        print("The fees is 20000+25000")
else:
    print("Enter the correct course ")


14. Check whether the given string is palindrome or not (try to use some function like reverse). 
For eg: x="madam" and y="madam", if x matches with y then print as "palindrome" else "not a  palindrome".

string = input("Enter a string ")
reverse_way1 = string[::-1]
print("The string you Entered : " , string)
print("The Reverse string done by indexing   : " , reverse_way1)
reverse_way2:str=""

for i in string : 
    reverse_way2 = i + reverse_way2 

print("The Reverse string done by for loop   : ",reverse_way2)

print()

if reverse_way1 in string :
    print("Entered string is a Palindrome ")
else :
    print("Entered string is not a palindrome ")



15. Check whether the x=100 is an integer or string. (try to use some functions like str or upper function etc 
to execute this use case) or use isinstanceof(variablename,datatype) function.

string="100"
x=100
#isinstance check string is a datatype of str type   
if isinstance(string, str):
    print("It is a string ")

#isinstance check x is a datatype of int type
if isinstance(x , int ):
    print("It is a integer ")



Control Statements

16. Write a program using for loop to print even numbers and odd numbers in the below range of data 
(generate using range function) [5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20] 
output should be with even as 6,8,10,12,14,16,18,20 and odd as 5,7,9,11,13,15,17,19.

for i in range (5,21,1):
    if i%2==0 :
        print (i , end=" ")
        print()
    else:
        print (i , end=" ")


even=[]
odd=[]
for i in range (5,21,1):
    if i%2==0 :
        even.append(i)
    else:
        odd.append(i)
print("Odd list is " , odd)
print("Even list is " , even)


17. Write a while loop to loop from 0 till 21 with the increment of 3, 
the result should be exactly 3,6,9,12,15,18 and store this result in a list

i=0
incremented_list=[]
while i<21:
    i=i+3
    incremented_list.append(i)

print("The list " , incremented_list)    


18. Write a for or while loop to print the cube of 4, 
result should be 4*4*4=64 (initiate some variable outside the loop with 4 and loop through 3 times to achieve the result)

loop=3
i=0
number=int(input("Enter a number : "))
cube_while=1
while i<loop:
    cube_while=cube_while*number
    i=i+1
print(cube_while)
print(f"The number of time iterated {loop} and the cube found out is {cube_while}" )
cube_for=1
for i in range (0,loop,1):
    cube_for=cube_for*number    
print(f"The number of time iterated {loop} and the cube found out is {cube_for}" )
    

19. Create a list as sal_lst=[10000,20000,30000,10000,15000], loop through the list 
and add 1000 bonus to the salary and store in another list sal_bonus_lst=[11000,21000,31000,11000,16000]
then store the bonus applied salary in another list where sal>11000

sal_lst=[10000,20000,30000,10000,15000]
bonus=1000
add=0
sal_bonus_list=[]
print("The list before bonus " , sal_lst)
for i in sal_lst:
    add=i+bonus
    sal_bonus_list.append(add)
print("The list after adding bonus " , sal_bonus_list)


20. Write a do while loop to print “Inceptez technologies” n number of times as per the 
input you get from the user. Minimum it has to be printed at least one time regardless of the user input.

i=0
loop=int(input("Enter the number of time loop has to happen : "))
#if the loop is 0 it prints infinite time 
if loop < 1:
    loop = 1
while True :
    print("Inceptez Technologies ")    
    i=i+1
    if i==loop :
        break
       

21. From the given list of list of elements produce the following output using nested for loop
lst1=[[10,20],[30,40,50],[60,70,80]], calculate the sum of all number, calculate the min value and 
the max value of all the elements in the lst1.

lst1=[[10,20],[30,40,50],[60,70,80]]
#to make the array of array to single array 
list2=sum(lst1,[])
print(list2)
print("The max element in array is " , max(list2))
print("The min element in array is " , min(list2))


sum_of_ele=0
for i in lst1 :
    for j in i:
        sum_of_ele=sum_of_ele+j

print("The sum of the element is : " , sum_of_ele )


22. Create a looping construct to create 3 tables upto 10 values. Output should be like this…
1 x 3 = 3
2 x 3 = 6
3 x 3 = 9
.
.
10 x 3 = 30
number = int(input("Enter the number for table : "))
#using simple for 
for i in range (0,11,1):
    print(f"{i} x {number} = " , number*i)

#using nested for loop 
table=int(input("Enter the number for table "))
for i in range (0,11,1):
    for j in range (0,11,1):
        if j == table:
            print(f"{i} x {table} = " , j*i)

#using nested for and using continue constructs
number = int(input("Enter the number for table : ")) 
print("Nested loop :")
# using nested for loop 
for i in range (1,number+1,1):
    for j in range (0,11,1):
        if(i==5 or i ==10):
            continue
        else :
            print (f"{i} x {j} = ", i*j )
"""
"""
Pattern printing :
    
n = int(input("Enter the number for the pattern "))
for i in range (0,n , 1):
    for j in range (0,i,1):
        print(" " , end=" ")
    for  k in range (n,i,-1):
        print("*" , end=" ")
    print()
"""

"""
#Usecase2 related to exit controlled loop (do while loop) + break & continue:
#Create a scheduler program to run a code minimum once or continue to run multiple hours + skipping odd hours

start_time = int(input("Enter the start time in 24 hours format "))
end_time = int(input("Enter the end time in 24 hours format "))

#using for loop
print("Using for loop")
for i in range (start_time , end_time+1 ,1):
    if i%2==0 : 
        print("Script is running ")
    else : 
        continue;
#using while loop 
print("Using do while ")
while start_time <= end_time:
    if start_time%2==0 : 
        print("Script is running " , start_time)
        start_time=start_time+1
    else :
        start_time=start_time+1
        continue;
"""
"""
print("Usecase3 : Complex Tuple - 
tuple(familyid:int,familyname:str,familymembers:list[dict{k:v,k:v,k:dict{k:v,k:v}}])")

dictionary={"Family id " : 1 , "Family_name" : "AB Family"  ,"fammily_members" : [{"Father" : "Senthilraj" , "Mother name" : "Vijiyalakshmi" , "Son" : "Akshaya Baalaji " }] }
# tuple elements / members are int , string , list [dictionary inside list ]
tuplee=(1 , "AB Family"  ,[{"Father" : "Senthilraj" , "Mother name" : "Vijiyalakshmi" , "Son" : "Akshaya Baalaji " }] )
print(dictionary);
print("Complex Tuple created is : " , tuplee)

complextup=(1,
            "Madison's Family",
            [{"gender":"male","Relation":"self","personalinfo":{"title":"Ms","name":"Madison"}},
             {"gender":"female","Relation":"spouse","personalinfo":{"title":"Mrs","name":"Elisa"}},
             {"gender":"female","Relation":"daughter","personalinfo":{"title":"Miss","name":"Hanna","hobby":"book reading"}},
             {"gender":"male","Relation":"son","personalinfo":{"title":"Master","name":"Dave","schooling":True}}])

print("1  id is ",complextup[0])
print("2  Family name is ",complextup[1])
print("3  gender of first list element is ",complextup[2][0].get("gender"))
print("4  relation of first list element is ",complextup[2][0].get("Relation"))
print("5  personalinfo of the first list element is ",complextup[2][0].get("personalinfo"))
print("5 i  personalinfo of the first list element is ",complextup[2][0]["personalinfo"])

print("6  personalinfo title of the first list element is ",complextup[2][0]["personalinfo"]["title"])
print("7  personalinfo name of the second list element is " ,complextup[2][1]["personalinfo"]["name"])
print("8  personalinfo hobby of the third list element is " ,complextup[2][2]["personalinfo"]["hobby"])
print("9  personalinfo schooling info of the fourth list element is " ,complextup[2][3]["personalinfo"]["schooling"])

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
