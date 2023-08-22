c= 0
sexo=''
while c == 0:
    sexo = str(input('Qual seu sexo?'))
    if sexo == 'm' or sexo == 'f':
        c += 1
print(f'você digitou {sexo}')
