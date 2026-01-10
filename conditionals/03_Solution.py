Score = int(input("Enter your Score: "))

if Score > 100 or Score < 0:
    print(" Please verify your grade again")
    exit()

if Score >= 90:
    grade = "A"
elif Score >= 80:
    grade = "B"
elif Score >= 70:
    grade = "C"
elif Score >= 60:
    grade = "D"
else:
    grade = "F"

print(" Your Grade is:", grade)