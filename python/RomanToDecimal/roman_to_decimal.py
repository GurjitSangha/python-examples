def roman2decimal(roman):
    #dict of decimal system equivalents of roman numerals
    eq={"I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000}

    #checking if the roman numeral string is valid
    if (len(set(roman).intersection(eq.keys())) == 0 or
        len(set(roman).difference(eq.keys())) > 0):
        raise Exception('The entry is not a valid roman numeral')

    i = 0
    dec = 0
    while(i < len(roman)):
        s1 = eq[roman[i]]
        if i+1 < len(roman):
            s2 = eq[roman[i+1]]
            if s1 >= s2:
                dec += s1
                i += 1
            else:
                dec += (s2 - s1)
                i += 2
        else:
            dec += s1
            i += 1
    return dec