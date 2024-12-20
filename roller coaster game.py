print("welcome to the roller coaster")
height=int(input("enter your height in cm = "))
bill=0

if height >= 120:
    print("u can ride the rollercoaster")
    age=int(input("enter your age = "))
    if age < 12 :
        bill=5
        print("you have to pay 5$")
    elif age <= 18:
        bill=7
        print("you hae to pay 7$")
    elif age >=45 and age <= 55 :
        print("you dont have to pay ")
    else:
        bill=12
        print("you have to pay 12$")
    photo=input("do yo want a photo ticket? Y or N")
    if photo == "Y" :
        
        print("you have to pay extra 3$")
        bill+=3
        print("you total amount is = ",bill)
    else:
        ("you ma go take your ride")

else:
    print("you need to grow taller")
