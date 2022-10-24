try:
  x = input("Please input your grade: ")
  if type(x) == int:
    if x >= 70:
      print("A")
    elif x >= 60:
      print("B")
    elif x >= 50:
      print("C")
    elif x >= 45:
      print("D")
    elif x >= 40:
      print("E")
    else:
      print("Failed")
except:
  print("Our program only accepts integers")
print("I will execute either way")

  

      