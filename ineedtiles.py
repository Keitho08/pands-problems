# This is program calculates how many tiles you will need 
# when tiling a wall or floor (in m2).

lenght = float(input("enter room length: "))
width = float(input("enter room width: "))

#length = 3.5
#width = 2.3

area = lenght * width
needed = area * 1.05 

print("You need", needed, "metres squared of tiles.")