def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View Items")
    print("4. Exit")
def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            item = input("Enter the item to be added: ")
            shopping_list.append(item)
            print(f"{item} has been added")
        elif choice == "2":
            item = input("Enter item to be removed: ")
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"{item} has been removed")
            else:
                print(f"{item} not found")
        elif choice == "3":
            if shopping_list:
                print("shopping list items:")
                for item in shopping_list:
                    print(f"- {item}")
        elif choice == "4":
            print("Exiting the Shopping List Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()                  

        