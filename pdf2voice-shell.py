#from tkinter import Tk
#from tkinter.filedialog import askopenfilename
import sys
import pdftotext
from gtts import gTTS

#Tk().withdraw()
#filelocation= askopenfilename()
file = sys.argv[1]

with open(file, "rb") as f:
    pdf = pdftotext.PDF(f)

string_of_text = ''
for text in pdf:
    string_of_text += text

final_file = gTTS(text = string_of_text, lang='en')
final_file.save(file + ".mp3")
