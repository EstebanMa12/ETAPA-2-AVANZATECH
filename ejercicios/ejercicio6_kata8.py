'''
Description:
Replace all vowel to exclamation mark in the sentence. aeiouAEIOU is vowel.

Examples
replace("Hi!") === "H!!"
replace("!Hi! Hi!") === "!H!! H!!"
replace("aeiou") === "!!!!!"
replace("ABCDE") === "!BCD!"
'''

def replace_exclamation(s):
    if len(s) == 0:
        return s
    
    if s[0] in "aeiouAEIOU":
        t = "!"
    else:
        t = s[0]
        
    return t + replace_exclamation(s[1:])