import random
import os
import time

remax = """

██████╗░███████╗███╗░░░███╗░█████╗░██╗░░██╗  ░██████╗░██╗░░██╗
██╔══██╗██╔════╝████╗░████║██╔══██╗╚██╗██╔╝  ██╔════╝░██║░░██║
██████╔╝█████╗░░██╔████╔██║███████║░╚███╔╝░  ██║░░██╗░███████║
██╔══██╗██╔══╝░░██║╚██╔╝██║██╔══██║░██╔██╗░  ██║░░╚██╗██╔══██║
██║░░██║███████╗██║░╚═╝░██║██║░░██║██╔╝╚██╗  ╚██████╔╝██║░░██║
╚═╝░░╚═╝╚══════╝╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝  ░╚═════╝░╚═╝░░╚═╝

            Remax Alghmadi - insta : @ 0637871936 .
            
"""

print(remax)
time.sleep(3)
print("\n")
print("")
print("Coded By # Remax Alghamdi . ")
print("")
print("Choose 1 For random users without domain")
print("Choose 2 for random users with random domains ")
print("Choose 3 for random users with domain of your choice")
print("\n")

Keywords = open("names/names.txt", 'r').read().splitlines()
domains = open("domains/domains.txt", 'r').read().splitlines()
default = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
save = open('list.txt', 'a')
mode = input("Enter the mode of list : ")


def mode1():
    mode1_length = input('length: ')
    mode1_count = input('count: ')
    if mode1_length == '1':
        for i in range(0, int(mode1_count)):
            save.write(random.choice(Keywords)+random.choice(default)+'\n')
            print('status: ' + str(i+1))
    elif mode1_length == '2':
        for i in range(0, int(mode1_count)):
            save.write(random.choice(Keywords) +
                        random.choice(default)+random.choice(default)+'\n')
            print('status: ' + str(i+1))
    elif mode1_length == '3':
        for i in range(0, int(mode1_count)):
            save.write(random.choice(Keywords)+random.choice(default) +
                        random.choice(default)+random.choice(default)+'\n')
            print('status: ' + str(i+1))
    elif mode1_length == '4':
        for i in range(0, int(mode1_count)):
            save.write(random.choice(Keywords)+random.choice(default) +
                        random.choice(default)+random.choice(default)+random.choice(default)+'\n')
            print('status: ' + str(i+1))
    elif mode1_length == '5':
        for i in range(0, int(mode1_count)):
            save.write(random.choice(Keywords)+random.choice(default)+random.choice(default) +
                        random.choice(default)+random.choice(default)+random.choice(default)+'\n')
            print('status: ' + str(i+1))
    elif mode1_length == '6':
        for i in range(0, int(mode1_count)):
            save.write(random.choice(Keywords)+random.choice(default)+random.choice(default)+random.choice(
                default)+random.choice(default)+random.choice(default)+random.choice(default)+'\n')
            print('status: ' + str(i+1))
    elif mode1_length == '7':
        for i in range(0, int(mode1_count)):
            save.write(random.choice(Keywords)+random.choice(default)+random.choice(default)+random.choice(default) +
                        random.choice(default)+random.choice(default)+random.choice(default)+random.choice(default)+'\n')
            print('status: ' + str(i+1))
    elif mode1_length == '8':
        for i in range(0, int(mode1_count)):
            save.write(random.choice(Keywords)+random.choice(default)+random.choice(default)+random.choice(default)+random.choice(
                default)+random.choice(default)+random.choice(default)+random.choice(default)+random.choice(default)+'\n')
            print('status: ' + str(i+1))

def mode2():
    mode1_length = input('length: ')
    mode1_count = input('count: ')
    if mode1_length == '1':
        for i in range(0, int(mode1_count)):
            save.write(random.choice(Keywords)+random.choice(default)+"@"+random.choice(domains)+'\n')
            print('status: ' + str(i+1))
    elif mode1_length == '2':
        for i in range(0, int(mode1_count)):
            save.write(random.choice(Keywords) +
                        random.choice(default)+random.choice(default)+"@"+random.choice(domains)+'\n')
            print('status: ' + str(i+1))
    elif mode1_length == '3':
        for i in range(0, int(mode1_count)):
            save.write(random.choice(Keywords)+random.choice(default) +
                        random.choice(default)+random.choice(default)+"@"+random.choice(domains)+'\n')
            print('status: ' + str(i+1))
    elif mode1_length == '4':
        for i in range(0, int(mode1_count)):
            save.write(random.choice(Keywords)+random.choice(default) +
                        random.choice(default)+random.choice(default)+random.choice(default)+"@"+random.choice(domains)+'\n')
            print('status: ' + str(i+1))
    elif mode1_length == '5':
        for i in range(0, int(mode1_count)):
            save.write(random.choice(Keywords)+random.choice(default)+random.choice(default) +
                        random.choice(default)+random.choice(default)+random.choice(default)+"@"+random.choice(domains)+'\n')
            print('status: ' + str(i+1))
    elif mode1_length == '6':
        for i in range(0, int(mode1_count)):
            save.write(random.choice(Keywords)+random.choice(default)+random.choice(default)+random.choice(
                default)+random.choice(default)+random.choice(default)+random.choice(default)+"@"+random.choice(domains)+'\n')
            print('status: ' + str(i+1))
    elif mode1_length == '7':
        for i in range(0, int(mode1_count)):
            save.write(random.choice(Keywords)+random.choice(default)+random.choice(default)+random.choice(default) +
                        random.choice(default)+random.choice(default)+random.choice(default)+random.choice(default)+"@"+random.choice(domains)+'\n')
            print('status: ' + str(i+1))
    elif mode1_length == '8':
        for i in range(0, int(mode1_count)):
            save.write(random.choice(Keywords)+random.choice(default)+random.choice(default)+random.choice(default)+random.choice(
                default)+random.choice(default)+random.choice(default)+random.choice(default)+random.choice(default)+"@"+random.choice(domains)+'\n')
            print('status: ' + str(i+1))

def mode3():
    domain = str(input("Your domain (Example : gmail.com) : "))
    mode1_length = input('length: ')
    mode1_count = input('count: ')
    if mode1_length == '1':
        for i in range(0, int(mode1_count)):
            save.write(random.choice(Keywords)+random.choice(default)+"@"+domain+'\n')
            print('status: ' + str(i+1))
    elif mode1_length == '2':
        for i in range(0, int(mode1_count)):
            save.write(random.choice(Keywords) +
                        random.choice(default)+random.choice(default)+"@"+domain+'\n')
            print('status: ' + str(i+1))
    elif mode1_length == '3':
        for i in range(0, int(mode1_count)):
            save.write(random.choice(Keywords)+random.choice(default) +
                        random.choice(default)+random.choice(default)+"@"+domain+'\n')
            print('status: ' + str(i+1))
    elif mode1_length == '4':
        for i in range(0, int(mode1_count)):
            save.write(random.choice(Keywords)+random.choice(default) +
                        random.choice(default)+random.choice(default)+random.choice(default)+"@"+domain+'\n')
            print('status: ' + str(i+1))
    elif mode1_length == '5':
        for i in range(0, int(mode1_count)):
            save.write(random.choice(Keywords)+random.choice(default)+random.choice(default) +
                        random.choice(default)+random.choice(default)+random.choice(default)+"@"+domain+'\n')
            print('status: ' + str(i+1))
    elif mode1_length == '6':
        for i in range(0, int(mode1_count)):
            save.write(random.choice(Keywords)+random.choice(default)+random.choice(default)+random.choice(
                default)+random.choice(default)+random.choice(default)+random.choice(default)+"@"+domain+'\n')
            print('status: ' + str(i+1))
    elif mode1_length == '7':
        for i in range(0, int(mode1_count)):
            save.write(random.choice(Keywords)+random.choice(default)+random.choice(default)+random.choice(default) +
                        random.choice(default)+random.choice(default)+random.choice(default)+random.choice(default)+"@"+domain+'\n')
            print('status: ' + str(i+1))
    elif mode1_length == '8':
        for i in range(0, int(mode1_count)):
            save.write(random.choice(Keywords)+random.choice(default)+random.choice(default)+random.choice(default)+random.choice(
                default)+random.choice(default)+random.choice(default)+random.choice(default)+random.choice(default)+"@"+domain+'\n')
            print('status: ' + str(i+1))

if mode == '1':
    mode1()
elif mode == '2':
    mode2()
elif mode == '3':
    mode3()
else:
    print("Error!")

print('')
input("press enter to close the program.")