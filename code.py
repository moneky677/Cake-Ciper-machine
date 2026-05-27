print("Welcome to the Cake Cipher!!!")
while True:
    choice = input("\nWould you like to cipher or decipher?\n\nd/c\n").lower().strip()
    while choice not in ['d','c']:
        print("Not an option, please try again")
        choice = input("Would you like to cipher or decipher?\nd/c\n").lower().strip()
    message = input("Please enter your message\n>>>\n").strip()
    if choice == 'c':
        table = str.maketrans(
                "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890`~!@#$%^&*()-_=+[{]}\|;:,<.>/?",
                "VbX4m3JFTe_K8&2|v/SQG:.n@{ID16Eaiy*9`\[,NCBzd$^r#>(f+)}A%thO5ZMY]jPHuwRos?xklqc;<LW~0p!=7g-U"
        )
    else:
        table = str.maketrans(
            "VbX4m3JFTe_K8&2|v/SQG:.n@{ID16Eaiy*9`\[,NCBzd$^r#>(f+)}A%thO5ZMY]jPHuwRos?xklqc;<LW~0p!=7g-U",
            "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890`~!@#$%^&*()-_=+[{]}\|;:,<.>/?"
        )
    print("\n\n"+message.translate(table))
