import a
while True:
    print("\n1. Sign Up\n2. Log In\n3. Display Users\n4. Delete User\n5. Exit")
    
    choice = int(input("Enter your choice: "))

    if choice == 1:
        a.sign_up()
    elif choice == 2:
        a.log_in()
    elif choice == 3:
        a.display_users()
    elif choice == 4:
        a.delete_user()
    elif choice == 5:
        print("Exiting...")
        break
    else:
        print("Invalid choice! Please try again")