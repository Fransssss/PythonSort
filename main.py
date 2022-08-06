# Author: Fransiskus Agapa

the_name = lambda first, last: first + ' ' + last

print("\n== Employee Database ==")
print("1. Input data")
print("2. Output data")
print("e. Exit")
choice = input("choice: ").lower()            # user input to lower case - while-loop condition becomes simpler

employee_list = []

while choice != 'e':
    if choice == '1':
        print("\n -- Input data --")
        fs_name = input("Input first name: ").capitalize()
        if fs_name.isdigit():
            print("\n[ Invalid input - string only ]")
        else:
            ls_name = input("Input last name: ").capitalize()
            if ls_name.isdigit():
                print("\n[ Invalid input - string only ]")
            else:
                emp_name = the_name(fs_name, ls_name)
                employee_list.append(emp_name)
                print("\n[ Database updated ]")

    elif choice == '2':
        print("\n -- Output data --")
        if len(employee_list) == 0:
            print("[ Database is empty ]")
        else:
            to_sort = input("\nWould you like to sort the output (yes/no): ").lower()
            if to_sort == "yes":
                print("")                 # put new line
                employee_list.sort()      # sort data
                for i in employee_list:
                    print(i)

            elif to_sort == "no":
                print("")
                for i in employee_list:
                    print(i)

            else:
                print("\n[ Invalid response ]")

    else:
        print("\n[ Invalid choice ]")

    print("\n== Employee Database ==")
    print("1. Input data")
    print("2. Output data")
    print("e. Exit")
    choice = input("choice: ").lower()

print("\n== Exit Program ==")
