'''
Create a function called shortcut to remove the lowercase vowels (a, e, i, o, u ) in a given string.

Examples
"hello"     -->  "hll"
"codewars"  -->  "cdwrs"
"goodbye"   -->  "gdby"
"HELLO"     -->  "HELLO"
'''

#Solución normal -> con ciclo for

#Solución con recursividad
def shortcut(s):
    if len(s) == 0:
        return s
    elif s[0] in "aeiou":
        return shortcut(s[1:])
    else:
        return s[0] + shortcut(s[1:])