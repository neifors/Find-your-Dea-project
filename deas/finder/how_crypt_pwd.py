import bcrypt


password = b"caca"
pass_hash = bcrypt.hashpw(password, bcrypt.gensalt())
print(pass_hash)

password_a_comprobar= input("\nEscriba su contraseña: ").encode()
veredict = bcrypt.checkpw(password_a_comprobar, pass_hash)
print(veredict)