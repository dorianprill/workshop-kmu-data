# DIH West Praxis-Workshop: Data Science in KMU

Dieser praxisorientierte Intensivkurs basiert auf dem an der Fachhochschule Salzburg abgehaltenen [DIH Praxis-Workshop Data Science in KMU](https://dih-west.at/events/praxisworkshop-data-science-in-kmu/) und behandelt folgende Grundlagen und Anwendungen der Datenanalyse, Exploration und Modellierung mit Python:

- Anforderungen and ihre Daten
- Gaengige Werkzeuge, Sprachen, Bibliotheken
- Visualisierung und Exploration von Daten
- Erarbeiten einer Fragestellung zur Modellierung
- Grundlagen der Modellierung

## Vorausgesetzte Kenntnisse

- Grundlagen der Programmierung (auch Scripting) in egal welcher Sprache
- Umgang mit der Kommandozeile, und Standardwerkzeugen
- Grundlagen der Algebra und Statistik

## Systemvoraussetzungen

- Ein modernes Betriebssystem: Linux, MacOS oder Windows 10/11
- Halbwegs aktueller Prozessor ( < ~8 jahre, dezidierte GPU nicht notwendig)
- Python 3.11.2 (getestet, theoretisch sollte jede ab 3.6 funktionieren)
- pip - Package Installer for Python (Wird normalerweise mit Python mitgeliefert)

## Installation

Als erstes muss der Python-Interpreter und ggf. Paketmanager `pip` (und Launcher `py` unter Windows) selbst installiert werden.

### Linux/*BSD/MacOS

Python direkt ueber den Paketmanager in Linux/MacOS installieren.  
Falls Version 3.11.2 noch nicht verfügbar sein sollte, alternativ das offizielle [Release hier herunterladen](https://www.python.org/downloads/release/python-3112/)

### Windows

Offiziellen Installer der Python Distribution [hier herunterladen](https://www.python.org/downloads/windows/) und installieren.
Stellen Sie sicher, dass die Installation des `py`-Launcher ausgewaehlt ist.
Auf einen Single-User-System (quasi alle) sollten Sie als Installationspfad z.B. `C:\Program Files\Python3.X` oder `C:\Python3.X` waehlen und sicherstellen, dass die Option "Add Python to PATH" aktiviert ist.

Sollte auf ihrem System `pip` nicht installiert sein, folgen sie den Anweisungen in der [PIP Dokumentation](https://pip.pypa.io/en/stable/installation/)

## Verifizieren der Installation
Pruefen Sie, ob die Programme richtig installiert sind, indem sie sie jeweils mit dem --version Argument aufrufen:
```{Bash}
python --version
pip --version
```
Sollte dies nicht funktionieren, pruefen Sie, ob die Programme im PATH sind, oder ob Sie die installierte Versionsnummer explizit aufrufen muessen, moegliche Namen sind z.B.:
```{Bash}
python3 
pip3
python311
python3.11
```

## Erstellen der Virtuellen Umgebung

Aufgrund der globalen Sichtbarkeit von Abhängigkeiten in Python ist es besser, für jedes Projekt eine eigene, virtuelle Python-Umgebung zu erstellen. Dies garantiert reproduzierbares Verhalten und gilt als  Best-Practice.

Der Python Interpreter selbst bietet die Möglichkeit, fuer sie eine virtuelle Python Umgebung zu erstellen. Allerdings muss hierbei beim Aufruf schon die gewünschte Zielversion von Python verwendet werden (Falls sie mehrere parallel installiert haben).

Alle folgenden Befehle sollten im Oberordner des Repository ausgeführt werden (Ebene dieser Readme.md).

Ein neues Virtual Environment im lokalen Ordner erzeugen Sie mit

```{Bash}
python -m venv env
```

Wobei `env` der (frei waehlbare) Ordnername der virtuellen Umgebung ist, die durch den Befehl erzeugt wird.

Als naechstes muss diese nun aktiviert werden.

> Achtung: Dies muss in jeder neuen Shell erneut ausgeführt werden.

### Linux/*BSD/MacOS

```{Bash}
source env/bin/activate
```

### Windows

```{Bash}
env\Scripts\activate
```

Eine genauere Anleitung fuer die verschiedenen Betriebssysteme finden Sie in der [offiziellen Dokumentation zu venv](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

Anschließend kümmern wir uns um die für unseren Workshop benötigten Pakete. Diese sind in der [Requirements-Datei](requirements.txt) direkt fuer pip lesbar aufgelistet.

```{Bash}
pip install -r requirements.txt
```

## Starten der Notebook-Server

Das gesamte Kursmaterial ist in sogennanten (jupyter) "notebooks" erstellt worden. Dies ist ein gemischtes Dateiformat, in welchem Code, Strukturierter Text (Markdown) und Mathematische Formeln nebeneinander dargestellt und ausgeführt werden koennen.  
Dieses Format wird mittlerweile weitlaeufig in verschiedenen IDEs unterstuetzt.  

Als erstes aktivieren Sie wieder die virtuelle Umgebung, falls noch nicht geschehen:

```{Bash}
./env/Scripts/activate.py
```

Das ausfuehren von

```{Bash}
jupyter-lab
```

startet eine Weboberflaeche, die einer IDE ähnelt, jedoch auf o.g. Notebook-Format spezialisiert ist. Mehrere Notebooks können dort in eigenen Tabs geöffnet werden.  

Alternativ steht auch noch die ursprüngliche Single-Notebook-Anwendung zur Verfügung, welche etwas simpler aufgebaut ist (besser geeignet fuer kleine Aufloesungen).  
Die wird gestartet mit

```{Bash}
jupyter-notebook
```

und ist in der Regel ausreichend fuer diesen Workshop.

Jupyter in einer virtuellen Umgebung funktioniert übrigens auch sehr gut direkt in VSCode, falls Sie das bereits nutzen.