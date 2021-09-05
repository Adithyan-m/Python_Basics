'''
vowels get turned into a Z
This means
 cat -> czt
'''


def translate(phrase):
    trans = ""
    for letter in phrase:
        if letter.lower() in "aeiou":        # to avoids seraching A E I O U (covertes letter to lowercase)
            if letter.isupper():
                trans = trans + "z"
            else:
                trans = trans + "z"
        else:
            trans = trans + letter

    return trans

print(translate(input("Enter a phrase to translate: ")))

