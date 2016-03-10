def replace(str, *params):
    return str.replace(params[0], params[1])


def capitalizeAll(str, *params):
    return str.title()


def capitalize_(str, *params):
    return str[0].upper() + str[1:]


def a(str, *params):
    if len(str) > 0:
        if str[0].lower() == 'u':
            if len(str) > 2:
                if str[2].lower() == 'i':
                    return "a " + str
        if str[0].lower() in "aeiou":
            return "an " + str
    return "a " + str


def firstS(str, *params):
    str2 = str.split(" ")
    return " ".join([s(str2[0])] + str2[1:])


def s(str, *params):
    if str[-1] in 'shx':
        return str + "es"
    elif str[-1] == 'y':
        if str[-2] not in "aeiou":
            return str[:-1] + "ies"
        else:
            return str + "s"
    else:
        return str + "s"


def ed(str, *params):
    if str[-1] == 'e':
        return str + "d"
    elif str[-1] == 'y':
        if str[-2] not in "aeiou":
            return str[:-1] + "ied"
    else:
        return str + "ed"

base_english = {
    'replace': replace,
    'capitalizeAll': capitalizeAll,
    'capitalize': capitalize_,
    'a': a,
    'firstS': firstS,
    's': s,
    'ed': ed
}
