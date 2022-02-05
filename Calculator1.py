# Program make a simple calculator
while True:
    operation = input('write the operation here: ') # writes the operation here , example 10 x 2 ÷ 2
    if 'x' in operation: # change all x for *
        operation =  operation.replace('x','*')
    if '÷' in operation: # change all  ÷  for /
        operation =operation.replace('÷','/')
    print(eval(operation)) #print the operation 
    next_calculation = input("Let's do next calculation? (yes/no): ")
    if next_calculation == "no":
        break

    else:
        print("Invalid Input")
