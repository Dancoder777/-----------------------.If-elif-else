# Задание 1
sum = [2, 3, 4, 5, 6, 7, 2, 12]
print(sum[0]+sum[1]+sum[2]+sum[3]+sum[4]+sum[5]+sum[6]+sum[7])

# Задание 2
chetNum = [2, 3, 4, 5, 6, 7, 2, 12]
for num in chetNum:
    if num % 2 == 0:
        print(num)

# Задание 3
maxNumList = [3, 7, 22, 9, 5555, 12, 823]  
max_number = maxNumList[0] 
for num in maxNumList:
    if num > max_number:
        max_number = num 
print("Самое большое число:", max_number)

# Задание 4
list = [1, 5, 3, 12, 5]  
for i in range(len(list) - 1, -1, -1):
    print(list[i])


# Задание 5
for i in range(1, 11):  # От 1 до 10 включительно
    print(f"5 × {i} = {5 * i}")
