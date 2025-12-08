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
        choice = input("Enter your choice (1-4): ")
            try:
                choice_num = int(choice)
                if 1 <= choice_num <= 4:
                    break  # valid number
                else:
                    print("Please enter a number between 1 and 4.")
            except ValueError:
                print("Invalid input. Please enter a number.")


        if choice_num == "1":
            item = input("Enter the item to be added: ")
            shopping_list.append(item)
            print(f"{item} has been added")
        elif choice_num == "2":
            item = input("Enter item to be removed: ")
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"{item} has been removed")
            else:
                print(f"{item} not found")
        elif choice_num == "3":
            if shopping_list:
                print("shopping list items:")
                for item in shopping_list:
                    print(f"- {item}")
        elif choice_num == "4":
            print("Exiting the Shopping List Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()                  
