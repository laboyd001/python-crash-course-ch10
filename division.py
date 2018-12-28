#handling the zerodivision exception

#this gives traceback zerodivision message:
# print(5/0)

#use try-except block:

# try:
#     print(5/0)
# except ZeroDivisionError:
#     print("You can't divide by zero!")

#Using exceptions to prevent crashes:

print("Give me 2 numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by zero!")
    else:
        print(answer)