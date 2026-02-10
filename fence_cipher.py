def fence_cipher(str):
    even = []
    odd = []
    for index,char in enumerate(str):
        if index % 2 == 0:
            even.append(char)
        else:
            odd.append(char)

    temp="".join(even),"".join(odd)
    res="".join(temp)

    return res




