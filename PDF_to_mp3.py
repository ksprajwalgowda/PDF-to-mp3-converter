import PyPDF2
from gtts import gTTS

def convert(file):
    	
	language = 'En'
	myobj = gTTS(text=extract_text(file), lang=language, slow=False) 
	name = file.split("\\")[-1].split(".pdf")[0]
	
	myobj.save(name+".mp3")
	


def extract_text(filename):
	
	pdfFileObj = open(filename, "rb")
	pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

	mytext = ""

	for pageNum in range(pdfReader.numPages):
		pageObj = pdfReader.getPage(pageNum)
		mytext += pageObj.extractText()

	pdfFileObj.close()

	return mytext


    	
convert("path of PDF file")
