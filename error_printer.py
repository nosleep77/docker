
def printer_error(s):
  lenLabel = 0
  a = 0

  lenLabel = len(s)
  colors = "abcdefghijklm"
  for i in s:
    if i not in colors:
      a += 1
  
  #return a

  return f"{a}/{lenLabel}"


print(printer_error("aaaxbbbbyyhwawiwjjjwwm"))

