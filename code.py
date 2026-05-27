while True:
    message = input("Please enter your message\n>>>\n").strip()
    if any(messages.isdigit() for messages in message):
        print("No numbers pls\npls try again >>>\n")
    else:
        table = str.maketrans(
        "abcdefghijklmnopqrstuvwxyz",
        "zyxwvutsrqponmlkjihgfedcba"
        )
        message = message.translate(table)
        print(message)
