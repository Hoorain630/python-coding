
height = [123,120,134,156,181,102]
total_height=0
for i in list(height):
    total_height +=i
print(f"the total height ={total_height}")
students=len(height)
print (f"the total number of students ={students}")

average_height=round(total_height/students)
print(f"the average height={average_height}")