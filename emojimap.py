import string

class EmojiMap():

  global __emojis
  global __get_emoji

  __emojis = {}

  def __init__(self):
    with open('data/emoji.data', 'r') as f:
      for l in f:
        e = l.strip().split("\t")
        __emojis[e[0]] = e[1]
    with open('emojis.txt', 'r') as f:
      for l in f:
        e = l.strip()
        __emojis[e[1:-1]] = e

  #gets the emoji or returns the input
  def __get_emoji(t):
    if t.lower() in __emojis:
        return __emojis[t.lower()].replace(" ", "")
    else:
        return t

  #emojifies
  def apply(self, t):
    result = ""
    curr = ""
    
    for l in t:
        if l.isspace() or l in string.punctuation:
            #space or punctuation ... so check for emojis
            result += __get_emoji(curr)
            result += l
            curr = ""
        else:
            curr += l
            
    result += __get_emoji(curr)
    
    return result

