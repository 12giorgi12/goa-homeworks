# def sum_even_indices(lst):
#     total = 0
    
#     for i in range(1, len(lst), 2):
#         total += lst[i]
    
#     return total

# input_data = [1, 2, 3, 4, 5]
# result = sum_even_indices(input_data)
# print("Output data (result):", result)



# def sum_odd_and_even_separately(lst):
#     # Initialize variables to store the sum of odd and even numbers
#     odd_sum = 0
#     even_sum = 0
    
#     # Iterate through the list
#     for num in lst:
#         if num % 2 == 0:
#             even_sum += num
#         else:
#             odd_sum += num
    
#     # Create a list containing the sums
#     result = [even_sum, odd_sum]
    
#     return result

# # Example usage:
# input_data = [1, 2, 3, 4, 5]
# output_data = sum_odd_and_even_separately(input_data)
# print("Output data:", output_data)



def count_elements(lst):
    return len(lst)

# მაგალითის გამოყენება:
input_data = [1, 2, 3, 4, 5]
result = count_elements(input_data)
print(result)



# def my_replace(string, old, new):
#     return string.replace(old, new)

# text = "Hello, World!"
# result = my_replace(text, "World", "Universe")
# print("Result:", result)