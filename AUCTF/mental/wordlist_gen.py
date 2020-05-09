#!/usr/bin/python3

countries = []
with open('countries.txt', 'r') as fcountries:
    for line in fcountries:
        countries.append(line.strip())

colors = []
with open('colors.txt', 'r') as fcolors:
    for line in fcolors:
        colors.append(line.strip())

fruits = []
with open('fruits.txt', 'r') as ffruits:
    for line in ffruits:
        fruits.append(line.strip())


with open('wordlist.lst', 'w') as wordlist:
    for color in colors:
        for country in countries:
            for fruit in fruits:
                wordlist.write(color+'-'+country+'-'+fruit+'\n')

