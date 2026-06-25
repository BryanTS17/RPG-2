alfabeto_minusculo = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]
alfabeto_maiusculo = [
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]
lista_numeros = [13, 1, 9, 19]
morse = {
    ".-": "A",
    "-...": "B",
    "-.-.": "C",
    "-..": "D",
    ".": "E",
    "..-.": "F",
    "--.": "G",
    "....": "H",
    "..": "I",
    ".---": "J",
    "-.-": "K",
    ".-..": "L",
    "--": "M",
    "-.": "N",
    "---": "O",
    ".--.": "P",
    "--.-": "Q",
    ".-.": "R",
    "...": "S",
    "-": "T",
    "..-": "U",
    "...-": "V",
    ".--": "W",
    "-..-": "X",
    "-.--": "Y",
    "--..": "Z",
    "-----": "0",
    ".----": "1",
    "..---": "2",
    "...--": "3",
    "....-": "4",
    ".....": "5",
    "-....": "6",
    "--...": "7",
    "---..": "8",
    "----.": "9",
    ".-.-.-": ".",
    "--..--": ",",
    "..--..": "?",
    "-.-.--": "!",
    "/": " ",
}


def decodificar(texto, voltar):
    novo_texto = ""
    for i in texto:
        for j in range(len(alfabeto_minusculo)):
            if i == alfabeto_minusculo[j]:
                novo_texto += alfabeto_minusculo[j - voltar]
                break

        for j in range(len(alfabeto_maiusculo)):
            if i == alfabeto_maiusculo[j]:
                novo_texto += alfabeto_maiusculo[j - voltar]
                break

        if i not in alfabeto_minusculo and i not in alfabeto_maiusculo:
            novo_texto += i

    return novo_texto


def codificar(texto, voltar):
    novo_texto = ""
    for i in texto:
        for j in range(len(alfabeto_minusculo)):
            if i == alfabeto_minusculo[j]:
                num = voltar
                while num > 0:
                    num -= 1
                    j += 1
                    if j > len(alfabeto_minusculo) - 1:
                        j = 0
                novo_texto += alfabeto_minusculo[j]
                break

        for j in range(len(alfabeto_maiusculo)):
            if i == alfabeto_maiusculo[j]:
                num = voltar
                while num > 0:
                    num -= 1
                    j += 1
                    if j > len(alfabeto_maiusculo) - 1:
                        j = 0
                novo_texto += alfabeto_maiusculo[j]
                break

        if i not in alfabeto_minusculo and i not in alfabeto_maiusculo:
            novo_texto += i

    return novo_texto


def tranformar_letra(lista):
    novo_texto = ""
    for i in lista:
        novo_texto += alfabeto_maiusculo[i - 1]
    return novo_texto


def binario(texto):
    binario = ""
    for letra in texto:
        binario += format(ord(letra), "08b") + " "
    return binario.strip()


def texto_normal(binario):
    texto = ""
    for byte in binario.split():
        texto += chr(int(byte, 2))
    return texto


def morse_para_texto(morse_code):
    novo_texto = ""
    for i in morse_code.split():
        if i in morse:
            novo_texto += morse[i]

    return novo_texto


#print("Texto em binario:", binario("Bryan"))
#print("Texto normal:", texto_normal("01000101"))
#print("Decodificado:", decodificar("dbsjoib", 3))
print(" Codificado:", codificar("acho que pode dar certo mas se pa nois sabe mais que ele", 3))
#print("Transformado em texto:", tranformar_letra(lista_numeros))
#print(
#    "Morse para texto:",
#    morse_para_texto(".... .- -.-. -.- . .- .-."),
#)

num = 0
while True:
    num += 1
    print(f"{num}: {decodificar('gews zsgi wemfe s rsqi hipi sy epkyqe mrjsvqeies he tve qmq gspsgev s rsqi i ew mrjsvqeies hipi iq yqe jivveqirxe u tybe xyhs he mrxivrix tve rsmw hiwgsfvmv qemw wsfvi ipi', num)}")
    if num >= 25:
        break
