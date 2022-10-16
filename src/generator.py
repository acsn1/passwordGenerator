import random
characters = "#$%^&*!ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789#$%^&*!"


def generatePassword(length):

    output = ''
    for i in range(length):
        output += characters[random.randint(0, len(characters) -1)]

    print(output)


print('Give me the length of the password you want to be generated: ')
generatePassword(int(input()))

k = input('Type Enter to exit the program.')
k = input('Type Enter to exit the program.')
k = input('Type Enter to confirm the exit from the program.')