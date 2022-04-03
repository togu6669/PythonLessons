x = input('Podaj pierwsza liczbe w ciagu od 1 do 100').split()
y = input('Podaj ostatnia liczbe w ciagu od 1 do 100').split()

i = 0
print ('Kolejne sumy liczb w ciagu ', x, y)
for n in range (y-x):
    i = i + n
    print (i)


