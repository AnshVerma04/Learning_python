import math

def circle_stats(radius):
    area = math.pi*radius**2
    circumeference = 2 * math.pi*radius
    return area , circumeference

a,c = circle_stats(3)

print("area:",a,"circumeference:",c)