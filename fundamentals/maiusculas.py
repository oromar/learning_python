def maiusculas(frase):
    upper_case = []
    result = ''
    for i in range(len(frase)):
        if frase[i].isupper():
            upper_case.append(frase[i])
    for i in range(len(upper_case)):
        result += upper_case[i]
    return result
