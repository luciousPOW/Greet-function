def greet(name):
    print(f"Hello, {name}! Welcome to the world of Python.")
    
user_name = input("Enter name: ").strip().capitalize()
greet(user_name)
