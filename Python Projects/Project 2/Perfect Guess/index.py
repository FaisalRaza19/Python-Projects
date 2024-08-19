# using while loop 

from random import randint;
n = randint(1,100);
a = -1
guess = 0
while(a != n):
    guess += 1;
    a = int(input("Enter the number: "));
    if(a > n):
        print("Lower number please");
    elif(a<n):
        print("Higher Number please");
    else:
        print(f"The Number is {n}.You guess the perfect number in {guess} attempt");


# using for loop 
from random import randint;
n = randint(1,100);
guess = 0

for i in range(1,30):
    guess += 1;
    
    inp = int(input("Enter the number: "));
    if(inp < n):
        print("Higher number please");

    elif(inp>n):
        print("Lower number please");
    else:
        print(f"The number is {n}.You guess perferct number in {guess} attempts");
        break;