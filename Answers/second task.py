#TASK-B (Can you solve Arithmetic Expressions?)
n = int(input())
for i in range(n):
    exp = input().strip()
    eqn = exp.split()

    num1 = int(eqn[1])
    num2 = int(eqn[3])
    operation = eqn[2]

    if operation == "+" :
        ans = num1 + num2
    elif operation == "-":
        ans = num1 - num2
    elif operation == "/":
        if num2 != 0:
            ans = num1/num2
        else:
            ans = num2/num1
    elif operation == "*":
        ans = num1 * num2

    print(f"{ans:.6f}")