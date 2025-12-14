a=1
media = 0
par= 0
impar = 0
while(a<=10):
    media = int(input("digite um numero"))
    if(media %2 == 0):
        par=par+media
    else: 
         impar=impar+media
    
    a=a+1
print  ("par", par) 
print("impar", impar)