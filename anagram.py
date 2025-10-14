# sort in alphanumerical order
def alpha_sorting(text):
    abc = "abcdefghijklmnopqrstuvwxyz"
    result = ""
    i = 0
    while i < len(abc):
        if abc[i] in text.lower():
            result += abc[i]*(text.lower().count(abc[i]))
        i += 1
    return result