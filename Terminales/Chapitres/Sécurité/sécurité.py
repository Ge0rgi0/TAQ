ALPHABET = ['a','b','c','d','e','f','g','h','i','j','k','l','m',
            'n','o','p','q','r','s','t','u','v','w','x','y','z']

# ============================================================
# 1.1 CHIFFREMENT DE CÉSAR
# ============================================================

# Exercice 1 : Chiffrer SECURITE avec décalage 5
def chiffrement_cesar(m: str, k: int) -> str:
    """Chiffre le message m avec le décalage k (César)."""
    res = ""
    for lettre in m.lower():
        if lettre in ALPHABET:
            indice = (ALPHABET.index(lettre) + k) % len(ALPHABET)
            res += ALPHABET[indice]
        else:
            res += lettre  # conserve les espaces et caractères spéciaux
    return res

# Exercice 2 : Déchiffrer
def dechiffrement_cesar(m: str, k: int) -> str:
    """Déchiffre le message m chiffré avec le décalage k (César)."""
    return chiffrement_cesar(m, -k)

# Tests ex 1 & 2
print("=== César ===")
print(chiffrement_cesar("securite", 5)) # -> xjhzwnyj
print(dechiffrement_cesar("cpgjid r thi bxtjm fjt dct extrt", 15))

# Exercice 4 : Déchiffrement sans connaître la clé
def dechiffrement_cesar_statistique(m: str, l: str) -> str:
    """
    Déchiffre un message César sans connaître la clé,
    en supposant que la lettre la plus fréquente est l.
    """
    # Compter les occurrences de chaque lettre
    frequences = {}
    for lettre in m.lower():
        if lettre in ALPHABET:
            frequences[lettre] = frequences.get(lettre, 0) + 1
    
    # Trouver la lettre la plus fréquente
    lettre_plus_frequente = max(frequences, key=frequences.get)
    
    # Calculer la clé : si cette lettre correspond à l
    indice_e = ALPHABET.index(l)
    indice_lettre = ALPHABET.index(lettre_plus_frequente)
    cle_estimee = (indice_lettre - indice_e) % len(ALPHABET)
    
    print(f"Lettre la plus fréquente : '{lettre_plus_frequente}'")
    print(f"Clé estimée : {cle_estimee}")
    
    return dechiffrement_cesar(m, cle_estimee)

# Test
message_chiffre = "cpgjid r thi bxtjm fjt dct extrt"
print(dechiffrement_cesar_statistique(message_chiffre, 'e'))


# ============================================================
# 1.2 CHIFFREMENT DE VIGENÈRE
# ============================================================

# Exercice 3 : fonctions chiffrement/déchiffrement
def chiffrement_vigenere(m: str, k: str) -> str:
    """Chiffre le message m avec la clé k (Vigenère)."""
    res = ""
    k = k.lower()
    i = 0  # indice dans la clé (ne progresse que sur les lettres)
    for lettre in m.lower():
        if lettre in ALPHABET:
            decalage = ALPHABET.index(k[i % len(k)])
            indice = (ALPHABET.index(lettre) + decalage) % len(ALPHABET)
            res += ALPHABET[indice]
            i += 1
        elif lettre == " ":
            res += lettre  # conserve espaces et ponctuation
    return res

def dechiffrement_vigenere(m: str, k: str) -> str:
    """Déchiffre le message m chiffré avec la clé k (Vigenère)."""
    res = ""
    k = k.lower()
    i = 0
    for lettre in m.lower():
        if lettre in ALPHABET:
            decalage = ALPHABET.index(k[i % len(k)])
            indice = (ALPHABET.index(lettre) - decalage) % len(ALPHABET)
            res += ALPHABET[indice]
            i += 1
        else:
            res += lettre
    return res

# Tests ex 1 & 2
print("\n=== Vigenère ===")
print(chiffrement_vigenere("message", "cle"))   # → oiuwycc
print(dechiffrement_vigenere("tn nfaac pvivbhr papyhqbs dr frhbdrr rlgpbmshpiyhtlg", "batman"))


# ============================================================
# 1.3 CHIFFREMENT XOR
# ============================================================

def xor(a: int, b: int) -> int:
    """Applique l'opération XOR bit à bit sur deux entiers."""
    return a ^ b

def chiffrement_xor(m: str, k: str) -> list:
    """
    Chiffre le message m avec la clé k via XOR.
    Renvoie une liste d'entiers (les codes chiffrés).
    """
    codes = []
    for i, caractere in enumerate(m):
        code_char = ord(caractere)
        code_cle  = ord(k[i % len(k)])
        codes.append(code_char ^ code_cle)
    return codes

def dechiffrement_xor(codes: list, k: str) -> str:
    """
    Déchiffre une liste de codes XOR avec la clé k.
    Grâce à la propriété XOR : (a XOR b) XOR b = a
    """
    res = ""
    for i, code in enumerate(codes):
        code_cle = ord(k[i % len(k)])
        res += chr(code ^ code_cle)
    return res

# Test
print("\n=== XOR ===")
message = "BONJOUR"
cle = "HI"
codes = chiffrement_xor(message, cle)
print("Codes chiffrés :", codes)          # → [10, 6, 6, 3, 7, 28, 26]
print("Déchiffré :", dechiffrement_xor(codes, cle))  # → BONJOUR

print(dechiffrement_vigenere("EE ZDAAES IAUIPIKE IZQLBCUROT WQ GEBNWQS EFSIANFBBBXIGFS","batman").upper())