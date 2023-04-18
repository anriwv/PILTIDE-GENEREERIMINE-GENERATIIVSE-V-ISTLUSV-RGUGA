NRG PT2023

### PILTIDE GENEREERIMINE GENERATIIVSE VÕISTLUSVÕRGUGA

#### Antud praktilise töö eesmärgiks oli arendada lihtsalt kasutatav tööriist, mis suudab genereerida kvaliteetseid pilte, mis on sarnased tegelikele piltidele, kasutades generatiivset võistlusvõrku
## Eesmärki saavutamiseks esitati järgmised ülesanded:
- [x]Teada saada generatiivse võistlusvõrku tööpõhimõtet.
- [x]Koostada generatiivse võistlusvõrgu arhitektuuri.
- [x]Andmete ette valmistada ja kasutada piltide genereerimiseks.
- [x]Läbiviija eksperimente mudeli parandamiseks.
- [x]Võrrelda erinevate generatiivsete võistlusvõrkude tulemusi.
- [x]Koostada lõplik lihtsalt kasutatav töörist


Autor kasutas oma andmestiku loomiseks ühte [kogumit](https://www.kaggle.com/datasets/greg115/abstract-art), mis koosnes 8145 abstraktsest värvilisest pildist suurusega 512x512 pikslit, mis on pärit Kaggle'i andmekogust. 

Autor otsustas muuta piltide suurust 128x128 pikslini. Samuti oli vaja eemaldada värvilisus, et saada ühtne halltoonidega piltide.  ([lõplik andmekogum](https://www.kaggle.com/datasets/anrisokolov/abstract-art-1281281-17))


Selleks kasutati koodi [compress.ipynb](https://github.com/anriwv/PILTIDE-GENEREERIMINE-GENERATIIVSE-V-ISTLUSV-RGUGA/blob/main/teisendamine/compress.ipynb)

Teisendamine:

![](https://github.com/anriwv/PILTIDE-GENEREERIMINE-GENERATIIVSE-V-ISTLUSV-RGUGA/blob/main/teisendamine/0.png)

Mudeli treenimise jaoks kasutas autor [Kaggle'i platvormi](https://www.kaggle.com/code/anrisokolov/17img)

Treenimise käigus genereeritakse näidispilte. Selline lähenemine võimaldab mudeli treeningu ajal visualiseerida, kuidas generatiivne mudel areneb.

![](https://github.com/anriwv/PILTIDE-GENEREERIMINE-GENERATIIVSE-V-ISTLUSV-RGUGA/blob/main/mudel/epo1-100.png)

Mudeli treenimise lõpus salvestatakse kaalud [faili .h5](https://github.com/anriwv/PILTIDE-GENEREERIMINE-GENERATIIVSE-V-ISTLUSV-RGUGA/blob/main/mudel/generator_modelKaggle-17.h5)  Nende salvestamine failina võimaldab neid hiljem taaskasutada.

[Koodiga](https://github.com/anriwv/PILTIDE-GENEREERIMINE-GENERATIIVSE-V-ISTLUSV-RGUGA/blob/main/tkinterKood/AP/app.py) saab kasutada treenitud mudelit piltide genereerimiseks ja neid kuvada kasutajaliideses või salvestada failina.
![](https://github.com/anriwv/PILTIDE-GENEREERIMINE-GENERATIIVSE-V-ISTLUSV-RGUGA/blob/main/tkinterKood/pltjatk.png)

Töö sisaldab endas loomingulist, praktilist ja analüütilist komponenti. 
Antud töö koostati 2023. aastal praktilise tööna.

>python.exe -m pip install --upgrade pip
>
>pip install -r requirements.txt
