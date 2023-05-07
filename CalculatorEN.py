###@alierenkose

beautiful = "-------------------------------------------------"

while True:
  print("Calculator(c) , Exponentiation(e) , Prime(p) , Diagonal(d) , Average(a) , Root Calculator(r)")
  calculation_type = input("Which one of these do you want to use: ")
  calculation_type = calculation_type.lower()

  if calculation_type not in ["c", "e", "p", "d", "a", "r"]:
    print("You have chosen an invalid operation type!")
    exit()

  if calculation_type == "c":
    operation = input("Which operation do you want to perform? (+, -, *, /): ")

    if operation not in ["+", "-", "*", "/"]:
      print("You have chosen an invalid operation type!")
      exit()

    num_of_nums = int(input("How many numbers do you want to include in the operation? "))

    numbers = []
    for i in range(num_of_nums):
      print(beautiful)
      num = float(input(f"\nEnter {i+1}. number: "))
      numbers.append(num)

    if operation == "+":
      result = sum(numbers)
    elif operation == "-":
      result = numbers[0] - sum(numbers[1:])
    elif operation == "*":
      result = 1
      for num in numbers:
        result *= num
    else:
      result = numbers[0]
      for num in numbers[1:]:
        result /= num

    print(beautiful)
    print(f"Result of {operation} operation of {num_of_nums} numbers: ", result)

  elif calculation_type == "e":
    base_num = float(input("Enter the number: "))
    print(beautiful)
    exponent = int(input("Enter the exponent: "))
    print(beautiful)
    result = base_num ** exponent
    print(f"{base_num} to the power of {exponent} is {result}")

  elif calculation_type == "p":
    num = int(input("Enter the number: "))
    print(beautiful)

    if num > 1:
      for i in range(2,num):
        if (num % i) == 0:
          print(f"{num} is not a prime number.")
          break
      else:
        print(f"{num} is a prime number.")
    else:
      print(f"{num} is not a prime number.")

  elif calculation_type == "d":
    num_of_sides = int(input("How many sides does the object have? "))
    print(beautiful)
    diagonal_result = num_of_sides * (num_of_sides - 3) / 2
    print(diagonal_result)

  elif calculation_type == "a":
    num_of_inputs = int(input("How many numbers will you enter? "))
    total = 0

    for i in range(num_of_inputs):
      num = float(input(f"Enter the {i + 1}. number: "))
      total += num

    average = total / num_of_inputs
    print(f"The arithmetic average of the numbers entered: {average}")

  elif calculation_type == "r":
    num = float(input("Enter the number you want to calculate the root of: "))
    root_degree = int(input("Enter the degree of the root (for example, 2 for square root, 3 for cube root): "))
    print(beautiful)
    result = num ** (1 / root_degree)
    print(f"{root_degree}. degree root of the entered number: {result}")

  print("")
  print("RESTARTING.....")
  print("")
  
  
  ###@alierenkose
