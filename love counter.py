
print("hey singles welcome to the love calculator !")
name_1=input("please enter your name = ")
name_2=input("please enter the name of your loved one = ")

combined_names= name_1 +name_2
lower_case= combined_names.lower()

t=lower_case.count("t")
r=lower_case.count("r")
u=lower_case.count("u")
e=lower_case.count("e")
first_digit=t+r+u+e

l=lower_case.count("t")
o=lower_case.count("t")
v=lower_case.count("t")
e=lower_case.count("t")
second_digit = l+o+v+e

score=int(str(first_digit)) + str(second_digit)
if (score < 10) or (score > 90):
    print(f"your score is {score}, you both go together like coke and pepsi")
elif score >=40 or score <=50:
    print(f"your score is {score}, you are alright together")
else:
    print(f"your score is {score}, you are a perfect match")

