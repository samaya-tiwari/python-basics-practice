
# Exercise 5: File Writer


user_input = input("Enter your name: ")
with open('greeting.txt', 'w') as file:
    file.write(f"Hello {user_input}!")
    file.close()