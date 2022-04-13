1README
Se creaza un request in care cerem cele mai relevante videouri cu "q-ul" "cancer 
colorectal" si date despre acestea (cu 'snippet' aflam numele canalului, cu 
'contentDetails' aflam durata videoului, cu 'statistics' in mare marte, restul).
Cream 'all_data' si il initializam ca fiind gol (o matrice in care stocam
informatiile)
Cream un response, executand reqestul

2README
Folsind un i care are 'range-ul' cat 'lenght-ul' itemurilor din 'response' (cate
itemuri sunt, pana acolo va merge i).
Folosind 'data' (un vector), stocam informatiile despre fiecare video, dupa care le
punem in 'all_data'.
Repetam pentru fiecare i (adica fiecare video).
Printam matricea cu datele despre fiecare video.

PROBLEME:

1. Cand creez for-ul, apare o problema care zice ca 'items' este KeyWord Error 
(adica items nu este folosit in acel dictionar).
Posibila cauza, i si 'items' sunt de forme diferite.
2. Cand se da requestul la inceput, apare HttpError 400.
3. Problema majora este ca nu se pot obtine toate datele dintr-un singur request.
Este nevoie, spre exemplu, de 'youtube.search', 'youtube.comments' si 'youtube.videos' pentru
a obtine toate datele necesare. Intrucat nu am reusit sa trec de eroarea de la punctul 
numarul 1, nu pot spune sigur daca va merge sau nu, insa as presupune ca nu va merge, 
si este nevoie de un mod de a combina mai multe requesturi. Desi suna simplu, problema 
peste care am dat este ca doar la 'youtube.search' te poti folosi de 'q' si sa cauti videori
in functie de un keyword. In rest, nu exista parametrul 'q'.