#Day 10

# f_name = input("Enter the first name: ")
# l_name = input("Enter the last name: ")
# def format_name(f_name, l_name):
#   """Take a first and last name and format it to return the title case version of the name."""""
#   if f_name == "" or l_name == "":
#     return "You didn't provide valid inputs."
#   formatted_f_name = f_name.title()
#   formatted_l_name = l_name.title()
#   return f"Result: {formatted_f_name} {formatted_l_name}"
# print(format_name(f_name, l_name))


# def my_function(a):
#     if a < 40:
#         return
#         print("Terrible")
#     if a < 80:
#         return "Pass"
#     else:
#         return "Great"
# print(my_function(25))

#Calculator

# def add(n1, n2):
#   return n1 + n2
# def subtract(n1, n2):
#   return n1 - n2
# def multiply(n1, n2):
#   return n1 * n2
# def divide(n1, n2):
#   return n1 / n2
# def calculator():
#   should_continue = True
#   number1 = int(input("Enter the first number: "))
#   while should_continue:
    
#     operations = {"+" : add, "-" : subtract, "*" : multiply, "/" : divide}
#     for i in operations:
#       print(i)
#     operation_symbol = input("Pick an operation from the line above: ")
#     number2 = int(input("Enter the second number: "))
#     calculation_function = operations[operation_symbol]
#     answer = calculation_function(number1, number2)
#     print(f"{number1} {operation_symbol} {number2} = {answer}")
  
#     choice = input(f"Type 'y' to continue calculating with {answer} or type 'n' to exit: ")
#     if choice == 'y':
#       number1 = answer
#     else:
#       should_continue = False
#       print("\nThank you for using the calculator.")
#calculator()