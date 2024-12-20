

print("welcome to python pizza!")
size=input("which size pizza would u like to order ? S , M , L = ")
pepporoni=input("would you like to add your peporni ? Y or N")
cheese=input("would u like to add extra cheese ? Y or N")
bill=0
if size == "S":
    bill+=10
elif size == "M":
    bill+=20
else :
    bill+=30
if pepporoni == "Y":
    if size == "S":
        bill+=2
    else:
        bill+=3
if cheese == "Y":
    bill+=1
print(f"thankyou for purchasing your pizza from python pizza your total bill will be {bill}$ ,have a nice day !")