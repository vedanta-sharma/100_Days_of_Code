#Day 8

# def greet():
#   print("Hello!")
#   print("How are you?")
#   print("Goodbye")
# greet()

# #Function that allows for input
# def greet_with_name(name):
#   print(f"Hello {name}!")
#   print(f"How are you {name}?")
#   print(f"Goodbye {name}")
# greet_with_name("Max")

# #Functions with more than 1 input
# def greet_with(name, location):
#   print(f"Hello {name}!")
#   print(f"What is it like in {location}?")
# greet_with("Max", "London")

# #Functions with keyword arguments
# def greet_with(name, location):
#   print(f"Hello {name}!")
#   print(f"What is it like in {location}?")
# greet_with(location = "London", name = "Tom")

#Caeasar Cipher
# import art
# print(art.logo)
# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


# def caeser(cipher_direction, input_text, shift_size):
#   cipher_text = ""
#   if cipher_direction == "decode":
#     shift_size *= -1
#   for i in input_text:
#     if i in alphabet:
#       current_position = alphabet.index(i)
#       new_position = current_position + shift_size
#       new_position %= len(alphabet)
#       cipher_letter = alphabet[new_position]
#       cipher_text += cipher_letter
#     else:
#       cipher_text += i
#   print(f"The {cipher_direction}d text is: {cipher_text}")

# should_continue = True
# while should_continue:
#   direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
#   text = input("Type your message:\n").lower()
#   shift = int(input("Type the shift number:\n"))
#   caeser(direction, text, shift)
#   restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
#   if restart == "no":
#     should_continue = False
#     print("Goodbye")