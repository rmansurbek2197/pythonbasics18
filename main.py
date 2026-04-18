def eng_uzun_soz(matn):
    sozlar = matn.split()
    eng_uzun = sozlar[0]
    for soz in sozlar:
        if len(soz) > len(eng_uzun):
            eng_uzun = soz
    return eng_uzun

matn = "Bu mening birinchi dasturim"
print(eng_uzun_soz(matn))

def eng_uzun_soz2(matn):
    sozlar = matn.split()
    sozlar.sort(key=len, reverse=True)
    return sozlar[0]

matn = "Bu mening birinchi dasturim"
print(eng_uzun_soz2(matn))

def eng_uzun_soz3(matn):
    sozlar = matn.split()
    max_uzunlik = 0
    eng_uzun = ""
    for soz in sozlar:
        if len(soz) > max_uzunlik:
            max_uzunlik = len(soz)
            eng_uzun = soz
    return eng_uzun

matn = "Bu mening birinchi dasturim"
print(eng_uzun_soz3(matn))