phones = [
    {'make': 'Google', 'model': 216, 'color': 'Black'},
    {'make': 'Mi Max', 'model': '2', 'color': 'Gold'},
    {'make': 'Samsung', 'model': 7, 'color': 'Blue'}
]
print("Original list:")
for phone in phones:
    print(phone)

sorted_phones = sorted(
    phones,
    key=lambda x: x['color']
)
print("\nSorted list:")
for phone in sorted_phones:
    print(phone)

