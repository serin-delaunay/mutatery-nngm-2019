def replace(s, *params):
    return s.replace(params[0], params[1])

def capitalizeAll(s, *params):
    return s.title()

def capitalize_(s, *params):
    return s[0].upper() + s[1:]

def a(s, *params):
    if len(s) > 0:
        if s[0].lower() == 'u':
            if len(s) > 2:
                if s[2].lower() == 'i':
                    return "a " + s
        if s[0].lower() in "aeiou":
            return "an " + s
    return "a " + s

def firstS(s, *params):
    s2 = s.split(" ");
    return " ".join([s(s2[0])] + s2[1:])

def s(s, *params):
    if s[-1] in 'shx':
        return s + "es"
    elif s[-1] == 'y':
        if s[-2] not in "aeiou":
            return s[:-1] + "ies"
        else:
            return s + "s"
    else:
        return s + "s"

def ed(s, *params):
    if s[-1] == 'e':
        return s + "d"
    elif s[-1] == 'y':
        if s[-2] not in "aeiou":
            return s[:-1] + "ied"
    else:
        return s + "ed"

base_english = {
    'replace': replace,
    'capitalizeAll': capitalizeAll,
    'capitalize': capitalize_,
    'a': a,
    'firstS': firstS,
    's': s,
    'ed': ed
}
