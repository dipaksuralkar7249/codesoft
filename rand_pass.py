import random
import string
import tkinter

root = tk.Tk()

def generate_random_password(length):
        # Define character sets
    num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    symbols = ["!", "@", "#", "$", "%", "^", "&", "*"]
    upper_str = list(string.ascii_uppercase)
    lower_str = list(string.ascii_lowercase)

        # Convert num to strings
    num = [str(x) for x in num]

        # Combine character sets
    combine = num + symbols + upper_str + lower_str

        # Generate random password
    password = ''.join(random.choices(combine, k=length))
    return password
    # Prompt user for password length
length = int(input("Enter the length of the password: "))

    # Generate random password
password = generate_random_password(length)

    # Print the generated password
print("Random Password:", password)



