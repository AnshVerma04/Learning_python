Distance = float(input("Enter your Distance: "))

if Distance <3:
    Transport = "Walk"
elif Distance <=15:
    Transport = "Bike"
else :
    Transport = "Car"

print("Travel with:",Transport)