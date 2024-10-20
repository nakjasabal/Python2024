def gugudan():
  for dan in range(2,10):
    for su in range(1,10):
      print("%d*%d=%2d" % (dan, su, su*dan), end=' ')
    print()
  print()

if __name__ == "__main__":    
  gugudan() 