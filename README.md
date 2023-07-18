# Gasolineira
Więcej gasoliny. Python 3.10

# getFilms:
Klawisz y zapisuje pozycję kursora. Klawisz n kończy program i zapisuje przechowane pozycje do pliku.

Z opcją --config pozycje kursora są zapisane do pliku konfiguracyjnego. Trzeba go utworzyć przed pierwszym użyciem i po zmianie monitora/skalowania itd. Powinny to być w kolejności:
- pole z nazwą użytkownika
- pole z hasłem
- przycisk wyloguj
- przycisk przełączający kalendarz na następny dzień

# setFilms
W funkcji logIn() trzeba w odpowiednie argumenty wpisać swojego mejla oraz hasło.

# Uruchamianie pod linuxem
Najpierw trzeba wywołać następującą opcję, by root uzyskał uprawnienia interakcji z interfejsami graficznymi:
```
xhost si:localuser:root
```

Aby usunąć uprawnienia:
```
xhost -si:localuser:root
```

Wszystko trzeba odpalać przez sudo.

W przypadku używania wirtualnych środowisk (np. pyenv) należy wywołać skrypt przez pythona z odopowiedniej ścieżki venva ręcznie, np.:
```
sudo XYZ/.pyenv/versions/gasolineira/bin/python ABC/getFilms.py
```

HF
