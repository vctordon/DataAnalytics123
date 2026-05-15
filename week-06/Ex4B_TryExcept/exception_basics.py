
try:
    num = int("hello")  # cannot convert string to number
except ValueError:
    print("ValueError: Cannot convert string to integer")
else:
    print(num)
finally:
    print("Let's try another one...\n")



try:
    eval("if True print('hello')")  # invalid syntax
except SyntaxError:
    print("SyntaxError: Invalid syntax detected")
else:
    print("Code ran successfully")
finally:
    print("Let's try another one...\n")

