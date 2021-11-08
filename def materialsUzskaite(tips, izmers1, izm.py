def materialsUzskaite(tips, izmers1, izmers2, skaits):
    #materialuAprekins() nodos datus
    #tips - "FINIERIS", "LISTE", "LENKIS"
    #"FINIERIS" - izmers1, izmers2 - garums platums, skaits
    #"LISTE" - izmers1(garums), skaits
    #"LENKIS" - skaits
    pass

def materialuAprekins(platums, garums, augstums, skaits):
    #Mainigie raksturo podestu
    #podestam augsa un apaksa
    materialsUzskaite("FINIERIS", platums, garums, 2*skaits)
    #prieksa un aizmugure
    materialsUzskaite("FINIERIS", garums, augstums, 2*skaits)
    #sanu malas
    materialsUzskaite("FINIERIS", platums, augstums, 2*skaits)

    materialsUzskaite("LISTE", garums, 0, 4*skaits)

    materialsUzskaite("LISTE", platums, 0, 4*skaits)

    materialsUzskaite("LISTE", augstums, 0, 4*skaits)

    materialsUzskaite("LENKIS", 0, 0, 8*skaits)