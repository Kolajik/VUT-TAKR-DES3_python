        #Funkce pro prevedeni String objektu na bity
def string2bits(s=''):
    return [bin(ord(x))[2:].zfill(8) for x in s]
        
        #Funkce pro prevedeni bitoveho objektu na String
def bits2string(b=None):
    return ''.join([chr(int(x, 2)) for x in b])