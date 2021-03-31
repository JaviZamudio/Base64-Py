def menu() -> int:
    print("\n\t - - - Base 64 - - -")
    print("1) Encode")
    print("2) Decode")
    print("0) Exit")    
    return int(input("Option: "))

def intToBin(num:int = 0) -> str:
    pos = 8
    result = ""
    for i in range(pos,0,-1):
        if(2 ** (i - 1) <= num):
            result += "1"
            num -= 2 ** (i - 1)
        else:
            result += "0"
    
    return result

def binToInt(num:str = "") -> int:
    res = 0
    exp = len(num) - 1

    if len(num) == 0:
        return 0
    for i in range(len(num)):
        if(num[i] == "1"):
            res += 2 ** exp
        exp -= 1


    return res

def b256ToB64(pos:int = 0) -> str:
    table = "=BCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    return table[pos]

def b64ToB256(char:str) -> int:
    table = "=BCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    return table.find(char)

def encode(text:str) -> str:
    result = ""
    textBin = ""

    for char in text:
        textBin += intToBin(ord(char))

    letters = []

    while 0 < len(textBin):
        if(len(textBin) >= 6):
            letters += [textBin[:6]]
            textBin = textBin[6:]
        else:
            textBin += "00000000"

    for letter in letters:
        result += b256ToB64(binToInt(letter))

    return result

def decode(text:str) -> str:
    result = ""
    textBin = ""

    for letter in text:
        textBin += intToBin(b64ToB256(letter))[2:]
    
    while len(textBin):
        letter = chr(binToInt(textBin[:8]))
        if(letter == chr(0)):
            break
        result += letter
        textBin = textBin[8:]

    return result

def main():
    option = menu()
    
    #encode
    if option == 1:
        text = input("Give me the text to encode: ")
        print("Result: " + encode(text))
    elif option == 2:
        text = input("Give me the text to decode: ")
        print("Result: " + decode(text))
    elif option == 0:
        exit()

while True:
    main()