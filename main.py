from fileinput import filename

def print_menu():
    print("--------- Menu ----------")
    print("a) Add a new test subject")
    print("s) Show all information")
    print("r) Read from file")
    print("w) Write to file")
    print("q) Quit")
    print("-------------------------\n")

def new_test_subject():
    print("---- New test subject ----")
    new_subject_number = input("Number: ")
    new_subject_time = int(input("Time: "))
    new_subject = (new_subject_number, new_subject_time)
    return new_subject

def write_data(test_subjects, filename):

    with open(filename, "w") as file:
        for i in test_subjects:
            i = str(i)
            file.write(f"{i[0]}\n{i[1]}\n")


def read_data(filename):
    with open(filename, "r") as file:
        return file.read()

def print_test_subjects(test_subjects):
    print("---- Registered test subjects ----")
    for i in test_subjects:
        print(f"Number : {test_subjects[0]:>5}")
        print(f"Time   : {test_subjects[1]:>5}\n")


def main():
    test_subjects = []
    choice = "z"
    while choice != "q":
        print_menu()
        choice = input("Your choice: ")
        if choice == "a":
            test_subjects = new_test_subject()
        elif choice == "s":
            print_test_subjects(test_subjects)
        elif choice == "r":
            test_subjects = read_data(filename)
        elif choice == "w":
            write_data(test_subjects, "filename.txt")
        elif choice == "q":
            print("Goodbye!")


if __name__ == "__main__":
    main()