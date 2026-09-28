s1 = "abc4def9ghi3"
digits = []

for char in s1:
    if char in "0123456789":
        digits.append(int(char))

total = sum(digits)
average = total / len(digits)

print("String:", s1)
print("Digits:", digits)
print("Sum:", total)
print("Average:", average)