# PL, for english version see below

Projekt wykonany w ramach zaliczenia przedmiotu akwizycja danych telemetrycznych (ADT). Potrzebne komendy na samym dole

Realizuje on wizualizację sieci wifi osób, które rano przyjeżdzają do na dworzec w Legionowie. 
Wspomniane sieci zebrane zostały przy użyciu oprogramowania WireShark. 

# ENG

Project for ADT, realising data canvassing and visualization. 
The data is wi-fi signals collected from people visiting Legionowo central station.

# Commands - must have at least python 3.x installed
git clone https://github.com/przempol/adt-networks

virtualenv venv

venv\Scripts\activate

pip install -r requirements.txt

python main.py

deactivate

