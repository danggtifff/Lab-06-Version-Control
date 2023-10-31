#This is my main.py

def menu():
    print("Menu"
          "-------------"
          "1. Encode"
          "2. Decode"
          "3. Quit\n")

if __name__ == '__main__':
    option = -1
    while True:
        menu()
        option = input("Please enter an option: ")
        if option == 1:
            password = input("Please enter your password to encode: ")
            password = encode.encode(password)
            print("Your password has been encoded and stored!\n")
        elif option == 2:
            print(f"The encoded password is {password}, and the original password is {decode.decode(password)}")