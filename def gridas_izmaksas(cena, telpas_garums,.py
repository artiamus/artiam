def gridas_izmaksas(cena, linolejas_platums, telpas_garums, telpas_platums):
    if telpas_platums%linolejas_platums != 0:
        trukst = telpas_platums%linolejas_platums
        if trukst < linolejas_platums:
            papildus = round(linolejas_platums * telpas_garums)
            izmaksas = (round(telpas_garums*telpas_platums) + papildus) * cena
        elif trukst > linolejas_platums:
            lin_gab = round(trukst/linolejas_platums)
            papildus = lin_gab * linolejas_platums * telpas_garums
            izmaksas = (round(telpas_garums*telpas_platums) + papildus) * cena
    else:
        izmaksas = round(telpas_platums*telpas_garums)*cena
    return izmaksas
print(gridas_izmaksas(6,2,5,4))
