#password entry

password = "Alpha"
guess = ""
i = 0
guesslimit = False
while guess != password and not (guesslimit):
    if i < 5:
        guess = input("enter password : ")
        i += 1
    else:
        guesslimit = True

if guesslimit:
    print("you have ran out of tries")
else:
    print("you are grented access")


