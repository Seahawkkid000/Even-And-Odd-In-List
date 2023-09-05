#Program to find out how many ood and even numbers there are in a list
loop=int(input("How many numbers would you like to enter"))
if(loop==0):
    
list=[]
even=0
odd=0
def solve_odd(x):
    if(x==1):
        print("There is 1 odd number in your list")
    else:
        print("There are", x, "odd numbers in your list")
def solve_even(x):
    if(x==1):
        print("There is 1 even number in your list")
    else:
        print("There are", x, "even numbers in your list")
def print_list():
    print("Your list is", list)
for i in range(0,loop):
    number=int(input("Enter a number"))
    list.append(number)

for j in list:
    if(j%2==0):
        even=even+1
    else:
        odd=odd+1

print_list()
while True:
    print("1. Find out how many odd numbers are in your list")
    print("2. Find out how many even numbers are in your list")
    print("3. Create a new list")
    print("4. Exit")
    choice=int(input("Enter your choice"))
    if(choice==1):
        solve_odd(odd)
        print_list()
    elif(choice==2):
        solve_even(even)
        print_list()
    elif(choice==3):
        loop=int(input("How many numbers would you like to enter"))
        list=[]
        even=0
        odd=0
        for i in range(0,loop):
            number=int(input("Enter a number"))
            list.append(number)

        for j in list:
            if(j%2==0):
                even=even+1
            else:
                odd=odd+1
        print_list()
    elif(choice==4):
        leave=input("Are you sure you would like to leave? Warning: Variables and Values will not be saved")
        leave=leave.lower()
        if(leave=="yes"):
            print("Bye! Have a great day")
            break
        elif(leave=="no"):
            odd=odd
            even=even
        else:
            print("Invalid Input. Please Try Again!")
    else:
        print("Invalid Input. Please Try Again!")
