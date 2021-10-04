# '''
# Returneaza true daca n este prim si false daca nu.
# '''
def is_prime(n):
  i = 2
  prim = True
  while i*i < n and prim:
    if n % i == 0:
      prim = False
    i+=1
  if n == 1:
    return False
  return prim
# # '''
# # Returneaza produsul numerelor din lista lst.
# # '''
def get_product(lst):
  produs = 1
  for numar in lst:
    produs *= numar
  return produs

# # '''
# # Returneaza CMMDC a doua numere x si y folosind primul algoritm.
# # '''
def get_cmmdc_v1(x, y):
  if x < y:
    c = x
    x = y
    y = c
  while(y != 0):
    c = x % y
    x = y
    y = c
  return x
  
def get_cmmdc_v2(x, y):
  if x < y:
    c = x
    x = y
    y = c
  while x != y:
    if(x > y):
      x -= y
    else:
      y -= x
  return x
  
def main():
  print('1. Verifica daca un numar dat este prim')
  print('2. Calculeaza produsul mai multor numere naturale')
  print('3. Calculeaza cmmdc a doua numere utilizand algoritmul lui Euclid')
  print('4. Calculeaza cmmdc a doua numere utilizand metoda scaderilor repetate')
  print('x. paraseste aplicatia')
  ex = input("Alegeti exercitiul dorit: ")
  while ex != 'x':
    if ex == '1':
      numar = input("Dorim sa verificam daca numarul urmator este prim: ")
      if is_prime(int(numar)):
        negatie = ""
      else:
        negatie = "nu "
      print("Numarul " , numar , negatie , "este prim")
    elif ex == '2':
      numar_de_numere = int(input("Numarul de numere din lista: "))
      lista_de_numere = []
      print("Numerele sunt: ")
      for numar_din_lista in range(0,numar_de_numere):
        element = int(input())
        lista_de_numere.append(element)
      print('Produsul numerelor date este: ' , get_product(lista_de_numere))
    elif ex == '3':
      print('Introduceti cele doua numere:')
      a = int(input('Primul numar:'))
      b = int(input('Al doilea numar:'))
      print(f'Cmmdc al numerelor {a} si {b} este ' ,get_cmmdc_v1(a,b))
    elif ex == '4':
      print('Introduceti cele doua numere:')
      a = int(input('Primul numar:'))
      b = int(input('Al doilea numar:'))
      print(f'Cmmdc al numerelor {a} si {b} este ' ,get_cmmdc_v2(a,b))
    else:
      print ('Va rugam introduceti un exercitiu valid')
    ex = input("Alegeti exercitiul dorit: ")

if __name__ == '__main__':
  main()
