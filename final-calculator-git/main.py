
while True:
  print("Select a Method")
  print("A = Method #1")
  print("B = Method #2")
  
  selection = input()
  
  if selection == "A":
      num1 = int(input("1st Number: "))
      operator = input("(+  -  *  / ): ")
      num2 = int(input("2nd Number: "))
  
      if operator == "+":
          print("ANSWER: ", num1 + num2)
          
      elif operator == "-":
          print("ANSWER: ", num1 - num2)
          
      elif operator == "*":
          print("ANSWER: ", num1 * num2)
          
      elif operator == "/":
          print("ANSWER: ", num1 / num2)
          
      else:
          print("INVALID INPUT (Make sure you put the correct input)")
  
  if selection == "a":
      num1 = int(input("1st Number: "))
      operator = input("(+  -  *  / ): ")
      num2 = int(input("2nd Number: "))
  
      if operator == "+":
          print("ANSWER: ", num1 + num2)
          
      elif operator == "-":
          print("ANSWER: ", num1 - num2)
          
      elif operator == "*":
          print("ANSWER: ", num1 * num2)
          
      elif operator == "/":
          print("ANSWER: ", num1 / num2)
          
      else:
          print("INVALID INPUT (Make sure you put the correct input)")
  
  elif selection == "B":
      print("Select")
      print("A. ADDITION")
      print("B. SUBTRACTION")
      print("C. MULTIPLICATION")
      print("D. DIVISION")
  
      answer = input()
  
      if answer == "A" or answer == "a":
          num1 = int(input("First Number: "))
          num2 = int(input("Second Number: "))
          print("Your SUM is: ", num1 + num2)
  
      elif answer == "B" or answer == "b":
          num3 = int(input("First Number: "))
          num4 = int(input("Second Number: "))
          print("Your DIFFERENCE is: ", num3 - num4)
  
      elif answer == "C" or answer == "c":
          num5 = int(input("First Number: "))
          num6 = int(input("Second Number: "))
          print("Your PRODUCT is: ", num5 * num6)
  
      elif answer == "D" or answer == "d":
          num7 = int(input("First Number: "))
          num8 = int(input("Second Number: "))
          print("Your QUOTIENT is: ", num7 / num8)
  
      else:
          print("Choose A, B, C, or D")
    
  elif selection == "b":
      print("Select")
      print("A. ADDITION")
      print("B. SUBTRACTION")
      print("C. MULTIPLICATION")
      print("D. DIVISION")
  
      answer = input()
  
      if answer == "A" or answer == "a":
          num1 = int(input("First Number: "))
          num2 = int(input("Second Number: "))
          print("Your SUM is: ", num1 + num2)
  
      elif answer == "B" or answer == "b":
          num3 = int(input("First Number: "))
          num4 = int(input("Second Number: "))
          print("Your DIFFERENCE is: ", num3 - num4)
  
      elif answer == "C" or answer == "c":
          num5 = int(input("First Number: "))
          num6 = int(input("Second Number: "))
          print("Your PRODUCT is: ", num5 * num6)
  
      elif answer == "D" or answer == "d":
          num7 = int(input("First Number: "))
          num8 = int(input("Second Number: "))
          print("Your QUOTIENT is: ", num7 / num8)
  
      else:
          print("Choose A, B, C, or D")
  
  else:
    print("**Choose A or B**")

  
  print("Do you still wish to continue? Y/N")
  
  exit = input()
  
  if exit == "N":
    print("Exiting program...")
    break

  elif exit == "n":
    print("Exiting program...")
    break
  
  elif exit == "Y":
    continue
  
  elif exit == "y":
    continue
  
  else:
    print("Select Y or N")