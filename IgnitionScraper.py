from bs4 import BeautifulSoup
from html.parser import HTMLParser
from tkinter import *
from tkinter import filedialog
from GetQuestions import GetQuestions
from tkintertable import TableCanvas, TableModel
from Content import DataTracking


window = Tk()
window.title("Ignition Scraper")
table = ""

tframe = Frame(window)
tframe.pack(fill=BOTH, expand=1)

#Opens FileDialog to Select new Webpage File
def LoadWebPage():

    HtmlFile = filedialog.askopenfilename()
    File = open(HtmlFile, encoding='utf-8')
    soup = BeautifulSoup(File.read(), features="html.parser")
    Data = GetQuestions.GetAnswers(soup)
  
    model = TableModel()
    table = TableCanvas(tframe, data=Data)
    table.thefont = ('Arial', 10)
    table.show()


def ClearTable():

    DataTracking.Question = []
    DataTracking.Answers = []
    DataTracking.Correct = []

    Data = {}
    model = TableModel()
    table = TableCanvas(tframe, data=Data)
    table.show()

b = Button(window, text="Add", command=LoadWebPage,width=20)
b.pack()

Reset = Button(window, text="Clear Table", command=ClearTable, width=20)
Reset.pack()

window.mainloop()
