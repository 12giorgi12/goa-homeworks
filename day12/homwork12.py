person_info = []
name = input("Please enter your name: ")
lastname = input("Please enter your lastname: ")
age = int(input("Please enter your age: "))
address = input("Please enter your addres: ")

person_info.append(name)
person_info.append(lastname)
person_info.append(age)
person_info.append(address)


print(person_info)
print(person_info[0:2])
print(person_info[1:3])
print(person_info[0:3])
print(person_info[1::])

num=int(input("pleas enter number"))
negative_numbers = []

for i in range(num,0):
    print(i)
 
 
name="giorgi wakadze"
print(name[0:6])
print(name[7::])


movies=["bad boys 1", "bad boys 2","bad boys 3""bad boys 4","supernatural"]
print(movies[0:2])