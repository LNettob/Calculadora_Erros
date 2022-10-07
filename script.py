//entrada dos numeros onde n é a quantidade de numeros, posteriormente iremos tornar melhor
a = float(input("Digite 1 numero: "))
b = float(input("Digite 2 numero: "))
n = 2

//calculo da media
media = (a+b)/n
print ("aqui sua media: ", media)

//calculo do desvio e do erro estatico
prov0 = (media -a)**2
prov1 = (media -b)**2
desvio = ((prov0+prov1)/(n-1))**(1/2)
erro = desvio / (n**(1/2))

print ("seu desvio:" ,desvio)
print ("seu erro estatico:" ,erro)

//calculo do erro total
erro_t = ((erro**2)+(0.05**2))**(1/2)
print ("seu erro total: ", erro_t)
