Generieren von Berichtsheften und für bessere Übersicht:

Nach Beachtung von unten kann das Programm direkt mit Python geöffnet werden ohne Bearbeitungssoftware

Das Hauptprogramm "BerichteErstellen.py" braucht:

pip install reportlab
pip install Pandas
pip install openpyxl

- Excel Datei mit dem Name: data.xlsx | Vorlage ist im Ordner
 - Absätze werden durch ein ";" gekennzeichnet
 - Namen mit Nachnamen eintragen
 - created Collum "no" eintragen um ein BH zu erstellen alles andere verhindert Erstellung der PDf
 - Berichtsheft Nummer, Kalenderwoche und Jahr muss selbst eingetragen werden
  - Tipp: nach den ersten zwei Zeilen alle sechs Felder auswählen und unten rechts vom markiertem herunterziehen
 - Leere Felder mit Überschrift können Probleme bereiten einfach einen "." reinmachen falls es leer sein sollte

- empty.jpg ist das Image welches für die Berichte verwendet wird
- ein Leerer Ordner mit dem Namen "generierteBerichte"
 - in diesem Ordner werden die neu erstellten Berichte reingeschrieben




