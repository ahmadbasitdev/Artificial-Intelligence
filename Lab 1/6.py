"""Lab 1 - Task 6: Data types and type casting."""

values = [
    1452,
    -4587,
    1.03,
    0.34,
    2.12e-10,
    complex(1, 2),
    True,
]

for value in values:
    print(f"{value!r}: {type(value).__name__}")

integer_text = "42"
print("Converted text:", int(integer_text))
