#ATM machines allow 4 or 6 digit PIN codes and PIN codes cannot contain anything but exactly 4 digits or exactly 6 digits.
#If the function is passed a valid PIN string, return true, else return f alse
def lectura(string,c=0):
    numeros = "1234567890"
    try:
        if string[c] in numeros:
            return lectura(string,c+1)
        else:
            return False
    except IndexError as error:
        return True
        
def validate_pin(pin):
    if len(pin)==4 or len(pin)==6:
        return lectura(pin)