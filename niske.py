# -*- coding: utf-8 -*-
"""
Created on Fri Jun 30 13:56:58 2017

@author: admin
"""

print(1458 + 8597 == 10055)
print(5 + 5 < 6 + 6)
print(8 + 4 >= 8 + 5)
print("kolač" != "torta")
print(len("kolač") != len("torta"))

rečenica = "Ja više neću biti niska."
lista_reči = rečenica.split(" ")

Milena je sinoć videla Mitra, nežnog, zelenog skakavca ispred stacionara i uzviknula je: "Ju, Mitre, uplašio si me!". Ali Mitar se na to nije obazirao - žustro je skočio u Mileninom pravcu. Videvši to, Milena polete preko dvorišta i polete ka stacionaru brzinom svetlosti. Nažalost, svetlost je brža od automatskog mehanizma za otvaranje vrata. I tako ostade Milenin trag na ulaznim vratima IS Petnica.
tekst = " Milena je sinoć videla Mitra, nežnog, zelenog skakavca ispred stacionara i uzviknula je: \"Ju, Mitre, uplašio si me!\". Ali Mitar se na to nije obazirao - žustro je skočio u Mileninom pravcu. Videvši to, Milena polete preko dvorišta i polete ka stacionaru brzinom svetlosti. Nažalost, svetlost je brža od automatskog mehanizma za otvaranje vrata. I tako ostade Milenin trag na ulaznim vratima IS Petnica. "
tekst = tekst.lower()
lista_reči = tekst.split(" ")
print(lista_reči)
tekst = " Milena je sinoć videla Mitra, nežnog, zelenog skakavca ispred stacionara i uzviknula je: \"Ju, Mitre, uplašio si me!\". Ali Mitar se na to nije obazirao - žustro je skočio u Mileninom pravcu. Videvši to, Milena polete preko dvorišta i polete ka stacionaru brzinom svetlosti. Nažalost, svetlost je brža od automatskog mehanizma za otvaranje vrata. I tako ostade Milenin trag na ulaznim vratima IS Petnica. "
karakteri = list(tekst)
print(karakteri)