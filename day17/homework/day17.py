def manipulate_string(string):
    manipulated_string = ""
    manipulated_string += string.lower() + "\n"
    manipulated_string += string.upper() + "\n"
    manipulated_string += string.capitalize() + "\n"
    substring = "day"
    index = string.find(substring)
    if index != -1:
        manipulated_string += f"The substring '{substring}' found at index {index}."
    else:
        manipulated_string += f"The substring '{substring}' not found."

    return manipulated_string

# Example usage
input_string = "today i learn "
result = manipulate_string(input_string)
print(result)



# def modify_and_join(lst):
#     lst.append('')
#     print("change name:")
#     index = int(input())
#     print("enter new name:")
#     new_string = input()

#     lst[index] = new_string

#     result = ' '.join(lst)
#     return result

# my_list = ["name1", "name2", "name3"]

# print(modify_and_join(my_list))