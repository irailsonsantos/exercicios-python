a = float(input('a primeira reta mede - '))
b = float(input('a segunda reta mede - '))
c = float(input('a terceira reta mede - '))
#ana1 = a = b and b = c and a = c
#ana2 = a = b and b = c and a != c

if a < b + c and b < a + c and c < a + b :
   print(' estas medidas {}, {}, {} podem formar um triangulo,'.format(a, b, c),end='' )
   if a != b != c != a:
       print(' ESCALENO')
   elif  a == b == c:
       print('EQUILÁTERO')
   else:
       print('ISOSCELES')
else:
   print (' essas medidas não podem formar um triangulo')
