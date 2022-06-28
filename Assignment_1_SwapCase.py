def swap_case(sentence):
    updated_s = ""
    for i in sentence:
        if i.isupper():
            updated_s += i.lower()
        elif i.islower():
            updated_s += i.upper()
        else:
            updated_s += i
    return updated_s


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
