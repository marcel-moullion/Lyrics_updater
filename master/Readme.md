# Lyrics Updater Readme

**Um den Lyrics Updater zu verwenden muss Python 2.7 auf dem Gerät installiert und in den  
Systemvariablen eingetragen sein.**

---

## Ordner Struktur

---

### master-Ordner

---
Dieser Ordner enthält:

* die Dateien zum Ausführen des Scripts (`"start_on_mac.command"/"start_on_windows.bat"`),
  Um das script auszuführen muss einmalig über das Terminal "chmod a+x start_on_mac.command" ausgeführt werden
* das Script zum Generieren der Songs (`"updateFiles.py"`),
* die Konfiguration welche Gruppen verfügbar sind und welche Farbe/Shorcuts diese
haben (`"masterConfig_Groups.pro6"`)
* sowie den Ordner der Textdateien der zu generierenden Songs (`textFiles`).

---

### Campus-Ordner

---
Dieser Ordner enthält:

* die config Dateien nach welchen die Songs generiert werden sollen (`"config_[Style].pro6"`)
* sowie die generierten Songs (`"[Titel]_[Sprache]_[Style].pro6"`).

---

## Konfigurations Files

---

### masterConfig_Groups.pro6

---
Dieses File befindet sich im *master* und enthält Informationen über die verfügbaren Gruppen  
sowie deren Farben und ShorKeys. Da diese Information in einem *.pro6* File abgespeichert wird,  
lässt sich die Konfiguration direkt in ProPresenter bearbeiten.  
Aus *masterConfig_Groups.pro6* werden ausschließlich:

* der Name der Gruppe (`bsp. "Bridge 1"`),
* die Farbe der Gruppe (`bsp. "gelb"`),
* und der ShortKey der Gruppe (`bsp. "B"`)

gelesen. Alle anderen Inhalte werden ignoriert.  

---

### config_[Style].pro6

---
Diese Files befinden sich in den jeweiligen Kampus-Ordnern und enthalten Informationen über  
das Aussehen und den Aufbau der einzelnen Slides. So werden z.B. Position, Größe, Schriftart, usw. festgelegt.  
Um die Elemente aus dem config-File lesen zu können muss dieses folgendem Aufbau entsprechen:

* Das config-File muss aus `einer Slide` bestehen.
* Das Element welches den primären Text enthält muss den namen `"TextElement"` haben.
* Die erste Zeile des Textes des primären TextElements muss mit `"This is the template Text"` beginnen.
* Falls es ein Element für den sekundären Text geben soll, muss dieses den name `"CaptionTextElement"` haben.
* Die erste Zeile des Textes des sekundären TextElements muss mit `"This is the caption template"` beginnen.
* Falls es ein Element für den Hintergrund geben soll, muss dieses den namen `"BottomLineShapeElement"` haben.
* Falls es ein zweites Element für den Hintergrund geben soll, muss dieses den namen `"TopLineShapeElement"` haben.
* Falls aus dem Style nur einzeilige Slides erzeugt werden sollen, muss in den Notes `"Only one line"` stehen.

---

## Text Files

---
Die Text Files zum generieren der Songs befinden sich im *master* im Ordner `"textFiles"` (`"[Titel].txt"`).  
Der Aufbau der Text Files muss folgendem Schema entsprechen:

```
DE                              <-- Name der ersten Sprache
                                <-- Leerzeile
Bridge 1                        <-- Name der ersten Gruppe
                                <-- Leerzeile
Erste Slide, erste Zeile        <-- Text
Erste Slide, zweite Zeile       <-- Text
                                <-- Leerzeile
Zweite Slide, erste Zeile       <-- Text
                                <-- Leerzeile
Dritte Slide, erste Zeile       <-- Text
                                <-- Zwei Leerzeilen trennung
                                <-- Zwei Leerzeilen trennung
EN                              <-- Name der zweiten Sprache
                                <-- Leerzeile
Bridge 1                        <-- Name der ersten Gruppe
                                <-- Leerzeile
First Slide, first Line         <-- Text
First Slide, second Line        <-- Text
                                <-- Leerzeile
Second Slide, first Line        <-- Text
                                <-- Leerzeile
Third Slide, first Line         <-- Text
                                <-- Zwei Leerzeilen trennung
                                <-- Zwei Leerzeilen trennung
Arrangements                    <-- Muss Arrangements heißen
                                <-- Leerzeile
Backing Track                   <-- Name des Arrangements
                                <-- Leerzeile
Bridge 1                        <-- Erste Gruppe des Arrangements
Bridge 1                        <-- Zweite Gruppe des Arrangements
                                <-- Leerzeile
Remix                           <-- Name des Arrangements
                                <-- Leerzeile
Bridge 1                        <-- Erste Gruppe des Arrangements
```

---
