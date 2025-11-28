print("========= ATM MACHINE =========\n\n")

atm_user = "lucifer"
atm_pin = 121212
balance = 349849343

while True:
    username = input("Enter Username: ").lower().strip()
    password = int(input("Enter ATM Pin: "))

    if username == atm_user and password == atm_pin:
        print("Login Success!\n")

        while True:
            print("1. Check Balance")
            print("2. Deposit Money")
            print("3. Withdraw Money")
            print("4. Exit")

            choice = input("Enter your choice: ")
            if choice == "1":
                print(f"Your Balance is: {balance}")
            elif choice == "2":
                amount = int(input("Enter Deposit Balance: "))
                balance += amount
                print(f"Your Balance is: {balance}")
            elif choice == "3":
                wd_amount = int(input("Enter withdraw Amount: "))
                if balance >= wd_amount:
                    balance -= wd_amount
                    print(f"Your Balance: {balance}")
                else:
                    print("Insufficient Balance")
            elif choice == "4":
                print("Thank You! Using ATM!")
                break
            else:
                print("Invalid Choice! Try Again")
        break

    else:
        print("Your username and password is incorrect!Try Again!")
        continue
