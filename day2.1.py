words =['prince', 'princess', 'king', 'queen']

for w in words[:]:
    if len(w)>6:
          words.insert(0, w)
          print(words)
