import hashlib

# Arquivo que vai ser comparado
arquivo1 = 'a.txt'
# Arquivo comparador
arquivo2 =  'b.txt'

# Definindo qual algoritmo sera usado para p hash 1 
hash1 = hashlib.new('ripemd160')

# Abrindo o arquivo para leitura binaria 
hash1.update(open(arquivo1, 'rb').read())

# Definindo qual algoritmo sera usado para p hash 1 
hash2 = hashlib.new('ripemd160')

# Abrindo o arquivo para leitura binaria 
hash2.update(open(arquivo2, 'rb').read())

# comparando os arquivos 
if hash1.digest() != hash2.digest():
    print(f"O arquivo: {arquivo1} é diferente do arquivo: {arquivo2}")
    print(f"O hash do arquivo {arquivo1} é: ",hash.hexdigest())
    print(f"O hash do arquivo {arquivo2} é: ",hash.hexdigest())
else:
    print(f"O arquivo {arquivo1} é ingual ao: {arquivo2}")

