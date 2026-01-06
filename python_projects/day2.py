'''word = "aabbcde"
count=len(word)
a={}
for char in word:
    if char in a:
        a[char]=a[char]+1
    else:
        a[char]=1
print(a)
for char in word:
    if a[char]==1:
        print(char)
        break'''
'''numbers = [1, 2, 2, 3, 4, 4, 5, 6, 6, 6, 7]

a={}
for num in numbers:
    if num in a:
        a[num]=a[num]+1
    else:
        a[num]=1
print(a)
max_count = 0  
max_num = None  
for num in a:
    if a[num] > max_count:  
        max_count = a[num]  
        max_num = num  
print(max_num)'''

"""for i in range(5):
    for a in range(i):
        print("*" ,end=" ")
    print()"""
'''def check(num):
    if num%2==0  :
        print("Even")
    else:
        print("odd")
check(17)
check(18)'''

#Movin to phase two POINTERS!
'''numbers = [5, 15, 25, 35, 45]
left = 1
right = len(numbers)-2
sum = numbers[left] + numbers[right]
print(sum)'''

"""numbers = [1, 3, 5, 7, 9]
left = 0
right = len(numbers)-1
if left < right :
    print("Pairs: {numbers[left]} & {numbers[right]}")
    left+=1
    right-=1"""

# Practicing 
# Random Number Generator
'''import random
print("Welcome! Guess the number from 1 to 100 ")
print("You Have 10 Attempts")
rnum = random.randint(1,100)
for i in range(10):
    user = int(input("Enter The Number :"))
    if user==rnum:
        print("Correct Guess! You Win")
        break
    elif user<=rnum:
        print("Wrong! Try Again (HINT: Aim Higher)")
    elif user>=rnum:
        print("Wrong! Try Again (HINT: Aim Lower)")
    elif user>100:
        print("Invalid! Enter number Betwwen 1-100")      
else:
    print("Game Over! Number is :", rnum)'''

# To do list app
'''item_list = ["ball","bat","gun","nade"]
while True:
    print("\nAction To Perform, view | add | remove | quit")
    user= input("Enter the Action : ")
    a= len(item_list)
    if user=="view":
        print("Your items :", end=" ")
        for i in range (a):
            print(item_list[i], end=" | ")

    elif user=="add":
        item=input("Enter item to add from the list: ")
        item_list.append(item)
        print(f"{item} added!")
    elif user=="remove":
        item=input("Enter item to remove from the list: ")
        if item in item_list:
            item_list.remove(item)
            print(f"{item} removed!")
        else:
            print("Error: That item is not in the list.")
    elif user == "quit":
        print("Goodbey!")
        break'''

#Phone Book using Dictionary


'''contacts = {}
while True:
    print("\n PhoneBook ")
    print("Actions To perform (Add, Search, Quit)")
    user=input("Enter Your Action : ").lower()
    if user=="quit":
        print("Goodbey!")
        break
    
    elif user=="add":
        name=input("Name : ")
        number=input("Number : ")
        contacts[name]=number
        print("Contact Saved : ", name," = ", number)
    
    elif user=="search":
        search=input("Enter Contact Name : ")
        if search in contacts:
            print("Found it!  ", contacts[search])
        else:
            print("This name doesn't Exist in Phone Book")
    else:
        print("Invalid")'''

    