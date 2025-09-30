inteiro = 10
# com virgula = 8.5
# snake_case -> caso cobra
com_virgula = 8.5

# nome = 'Renan'
#camelCase -> 'Renan'
meuNome = 'Renan'

#PascalCase - Caso Pascal (usado para classes(exclusivo))
Carro1 = 'Corola'

print(inteiro, '\n',meuNome)

idade = int( input('Informe sua idade: '))

if idade >= 18:
    print('Maior de idade ')
else :
    print('Menor de idade ')

#descobrir mior numero entre 3

numero1 = int(input('Digite o numero '))
numero2 = int(input('Digite o segundo numero '))
numero3 = int(input('Digite o terceiro numero '))

if numero1 >= numero2 and numero1 >= numero3:
    print('O ', numero1, ' é maior')
elif numero2 >= numero3:
    print('O ', numero2, ' é maior')
else:
    print('O ', numero3, ' é maior')

