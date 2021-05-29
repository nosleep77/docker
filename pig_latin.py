
def pig_it(s):
  s = s.split()
  pigSent = ""
  word = ""

  for b in s:
    if b.isalpha():
      word = b[1:] + b[0] + "ay"
      pigSent = pigSent + " " + word
    else:
      pigSent = pigSent + " " + b

  return pigSent

print(pig_it('Hello world !'))