
def leftSide(x):
  genNum = 1
  for a in range(x):	## 0,1,2,3
    genNum = (2 * a) + genNum	## genNum = 1,3,7

  return genNum

def rightSide(x):
  genNum = 1
  for a in range(2, x+1):	## 0,1,2,3
    genNum = (2 * (a)) + genNum	## genNum = 1,3,7

  return genNum

def row_sum_odd_numbers(row):

  b = 0
  for a in range(leftSide(row), rightSide(row)+1):
    if a % 2 != 0:
      b += a

  return b

#print(f"left side is {leftSide(4)}")
#print(f"right side is {rightSide(4)}")
print(row_sum_odd_numbers(4))


