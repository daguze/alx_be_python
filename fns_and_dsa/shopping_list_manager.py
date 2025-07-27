
def display_menu():
    print("Shopping List Manager")
    print("1. Add item to shopping list")
    print("2. Remove item from shopping list")
    print("3. View shopping list")
    print("4. Exit")
def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("enter your choice: ")
        if choice == "1":
            item = input("Enter item to add: ")
            shopping_list.append(item)
            print(f"added {item} to shopping list.")
        elif choice == "2":
            item = input("enter item to be removed:")
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"removed {item} from shopping list.")
            else:
                print(f"{item} not found in shopping list.")
        elif choice == "3":
            if shopping_list:
                print("shopping list:")
                for i,item in enumerate(shopping_list,start=1):
                    print(f"{i}.{item}")
            else:
                print("shopping list is empty.")
        elif choice == "4":
            print("Exiting the Shopping List Manager.")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()


        


