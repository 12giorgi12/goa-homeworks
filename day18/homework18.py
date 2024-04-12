# def manipulate_string(string):
#     username = string.lower() if string else "user"
#     words = string.split()

#     manipulated_string = ""
#     manipulated_string += " ".join(word.lower() for word in words) + "\n"
#     manipulated_string += " ".join(word.upper() for word in words) + "\n"
#     manipulated_string += " ".join(word.capitalize() for word in words) + "\n"
#     substring = "დღე"
#     index = string.find(substring)
#     if index != -1:
#         manipulated_string += f"The substring '{substring}' found at index {index}."
#     else:
#         manipulated_string += f"The substring '{substring}' not found."

#     return manipulated_string
# username = input("Please enter your name: ")
# result = manipulate_string(username)
# print(result)




# def manipulate_string(string):
#     new_string = ""
#     for char in string:
#         if char.islower():
#             new_string += char.upper()
#         elif char.isupper():
#             new_string += char.lower() 
#         else:
#             new_string += char
#     username = new_string if new_string else "user"
#     words = username.split()

#     manipulated_string = ""
#     manipulated_string += " ".join(word.lower() for word in words) + "\n"
#     manipulated_string += " ".join(word.upper() for word in words) + "\n"
#     manipulated_string += " ".join(word.capitalize() for word in words) + "\n"
#     substring = "day"
#     index = username.find(substring)
#     if index != -1:
#         manipulated_string += f"The substring '{substring}' found at index {index}.\n"
#     else:
#         manipulated_string += f"The substring '{substring}' not found.\n"
#     word_count = len(words)
#     manipulated_string += f"The word has been entered {word_count} times.\n"

#     return manipulated_string

# username = input("Please enter your word: ")
# result = manipulate_string(username)
# print(result)



# def name(string):
#     new_string = ""
#     for index, char in enumerate(string):
#         if index % 2 == 0:  
#             new_string += char.upper()  
#         else:
#             new_string += char.lower()  
#     return new_string
# username = input("Please enter your name: ")
# result = name(username)
# print("name:", result)



def manipulate_string(string):
    if len(string) > 5:
        manipulated_string = string.upper()
    else:
        manipulated_string = string.lower()

    return manipulated_string
username = input("Please enter your name: ")
result = manipulate_string(username)
print("name:", result)
