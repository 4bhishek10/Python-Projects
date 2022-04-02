def upperCase(st):
  for ele in st:
    if ele.isupper():
        #print("true")
        return True
        break
  return False 

def containsNumber(st):
  for i in range(0,10):
    j = str(i)
    if j in st:
        #print("true")
        return True
        break
  return False

def length(st):
  if len(st)>=3:
      #print("true")
      return True
  return False

def space(st):
  for ele in st:
    if ele == ' ' or ele == '/':
      return True
  #print("true")
  return False
  
def checkPassword(st):
  if length(st) == True and space(st) == False and containsNumber(st) == True and upperCase(st) == True:
      return 1
  else:
      return 0

st = str(input("please enter the password: "))

print(checkPassword(st))