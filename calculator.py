first_value = 5
second_value = 2
operator = "*"
if first_value is None or second_value is None:
    print("Can't divide by None value")
else:
    if operator == "+":
        print(first_value + second_value)
    elif operator == "-":
        print(first_value - second_value)
    elif operator == "*":
        print(first_value * second_value)
    elif operator == "/":
        if second_value == 0:
            print("Can't divide by 0")
        else:
            print(first_value / second_value)
    else:
        print("Please select operator's: + - * /")

