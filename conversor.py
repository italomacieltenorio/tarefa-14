def conversor(i):
  arq = open('conversor', 'a')
  m1 = i * 0.39
  arq.write(f'o valor{i} em centímentros corresponde a {m1} valor em polegadas')
  arq.close()