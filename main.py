from student_class import Student


def save_info(*args):
    file = open("./{}.txt".format(args[0]), 'w')
    file.write(args[1])
    file.write('-')
    file.write(args[2])
    file.close()


def read_file(address):
    file = open(address, 'r')
    file_content = file.readline()
    user_info = file_content.split('-')
    username = user_info[0]
    password = user_info[1]
    return username, password


def sign_up():
    username = input("please enter username to sign:")
    password = input("please enter password to sign:")
    confirm = input("are you sure you want to register,y/n:")
    if confirm == 'y' or confirm == 'Y':
        save_info("user_info", username, password)


# denglu
def sign_in():
    username, password = read_file("./user_info.txt")
    user_name = input("please enter username:")
    pass_word = input("please enter password:")
    if user_name != username or pass_word != password:
        print("username or password is not right,please enter again")
        return False
    elif user_name == username and pass_word == password:
        flag = True
        return flag


# menu
def menu():
    print("=" * 30)
    print("press 0 key for quit")
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


def fine_stu(all_student, fuzzy_key_word):
    for stu in all_student:
        if (stu.stu_id == fuzzy_key_word) or (stu.name == fuzzy_key_word):
            return stu


def delete_student_info(all_student):
    stu_key_word = input("please enter student name or stu_id to delete:")
    stu = fine_stu(all_student, stu_key_word)
    if not stu:
        print("{} is not exist".format(stu_key_word))
        exit()
    all_student.remove(stu)
    print("student {} delete success".format(stu_key_word))


def modify_student_info(all_student):
    key_word = input("please enter name or stu_id to modify:")
    stu = fine_stu(all_student, key_word)
    if not stu:
        print("{} is not exist".format(key_word))
        return
    choice = int(input("please select the content to modify\n1.stu_id;\n2.name;\n3.age:"))
    modify_key_word = input("please enter information:")
    if choice == 1:
        stu.stu_id = modify_key_word
    elif choice == 2:
        stu.name = modify_key_word
    elif choice == 3:
        stu.age = modify_key_word


def query_student_info(all_student, fuzzy_key_word):
    stu = fine_stu(all_student, fuzzy_key_word)
    if not stu:
        print("{} is not exist".format(fuzzy_key_word))
        return
    stu.display_stu_info()


def main():
    flag = sign_in()
    all_student = []
    while not flag:
        flag = sign_in()
    choice = menu()
    while flag and choice:
        if choice == 1:
            add_student_info(all_student)
        elif choice == 2:
            delete_student_info(all_student)
        elif choice == 3:
            modify_student_info(all_student)
        elif choice == 4:
            key_word = input("please enter name or stu_id to find:")
            query_student_info(all_student, key_word)
        choice = menu()


if __name__ == '__main__':
    sign_up()
    main()
