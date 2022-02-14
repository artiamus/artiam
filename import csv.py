import csv

def kopa_csv(pirmaisCSV,OtraisCSV):

    with open(pirmaisCSV, 'r', encoding="utf-8") as fails:
        lasit_csv = csv.reader(fails)
        saturs = []
        for rinda in lasit_csv:
           saturs.append(rinda)
        
    with open(OtraisCSV, 'r', encoding="utf-8") as fails:
        lasit_csv = csv.reader(fails)
        saturs_otrajam = []
        for rinda in lasit_csv:
            saturs_otrajam.append(rinda)

    if len(saturs) == len(saturs_otrajam):
        with open ('divikopa.csv', 'r', encoding="utf-8",newline=''):
            csvwrite = csv.writer(fails)
            csvwrite.writerows(saturs)
            csvwrite.writerows(saturs_otrajam)

kopa_csv("pirmais.csv","otrais.csv")


            