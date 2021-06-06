splitMe =input( "give me a sentance and ill reverse it: \n")
arr = splitMe.split(" ")
reverser = arr[::-1]
for i in range( 0, len(reverser)):
  print(reverser[i], end= ' ')
