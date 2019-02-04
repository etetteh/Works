"""How about scanning documents to raise alerts, when you encounter a curse word. Well, this is
   exactly what this functions do.
"""

import urllib.request

# change url to websites that prevent curse words    
def curse_word(text):
    url_content = urllib.request.urlopen("https://www.purgomalum.com/service/containsprofanity?text="+text)
    url_output = url_content.read()
    print(url_output)
#     url_content.close()
    
def read_text():
    content = open("Drake_Redemption_Lyrics.txt")
    output = content.read()
    print(output)
#     content.close()
    curse_word(output)


read_text()

