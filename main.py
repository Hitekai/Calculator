operand1 = float(input("Введите первый операнд: "))
operator = input("Введите оператор (+, -, *, /, **): ")
operand2 = float(input("Введите второй операнд: "))

if operator == '+':
    result = operand1 + operand2
elif operator == '-':
    result = operand1 - operand2
elif operator == '*':
    result = operand1 * operand2
elif operator == '**':
    result = operand1 ** operand2
elif operator == '/':
    if operand2 != 0:
        result = operand1 / operand2
    else:
        result = "Ошибка: Нельзя делить на ноль!"
else:
    result = "Ошибка: Неподдерживаемый оператор!"

print(f"Результат: {result}")