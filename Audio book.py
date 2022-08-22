import pyttsx3
import pyautogui
import PyPDF2
book = open ('short story.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print(pages)
speaker = pyttsx3.init()
page = pdfReader.getPage(2)
text = page.extract_text()
speaker.say(text)
speaker.runAndWait()

