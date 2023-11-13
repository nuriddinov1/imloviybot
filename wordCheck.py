"""
This code written by ->> nuriddinov_
@imlobot
$nuriddinov_
"""
from uzwords import words
from difflib import get_close_matches

def checkWord(word,words=words):
    word=word.lower()
    matches=set(get_close_matches(word,words))
    avaiable=False
    if word in matches:
        avaiable = True
        matches = word
    elif "ҳ" in word:
        word=word.replace("ҳ","x")
        matches.update(get_close_matches(word,words))
    elif "х" in word:
        word=word.replace("x","ҳ")
        matches.update(get_close_matches(word,words))
    elif word in matches:
        avaiable=True
        matches=word


    return {'aviable':avaiable,'matches':matches}
def reposted(word):
    matches=list(checkWord(word)["matches"])
    text="".join(matches)
    if word==text:
        return True
    return False