def pasuti_tkreklus(skaits, apdruka, piegadi):
    cena = {'TEKTS':5,'ZIME':7,'FOTO':20}
    piegadi = {True:15, False:0}
    apdrukas_vert = cena[apdruka] * skaits
    if apdrukas_vert < 50:
        return apdrukas_vert + 15
    elif apdrukas_vert >= 50:
        return apdrukas_vert
    elif apdrukas_vert > 100:
        return apdrukas_vert *0.05
    else:
        if apdrukas_vert > 100:
            return apdrukas_vert * 0.05
        else:
            return apdrukas_vert
print(pasuti_tkreklus(5,'FOTO', True))
