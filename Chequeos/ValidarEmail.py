import re


def Email(email):

    regex = '^[a-zA-Z0-9]+[\._]?[a-zA-Z0-9]+[@]\w+[.]\w{2,3}$'

    if(re.search(regex,email)):
        return email

    else:
        return False


