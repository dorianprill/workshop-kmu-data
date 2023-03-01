# Praxis-Workshop: Getting Started mit Data Science in KMU

## Grundkentnisse Programmierung/Scripting/EDV vorausgesetzt

Praxisorientierter Intensivkurs behandelt folgende Grundlagen und Anwendungen von Data-Science mit Python

- Dateninfrastruktur und Werkzeuge
- Visualisierung und Exploration von Daten
- Erarbeiten einer Fragestellung zur Modellierung

### Vorausgesetzte Kenntnisse

- Grundlagen der Programmierung in egal welcher Sprache
- Umgang mit der Kommandozeile

## Systemvoraussetzungen

- Ein modernes Betriebssystem: Linux, MacOS oder Windows 10/11
- Halbwegs aktueller Prozessor ( < ~8 jahre, dezidierte GPU nicht notwendig)
- Python 3.11.2 (Aktuelle Version, wurde hiermit getestet)
- pip - Package Installer for Python (Wird normalerweise mit Python mitgeliefert)

## Installation

Als erstes muss der Python-Interpreter und ggf. Paketmanager und Launcher (`py` unter Windows) selbst installiert werden.

1. Python direkt ueber den Paketmanager in Linux/MacOS installieren.  
Falls Version 3.11.2 noch nicht verfügbar sein sollte, alternativ das offizielle [Release hier herunterladen](https://www.python.org/downloads/release/python-3112/)
2. Gegebenenfalls PIP installieren [Dokumentation](https://pip.pypa.io/en/stable/installation/)

## Erstellen der Virtuellen Umgebung

Aufgrund der globalen Sichtbarkeit von Abhängigkeiten in Python ist es besser, für jedes Projekt eine eigene, virtuelle Python-Umgebung zu erstellen. Dies garantiert reproduzierbares Verhalten.

Der Python Interpreter selbst bietet schon die Möglichkeit, eine virtuelle Python Umgebung zu erstellen. Allerdings muss hierbei lokal schon die gewünschte Zielversion von Python verwendet werden.

Alle folgenden Befehle sollten im Oberordner des Repository ausgeführt werden (Ebene dieser Readme.md).

Ein neues Virtual Environment im lokalen Ordner erzeugen Sie mit

```{Bash}
python -m venv env
```

Wobei `env` der Ordnername der virtuellen Umgebung ist, die durch den Befehl erzeugt wird.

Als naechstes muss diese nun aktiviert werden.
> Achtung: Dies muss in jeder neuen Shell erneut ausgeführt werden.

```{Bash}
source env/bin/activate
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

startet eine Weboberflaeche, die einer IDE ähnelt, jedoch auf o.g. Notebook-Format spezialisiert ist. Notebooks können dort in eigenen Tabs geöffnet werden.  

Alternativ steht auch noch die ursprüngliche Standalone-Anwendung zur Verfügung, welche etwas simpler aufgebaut ist.  
Die wird gestartet mit

```{Bash}
jupyter-notebook
```

und ist in der Regel ausreichend fuer diesen Workshop.

Jupyter in einer virtuellen Umgebung funktioniert übrigens auch sehr gut direkt in VSCode, falls Sie sich damit auskennen.
