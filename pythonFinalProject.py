import tkinter
import tkinter.messagebox
import requests
from bs4 import BeautifulSoup
import pandas as pd
import datetime
import matplotlib.pyplot as plt

class myGUI:
    def __init__(self):
        self.mainWin=tkinter.Tk()
        self.mylabel=tkinter.Label(self.mainWin,text="Input a stock id(EX:鴻海2354 ==> INPUT: 2354.TW) you wanna plot & search here:")
        self.mylabel.pack()
        self.stockEntry=tkinter.Entry(self.mainWin,width=20)
        self.stockEntry.pack()
        self.mylabel2=tkinter.Label(self.mainWin,text="Input a file name you wanna save for the csv file:")
        self.mylabel2.pack()
        self.nameEntry=tkinter.Entry(self.mainWin,width=20)
        self.nameEntry.pack()
        self.mylabel3=tkinter.Label(self.mainWin,text="Input a date/month(EX:2000-01-04 or 2000-01) you wanna print info from the stock:")
        self.mylabel3.pack()
        self.dateEntry=tkinter.Entry(self.mainWin,width=20)
        self.dateEntry.pack()
        self.mybutton=tkinter.Button(self.mainWin,text="Click",command=self.clicked)
        self.mybutton.pack()
        self.value=tkinter.StringVar()
        self.value.set("Your website is:  ,and the the file name is:  ,and the time you search is: ")
        self.output=tkinter.Label(self.mainWin,textvariable=self.value)
        self.output.pack()

        tkinter.mainloop()
    def clicked(self):
        stock=self.stockEntry.get()
        name=self.nameEntry.get()
        date=self.dateEntry.get()
        #below codes are from https://www.finlab.tw/ 
        now = int(datetime.datetime.now().timestamp())+86400
        url = "https://query1.finance.yahoo.com/v7/finance/download/" + stock + "?period1=0&period2=" + str(now) + "&interval=1d&events=history&crumb=hP2rOschxO0"
        #end
        page = requests.post(url)
        #below codes are from https://www.finlab.tw/ 
        with open((name+'.csv'), 'w') as f:
            f.writelines(page.text)
        #end
        self.value.set("Your website is: '" + url + "', \n and the file name is " + name + '.csv, \n and the time you search is: ' + date)
        #below codes are from https://www.finlab.tw/ 
        df = pd.read_csv((name+'.csv'), index_col='Date', parse_dates=['Date'])
        #end
        # below code is from https://leemeng.tw/practical-pandas-tutorial-for-aspiring-data-scientists.html
        print((df.filter(regex=date, axis=0)))
        #end
        plt.show(df.Close.plot())

def main():
    mygui=myGUI()

main()
