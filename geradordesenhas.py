import hashlib
import random
input ("Pressione enter para iniciar o programa ")
print ("A senha gerada foi: ")
def senha(length):
    caracteres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+-=[]{}|;:,.<>?"
    random_string = "".join(random.choice(caracteres) for i in range(length))
    hash_object = hashlib.sha256(random_string.encode("utf-8"))
    password_hash = hash_object.hexdigest()
    return password_hash[:6]
password = senha(6)
print(password)
input ("Pressione enter para sair do programa")

