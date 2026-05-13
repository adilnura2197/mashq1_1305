class Student:
    school_name = "Najot Ta'lim"
    country = "Uzbekistan"

    def __init__(self, fullname, age, course, grade):
        self.fullname = fullname
        self.age = age
        self.course = course
        self.grade = grade

    def show_info(self):
        print(f"Ism: {self.fullname}")
        print(f"Yosh: {self.age}")
        print(f"Kurs: {self.course}")
        print(f"Bahosi: {self.grade}")
        print(f"Maktab: {Student.school_name}")
        print(f"Mamlakat: {Student.country}")

    def change_grade(self, new_grade):
        print(f"{self.fullname} bahosi o'zgardi: {self.grade} -> {new_grade}")
        self.grade = new_grade


s1 = Student("Azamat", 21, "Backend", "B")
s2 = Student("Ali", 19, "Frontend", "C")
s3 = Student("Vali", 22, "Design", "A")


s1.show_info()
print()
s2.show_info()
print()
s3.show_info()
