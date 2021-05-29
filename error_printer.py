
def printer_error(s):
  lenLabel = 0
  a = 0

  lenLabel = len(s)
  colors = "abcdefghijklm"
  for i in s:
    if i not in colors:
      a += 1
  
  return f"{a}/{lenLabel}"

print(printer_error("aaaxbbbbyyhwawiwjjjwwm"))

def printer_error(s):
    return "{}/{}".format(len([x for x in s if x not in "abcdefghijklm"]), len(s))