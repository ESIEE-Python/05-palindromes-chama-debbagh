""" Programme qui verifie si une chaine de caractere est un palindrome """
#### Fonction secondaire

def ispalindrome(p):
    """ FONCTION SECONDAIRE QUI DETERMINE SI UNE CHAINE
     EST UN PALINDROME OU PAS TOUT EN ELIMINANT LES ACCENTS ET LES ESPACES """
    table=str.maketrans('àâäéèêëîïôöùûüÿç' , 'aaaeeeeiioouuuyc' , " ")
    p=p.lower().translate(table)
    #suprime les caractere non alphabetique
    caractere=''
    for i in p:
        if ('a' <= i <= 'z') or ('0' <= i <= '9') :
            caractere += i
    #verifie si c'est un palindrome
    return caractere==caractere[::-1]
#### Fonction principale

def main():

    # vos appels à la fonction secondaire ici
    """ fait les teste de la fonction secondaire et verifie si les exemple sont des palindrome"""

    for s in ["radar", "kayak", "level", "rotor", "civique", "deifie"]:
        print(s, ispalindrome(s))


if __name__ == "__main__":
    main()
#resultat si une chaine de caractere est un palindrome
