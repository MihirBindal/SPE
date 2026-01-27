import sys

# Check if we got enough arguments
if len(sys.argv) < 4:
    print("Error: Please provide Num1, Num2, and Operation")
    sys.exit(1)

num1 = float(sys.argv[1])
num2 = float(sys.argv[2])
operation = sys.argv[3]

print(f"Inputs: {num1} and {num2}")

result = 0
op_name = "Unknown"

if operation == '1':
    result = num1 + num2
    op_name = "Addition"
elif operation == '2':
    result = num1 - num2
    op_name = "Subtraction"
elif operation == '3':
    result = num1 * num2
    op_name = "Multiplication"
elif operation == '4':
    if num2 == 0:
        print("Error: Cannot divide by Zero!")
        sys.exit(1)
    result = num1 / num2
    op_name = "Division"
else:
    print(f"Invalid Operation Code: {operation}")
    sys.exit(1)

print(f"Operation: {op_name}")
print(f"Result: {result}")
