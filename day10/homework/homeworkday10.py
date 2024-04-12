

HM_list = ["C++", "python", "html", "ca", "Javascript"]

print(HM_list)

print(HM_list[4])



IM_list2 = [5, "i am string", 2.5, True]

print(IM_list2[0])

print(IM_list2[1])

print(IM_list2[2])

print(IM_list2[3])


HM_list3=[]

for i in range (0,21):

    if i % 4==0 and i != 0:
        HM_list3.append(i) 

print(max(HM_list3))




HW_list4 = []

for y in range(30,51):
    if y % 21:
        HW_list4.append(y)
HW_list4.sort()
print(HW_list4[0] + HW_list4[1] + HW_list4[2])


HM_lists = []

for x in HW_list4:
    if x % 3-0:
        HM_lists.append(x)

print(HM_lists)
