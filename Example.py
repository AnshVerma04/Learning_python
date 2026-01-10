student = {
    "name": "Ansh",
    "age": 22,
    "course ": "BCA",
    "grade" :"A++"
}
print(student.get("age"))          # 22
print(student.get("grade", "N/A")) # N/A (since "grade" not found)
