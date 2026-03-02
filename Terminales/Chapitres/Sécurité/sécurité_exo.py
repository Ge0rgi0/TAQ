ALPHABET = ['a','b','c','d','e','f','g','h','i','j','k','l','m',
            'n','o','p','q','r','s','t','u','v','w','x','y','z']

# ============================================================
# 1.1 CHIFFREMENT DE CeSAR
# ============================================================

# Exercice 1 : Chiffrer
def chiffrement_cesar(m: str, k: int) -> str:
    """Chiffre le message m avec le decalage k (Cesar)."""
    passintegrer un fichier python à telecharger dans markdown

# Exercice 2 : Dechiffrer
def dechiffrement_cesar(m: str, k: int) -> str:
    """Dechiffre le message m chiffre avec le decalage k (Cesar)."""
    pass

# Tests ex 1 & 2
print("=== Cesar ===")
print(chiffrement_cesar("securite", 5)) # -> xjhzwnyj
print(dechiffrement_cesar("cpgjid r thi bxtjm fjt dct extrt", 15))

# Exercice 4 : Dechiffrement sans connaître la cle
def dechiffrement_cesar_statistique(m: str, l: str) -> str:
    """
    Dechiffre un message Cesar sans connaître la cle,
    en supposant que la lettre la plus frequente est l.
    """
    pass

# Test
message_chiffre = "cpgjid r thi bxtjm fjt dct extrt"
print(dechiffrement_cesar_statistique(message_chiffre, 'e'))


# ============================================================
# 1.2 CHIFFREMENT DE VIGENeRE
# ============================================================

# Exercice 3 : fonctions chiffrement/dechiffrement
def chiffrement_vigenere(m: str, k: str) -> str:
    """Chiffre le message m avec la cle k (Vigenere)."""
    pass

def dechiffrement_vigenere(m: str, k: str) -> str:
    """Dechiffre le message m chiffre avec la cle k (Vigenere)."""
    pass

# Tests ex 1 & 2
print("\n=== Vigenere ===")
print(chiffrement_vigenere("message", "cle"))   # → oiuwycc
print(dechiffrement_vigenere("tn nfaac pvivbhr papyhqbs dr frhbdrr rlgpbmshpiyhtlg", "batman"))


# ============================================================
# 1.3 CHIFFREMENT XOR
# ============================================================

def chiffrement_xor(m: str, k: str) -> list:
    """
    Chiffre le message m avec la cle k via XOR.
    Renvoie une liste d'entiers (les codes chiffres).
    """
    pass

def dechiffrement_xor(codes: list, k: str) -> str:
    """
    Dechiffre une liste de codes XOR avec la cle k.
    Grâce à la propriete XOR : (a XOR b) XOR b = a
    """
    pass

# Test
print("\n=== XOR ===")
message = "BONJOUR"
cle = "HI"
codes = chiffrement_xor(message, cle)
print("Codes chiffres :", codes)          # → [10, 6, 6, 3, 7, 28, 26]
print("Dechiffre :", dechiffrement_xor(codes, cle))  # → BONJOUR


