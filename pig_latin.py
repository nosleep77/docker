
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

  return pigSent.lstrip()

print(pig_it('Hello world !'))

## better version
def pig_it(text):
    lst = text.split()
    return ' '.join( [word[1:] + word[:1] + 'ay' if word.isalpha() else word for word in lst])
    