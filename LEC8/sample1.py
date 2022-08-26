def password_verify(x):
    while x != "Bravo" and x != "bravo":
        x = input("The password is not right. Please enter the password again ")

    print("bingo!")


password_verify(input("Please enter the password "))