# pip install reportlab pandas

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
import string
import math
import datetime
import pandas as pd
import gc
# c = canvas.Canvas("test.pdf", pagesize=A4)

# Read the Excel file
datum = str(datetime.datetime.now())[:10].split('-')[::-1]
datum = ".".join(datum)


import os

here = os.path.dirname(os.path.abspath(__file__))

filename = os.path.join(here, 'data.xlsx')


print(filename)

def writeText(x, y, textString, c:canvas, schriftGroesse = 10, color="black", abstand = 1.3):
    c.setFontSize(schriftGroesse)
    if color == "white":
        c.setFillColorRGB(1,1,1)
    d = " "
    textString = textString.split(";")
    for i in textString:
        c.drawString(x,y,i)
        y = y - schriftGroesse*abstand
    c.setFillColorRGB(0,0,0)


def berichtheft(z):
    if z[-1] == 'no':
        filenam = os.path.join(here,f"generierteBerichte\\Bericht_{z[0]}-{z[2]}_KW{z[1]}.pdf")
        c = canvas.Canvas(filenam, pagesize=A4)
        x,y = A4
        #Image 
        filenam = os.path.join(here,"empty.jpg")
        c.drawImage(filenam, x*0.05,y*0.05,width=x*0.9,height=y*0.9)
        #Nachweis Nummer und KW + Jahr
        writeText(x*0.74, y*0.936,f"{z[0]};{z[1]}/{z[2]}",c, color="white")
        #Lfd. Nr.1 Betriebliche Tätigkeit
        writeText(x*0.88, y*0.85,f"{z[4]}",c)
        #Lfd. Nr.1 Themen der Woche
        writeText(x*0.88, y*0.55,f"{z[6]}",c)
        #Betriebliche Tätigkeit
        writeText(x*0.1, y*0.85,f"{z[3]}",c, schriftGroesse=15)
        #Themen der Woche
        writeText(x*0.1, y*0.55,f"{z[5]}",c, schriftGroesse=15)
        #Berufsschule
        writeText(x*0.1, y*0.28,f"{z[7]}",c, schriftGroesse=15)
        #Aktuelles datum
        writeText(x*0.15, y*0.13,f"{datum}",c)
        writeText(x*0.6, y*0.13,f"{datum}",c)
        writeText(x*0.30, y*0.13,f"{datum}",c)
        writeText(x*0.10, y*0.13,f"{datum}",c)
        #---------------------für empty
        writeText(x*0.1, y*0.936,f"Name;{subFach}",c, color="white")
        writeText(x*0.3, y*0.936,f"{name};{fach}",c, color="white")
        writeText(x*0.5, y*0.936,f"Ausbildungsnachweis Nr.;KW und Jahr",c, color="white")
        writeText(x*0.1, y*0.9,f"Betriebliche Tätigkeit",c)
        writeText(x*0.1, y*0.89,f"(Praktisches Arbeiten, Ausführen von Arbeitsanweisungen)",c,schriftGroesse=7)
        writeText(x*0.872, y*0.895,f"Lfd. Nr.\u00B9",c)
        writeText(x*0.872, y*0.6,f"Lfd. Nr.\u00B9",c)
        writeText(x*0.1, y*0.602,f"Themen der Woche",c)
        writeText(x*0.1, y*0.592,f"(Unterweisungen, Lehrgespräche, betrieblicher Unterricht, Projekte)",c,schriftGroesse=7)
        writeText(x*0.1, y*0.325,f"Berufsschule",c)
        writeText(x*0.1, y*0.315,f"(Themen und Schwerpunkte des Unterrichts)",c,schriftGroesse=7)
        writeText(x*0.09, y*0.13,f"Datum:",c)
        writeText(x*0.32, y*0.13,f"Datum:",c)
        writeText(x*0.545, y*0.13,f"Datum:",c)
        writeText(x*0.73, y*0.13,f"Datum:",c)
        writeText(x*0.1, y*0.08,f"Unterschrift Auszubildende/r",c,schriftGroesse=7)
        writeText(x*0.31, y*0.08,f"Unterschrift Ausbildungsbeauftragte/r",c,schriftGroesse=7)
        writeText(x*0.55, y*0.08,f"Unterschrift Ausbilder/in",c,schriftGroesse=7)
        writeText(x*0.74, y*0.08,f"Unterschrift gesetzliche/r Vertreter/in",c,schriftGroesse=7)
        writeText(x*0.07, y*0.06,f"\u00B9 Zuordnung zu der Laufenden Nummer (Unterpunkte) des Ausbildungsrahmenplanes oder des betrieblichen Ausbildungsplanes",c,schriftGroesse=7)

        c.save()
        
    return


# df = pd.read_excel('data.xlsx')


      # 0    1    2      3                  4               5             6             7      8
# test = [77, 11, 2025, 'Praxiswoche CJD', '3.1;3.2;4.2', 'Unnamed: 5', 'Unnamed: 6', 'Ferien', 'no']

# print("x\u00b2")

# tabelle = list(pd.read_excel('data.xlsx', skiprows=0))
tabelle = list(pd.read_excel(filename, skiprows=0))
name = tabelle[3]
fach = tabelle[5]
subFach = tabelle[7]

# tabelle = list(pd.read_excel('data.xlsx', skiprows=2))
# berichtheft(tabelle)
# print(tabelle)
temp = 1
while True:
    gc.collect()
    # break
    temp += 1
    # if True:
    try:
        tabelle = list(pd.read_excel(filename, skiprows=temp))
        if tabelle == []:
            print("tabelle leer")
            break
        berichtheft(tabelle)
        
    except:
        print("tabelle error")
        break

