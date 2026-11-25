import csv

rows = []
with open("data/adresser.csv", encoding="utf-8") as f:
    for r in csv.reader(f, delimiter=";"):
        pn = r[2].strip().zfill(4)
        if len(pn) == 4 and pn.isdigit():
            rows.append([r[0], r[1], pn])
        else:
            print("Fejl:", r)
with open("data/resultat.csv", "w", encoding="utf-8", newline="") as f:
    csv.writer(f, delimiter=";").writerows(rows)
