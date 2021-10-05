class Student:

    def __init__(self, stu_id, name, gender, age, major):
        self.stu_id = stu_id
        self.name = name
        self.gender = gender
        self.age = age
        self.major = major

    def display_stu_info(self):
        print("-" * 30)
        print("stu_id:" + self.stu_id)
        print("name:" + self.name)
        print("gender:" + self.gender)
        print("age:" + self.age)
        print("major:" + self.major)
        print("-" * 30)

    def format_to_student(self):
        return "{0}-{1}-{2}-{3}-{4}\n".format(self.stu_id, self.name, self.gender,
                                              self.age, self.major)
