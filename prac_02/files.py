def question_1():
    out_file = open("name.txt", "w")
    name = input("Enter name: ")
    print(name, file=out_file)
    out_file.close()

def question_2():
    in_file = open("name.txt", "r")
    name = in_file.read()
    in_file.close()
    print("Your name is {}".format(name))

def question_3():
    in_file = open("numbers.txt", "r")
    number_1 = int(in_file.readline())
    number_2 = int(in_file.readline())
    in_file.close()
    print(number_1 + number_2)

def question_4():
    in_file = open("numbers.txt", "r")
    total = 0
    for i in in_file:
        number = int(i)
        total += number
    in_file.close()
    print(total)
question_4()