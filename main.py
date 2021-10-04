from student_class import Student


def login():
    username = input("please enter username:")
    password = input("please enter password:")
    if username == "123456" and password == "123456":
        flag = True
        return flag


def menu():
    print("=" * 30)
    print("1.add student information")
    print("2.delete student information")
    print("3.modify student information")
    print("4.query student information")
    print("=" * 30)
    choice = input("please enter the action you want:")
    return int(choice)


def add_student_info(all_student):
    stu_id = input("please enter stu_id:")
    name = input("please enter student name:")
    gender = input("please enter gender(0 for female,1 for male)")
    age = input("please enter student age:")
    major = input("please enter student major:")
    stu = Student(stu_id, name, gender, age, major)
    all_student.append(stu)


def query_student_info(all_student,fuzzy_key_word):
    for stu in all_student:
        if (stu.stu_id == fuzzy_key_word) or (stu.name == fuzzy_key_word):
            stu.display_stu_info()
            return
    return None


def main():
    flag = login()
    choice = menu()
    all_student = []
    while flag and choice:
        print("welcome to system")
        if choice == 1:
            add_student_info(all_student)
        elif choice == 2:
            print("delete student information")
        elif choice == 3:
            print("modify student information")
        elif choice == 4:
            key_word = input("please enter name or stu_id to find:")
            query_student_info(all_student,key_word)
        choice = menu()


if __name__ == '__main__':
    main()