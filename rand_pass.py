import random
import string
import tkinter as tk

#root = tk.Tk()
#root.geometry("400x500")

num = [0,1,2,3,4,5,6,7,8,9]
symbals = ["!","@","#","$","%","^","&","*"]
upper_str = list(string.ascii_uppercase)
lower_str = list(string.ascii_lowercase)
combine = num + symbals + upper_str + lower_str
n = random.choices(combine, k=23)


#combine = str(num) + str(symbals) + str(upper_str) + str(lower_str)
print("**** Random Password Generator ****")
str = ""
print(n)

#n = int(input("Enter the Length of Password  :-"))
#n = random.choices(combine, k = n)
#print("".join(n))

#root.mainloop()