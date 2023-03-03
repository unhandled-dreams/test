def encode(plaintext, keyword):

    plaintext = plaintext.replace(" ", "").upper()
    keyword = keyword.replace(" ", "")

    """ INVALID CASES """
    if len(plaintext) == 0 or len(keyword) == 0:
        return "ERROR: MISSING INPUT"
    if not keyword.isalpha():
        return "ERROR: KEYWORD MUST BE ALPHABET LETTERS ONLY"

    """ step 1: create the omega list with (m = keyword length) empty strings """
    m = len(keyword)
    omega = [""] * m

    """ step 2: build the priority list using the keyword """
    priority = []
    sorted_keyword = sorted(keyword)
    for char in keyword:
        p = sorted_keyword.index(char)
        priority.append(p)
        sorted_keyword[p] = None

    """ step 3: fill omega strings in PRIORITY order (one char at a time) """
    for i in range(len(plaintext)):
        p = priority[i % m]
        char = plaintext[i]
        omega[p] += char

    """ finally: concatenate omega strings in ASCENDING order """
    ciphertext = ""
    for i in range(m):
        ciphertext += omega[i]
    return ciphertext


def decode(ciphertext, keyword):

    ciphertext = ciphertext.replace(" ", "").upper()
    keyword = keyword.replace(" ", "")

    """ INVALID CASES """
    if len(ciphertext) == 0 or len(keyword) == 0:
        return "ERROR: MISSING INPUT"
    if not keyword.isalpha():
        return "ERROR: KEYWORD MUST BE ALPHABET LETTERS ONLY"

    """ step 1: create the omega list with (m = keyword length) empty strings """
    m = len(keyword)
    omega = [""] * m

    """ step 2: build the priority list using the keyword """
    priority = []
    sorted_keyword = sorted(keyword)
    for char in keyword:
        p = sorted_keyword.index(char)
        priority.append(p)
        sorted_keyword[p] = None

    """ step 3: fill omega strings in ASCENDING order (many chars at a time) """
    length = len(ciphertext) // m
    endpoint = len(ciphertext) % m
    start = 0
    for i in range(m):
        extra = priority.index(i) < endpoint
        end = start + length + extra
        omega[i] += ciphertext[start:end]
        start = end

    """ finally: concatenate omega strings in PRIORITY order (one char at a time) """
    plaintext = ""
    for i in range(len(ciphertext)):
        p = priority[i % m]
        string = omega[p]
        char = string[i // m]
        plaintext += char
    return plaintext


def interface():

    print("Welcome to the Columnar Transposition Cipher")
    print("* Enter 1 to Encode")
    print("* Enter 2 to Decode")
    print("* Enter anything else to terminate")

    while True:

        entry = input("\n" + "Entry: ")

        if entry == "1":
            plaintext = input("Plaintext: ")
            keyword = input("Keyword: ")
            print("=> " + encode(plaintext, keyword))
            continue

        if entry == "2":
            ciphertext = input("Ciphertext: ")
            keyword = input("Keyword: ")
            print("=> " + decode(ciphertext, keyword))
            continue

        print("=> thank you for using me bye <3")
        break


interface()
