def greet(fname, lname, sex, age):
    return "\nHello, {:s} {:s}! You are a {:s} year old {:s}.\n"\
        .format(fname.capitalize(), lname.capitalize(), age, sex.lower())