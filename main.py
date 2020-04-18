import local as lc
film_1 = ''
film_2 = ''
name_1 = ''
name_2 = ''
d = {}
d1 = {}
d2 = {}
d3 = {}
d4 = {}
d5 = {}
d6 = {}
s = list()
def slovar(film_1, film_2):
    if film_1 in d:
        key = film_1
        value = d[film_1]
        d2[key] = value

    if film_2 in d:
        key = film_2
        value = d[film_2]
        d2[key] = value

    for keys in d2:
        c = d2[keys]
        for i in c:
            key = i
            value = keys
            if key in d3:
                d3[key].append(value)
            else:
                d3[key] = []
                d3[key].append(value)

def slovar2(name_1, name_2):
    if name_1 in d1:
        key = name_1
        value = d1[name_1]
        d6[key] = value

    if name_2 in d1:
        key = name_2
        value = d1[name_2]
        d6[key] = value

    for keys in d6:
        c = d6[keys]
        for i in c:
            key = i
            value = keys
            if key in d5:
                d5[key].append(value)
            else:
                d5[key] = []
                d5[key].append(value)


with open('input.txt') as inp_file:
    for line in inp_file.readlines():
        line = line[:-1]
        delen = line.find(':')
        s1 = line[delen + 2:]
        s = s1.split(', ')
        key = line[:delen]
        values = s[:]
        d[key] = values

for keys in d:
    c = d[keys]
    for i in c:
        key = i
        value = keys
        if key in d1:
            d1[key].append(value)
        else:
            d1[key] = []
            d1[key].append(value)

number = int(input(lc.MENU1))

while number != 3:
    if number == 1:
        num = 0
        print(lc.ALLSPISOK2)
        for key in d:
            num += 1
            print(num, '-', key)

        film_1 = input(lc.FILM1)
        film_2 = input(lc.FILM2)
        number_2 = int(input(lc.MENU11))
        slovar(film_1, film_2)

        if number_2 == 1:
            for i in d3:
                print(i)

        elif number_2 == 2:
            for i in d3:
                if len(d3[i]) == 2:
                    print(i)

        elif number_2 == 3:
            for i in d3:
                r = []
                r.append(film_1)
                if d3[i] == r:
                    print(i)


    elif number == 2:
        num = 0
        print(lc.ALLSPISOK)
        for key in d1:
            num += 1
            print(num, '-', key)

        name_1 = input(lc.NAME1)
        name_2 = input(lc.NAME2)
        number_2 = int(input(lc.MENU12))

        for i in d1:
            t = i.split()
            key = t[-1]
            value = i
            d4[key] = value

        name_1 = d4[name_1]
        name_2 = d4[name_2]
        slovar2(name_1,name_2)

        if number_2 == 1:
            for i in d5:
                print(i)
        elif number_2 == 2:
            for i in d5:
                if len(d5[i]) == 2:
                    print(i)
        elif number_2 == 3:
            for i in d5:
                r = []
                r.append(name_1)
                if d5[i] == r:
                    print(i)

    number = int(input(lc.MENU1))
    d2.clear()
    d3.clear()
    d5.clear()
    d6.clear()
print(lc.END)



