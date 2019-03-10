# SLOT_magazyn_v2
Program obsługujący Magazyn Sceniczny na Slot Art Festival

### Opis

Program ten pozwala na stworzenie planu magazynu z wydzielonymi obszarami. 
Użytkownik po zalogowaniu może dodawać nowe obszary oraz edytować ich właściwości. 
Dla każdego obszaru użytkownik może przyjąc nowy przedmiot oraz wydać bądź przyjąć istniejący przedmiot.

Wszystkie informacje o obszarach, przedmiotach, użytkownikach są przechowywane w lokalnej bazie danych.

### Kod
Główny plik wykonywalny programu to "magazyn.py". 
Dwa pomocnicze pliki to "clear_gui.py" odpowiadający za interfejs użytkownika oraz 
"slotbaza.py" odpowiadający za komunikację z bazą danych.

Główna okno programu opisuje klasa "Magazyn" dziedzicząca po MainWindow z biblioteki PyQt.

### Wymagane biblioteki
Do poprawnego działania programu niezbędny jest Python w wersji 3.x. 
Ponad to wymagane są nstępujące biblioteki: PyQt 5.x, peewee, hashlib, sqlite3.

### Inne wymagania
Minimalna rozdzielczość ekranu: 1280x900\
Maksymalna rozdzielczość ekranu: 1920x1280\
Minimum 2GB pamięci RAM\
System operacyjny wspierający sterownik bazy danych SQL