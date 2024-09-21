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
    print("\n---- New test subject ----")
    new_subject_number = input("Number: ")
    new_subject_time = int(input("Time: "))
    return new_subject_number, new_subject_time

def write_data(test_subjects, filename):
    with open(filename, "w") as file:
        for test_subjects in test_subjects:
            file.write(test_subjects[0] + "\n")
            file.write(str(test_subjects[1]) + "\n")
    print("*** Data written to file ***")


def read_data(filename):
    test_subjects = []
    with open(filename, "r") as file:
        lines = file.readlines()
        for i in range(0, len(lines), 2):
            test_subject_number = lines[i].strip() #Remove newline character
            test_subject_time = int(lines[i+1].strip())
            test_subjects.append((test_subject_number, test_subject_time))
    print("*** Data read from file ***")
    return test_subjects

def print_test_subjects(test_subjects):
    print("\n---- Registered test subjects ----")
    for subject_number, subject_time in test_subjects:
        print(f"Number : {subject_number:>5}")
        print(f"Time   : {subject_time:>5}\n")


def main():
    test_subjects = []
    choice = "z"
    while choice != "q":
        print_menu()
        choice = input("Your choice: ")
        if choice == "a":
            test_subjects.append(new_test_subject())
        elif choice == "s":
            print_test_subjects(test_subjects)
        elif choice == "r":
            filename = input("Filename: ")
            test_subjects = read_data(filename)
            print_test_subjects(test_subjects)
        elif choice == "w":
            filename = input("Filename: ")
            write_data(test_subjects, filename)


if __name__ == "__main__":
    main()