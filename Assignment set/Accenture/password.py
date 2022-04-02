def upperCase(st):
  for ele in st:
    if ele.isupper():
      return True
  return False 

def containsNumber(st):
  for i in range(0,10):
    j = str(i)
    if j in st:
      return True
  return False

def length(st):
  if len(str)>=3:
    return True
  return False

def space(st):
  for ele in st:
    if ele == ' ' or ele == '/':
      return True
  return False
  
def checkPassword(st):
  pass

st = str(input())

print(containsNumber(st))