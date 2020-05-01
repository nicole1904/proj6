Proj6 (Recommender)

Program sa spusta z main.py, nasledne sa zobrazi GUI okno, kde sa zada ID pozadovaneho uzivatela. 
Stlacenim tlacidla "OK" program najde podobnych uzivatelov a odpuruci zadanemu uzivatelovi najviac 15 filmov, ktore este nehodnotil. 
Pri zadani uzivatela, ktory neexistuje, program vypise chybu, ale neskonci a je mozne zadat noveho uzivatela na prehladavanie.

Program ma 2 vstupne subory, data.csv a movie_titles.csv. 
movie_titles.csv osahuje ID filmu, jeho nazov a rok vydania. 
data.csv obsahuje data ID uzivatela, ktory dany film hodnotil, pocet hviezdiciek, ktore filmu dal a datum hodnotenia. 
Vstupne subory musia byt v rovnakom formate ako su testovacie subory a musia mat priponu .csv

Program taktiez vyzaduje externe kniznice: pandas (vytvorenie tabulky hodnotenia), PySimpleGUI (vykreslenie GUI), numpy (vzorce na vypocet podobnosti a ine matematicke funkcie) a csv (nacitanie vstupnych hodnot zo suborov)

Program je z velkej casti inspirovany: z https://medium.com/@sam.mail2me/recommendation-systems-collaborative-filtering-just-with-numpy-and-pandas-a-z-fa9868a95da2