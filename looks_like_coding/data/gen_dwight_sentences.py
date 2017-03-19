import re


dm = r'Dwight Schrute: '
dwight_quotes = []
with open("dwight_dialogue.txt", "r") as rf:
    sentences = rf.readlines() 
    for sentence in sentences:
        m = re.match(dm, sentence)
        if m:
            dwight_quotes.append(sentence[m.end():])

assert len(dwight_quotes) == 526  # Total 

with open("dwight_quotes.txt", "w") as wf:
    for quote in dwight_quotes:
        wf.write(quote)
