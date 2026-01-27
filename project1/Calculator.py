
def get_integer_input(prompt: str) -> float:
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")

def get_operation_input(prompt: str) -> str:
    while True:
        op = input(prompt).strip()
        if op in ['+', '-', '*', '/']:
            return op
        else:
            print("Invalid operation. Please enter one of +, -, *, /.")

def perform_calculation(a: float, b: float, op: str) -> float:
    if op == '+':
        result = a + b
    elif op == '-':
        result = a - b
    elif op == '*':         
        result = a * b      
    elif op == '/':
        if b != 0:
            result = a / b
        else:
            raise ZeroDivisionError("Division by zero is not allowed.") 
    else:
        raise ValueError(f"Unknown operator: {op}")  
    
    return round(result, 2)

def perform_calculation2(a: float, b: float, op: str) -> float:
    operations = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x / y if y != 0 else (_ for _ in ()).throw(ZeroDivisionError("Division by zero is not allowed."))     
    }
    return round(operations[op](a, b), 2)

def main():
    while True:
        a = get_integer_input("Enter first number: ")
        b = get_integer_input("Enter second number: ")
        op = get_operation_input("Enter operation (+, -, *, /): ")
        try:
            result = perform_calculation2(a, b, op)
        except (ValueError, ZeroDivisionError) as e:
            print("Error:", e)
            continue
        print(f"{a} {op} {b} = {result}")
        c = input("Do you want to perform another calculation? (y/n): ").strip().lower()
        if c != 'y':
            break

if __name__ == "__main__":
    main()