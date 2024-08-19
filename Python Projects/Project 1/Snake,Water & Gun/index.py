import random;
user = input("Enter The Snake or Water or Gun: ");
user = user.capitalize();
print(user);
computer = random.choice(["Snake","Water","Gun"]);
print(computer);

if(user == computer):
    print("Match Will Draw");
else:
    if(user == "Snake" and computer == "Water"):
        print("User Win The Match");
    
    elif(user == "Gun" and computer == "Water"):
        print("Computer won the Match");
    
    elif(user == "Water" and computer == "Snake"):
        print("Computer Win The Match");
    
    elif(user == "Gun" and computer == "Snake"):
        print("User won the Match");
    
    elif(user == "Water" and computer == "Gun"):
        print("Computer Win The Match");
    
    elif(user == "Snake" and computer == "Gun"):
        print("Computer won the Match");
    
    else:
        print("Something went wrong");