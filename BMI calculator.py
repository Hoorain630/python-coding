
num_1=int(input("enter a number = "))
num_2=int(input("enter a number = "))

print(type(num_1 + num_2))
print(type(str(num_1)+ str(num_2)))


#BMI calculation 
weight=int(input("enter your weight in kg= "))
height=float(input("enter your height in m= "))
height_upd =height**2
BMI = weight/height_upd
bmi_as_int=int(BMI)
print ("your BMI = ",bmi_as_int)