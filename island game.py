


print("welcome to the treasure island")
print("your mission is o fine the treasure")
direction= input("your are at the croos road ,where do u want to go ? type left or right = ")
if direction == "left":
    print ("you have come to the lake , there is an island in the middle of the lake ")
else:
    print("game over")
level_2=input("type 'swim' if you want to swim ,other wise type 'wait' to wait for the boat = ")
if level_2 == "wait" :
    print("you have reached the island un harmed")
else:
    print("game over , you are eaten by the sharks")
level_3=input("you have three doors in front of you which one would u like to choose ? red mblue,or purple= ")
if level_3 ==  "purple":
    print("congratulations! you have entered the room with food , you won!")
else:
    print("you have entered the room with beastes ,you lost!")
