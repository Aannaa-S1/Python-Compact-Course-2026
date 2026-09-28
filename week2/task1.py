numbers = [(2,5),(1,2),(4,4),(2,3),(2,1)]
print(numbers)

for i in range (len(numbers)):
    for j in range (len(numbers)-1):
        if numbers[j][-1] > numbers[j+1][-1]:
            temp = numbers[j]
            numbers[j] = numbers[j+1]
            numbers[j+1] = temp
print(numbers)
