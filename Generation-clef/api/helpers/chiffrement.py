from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
#https://www.pycryptodome.org/en/latest/src/examples.html#generate-public-key-and-private-key
import hashlib
#https://learntutorials.net/fr/python/topic/2598/securite-et-cryptographie
#utilisation timestamp http://www.python-simple.com/python-modules-autres/date-et-temps.php
import datetime

#Génération d'un couple de clef publique/privée avec RSA
key = RSA.generate(2048)
print(key,end="\n")
print(key.publickey(),end="\n")
private_key = key.export_key()
#print(private_key,end="\n")

#Sauvegarde dans un fichier de la clef privée
file_out = open("private.pem", "wb")
file_out.write(private_key)
file_out.close()

#Sauvegarde dans un fichier de la clef publique
public_key = key.publickey().export_key()
file_out = open("public.pem", "wb")
file_out.write(public_key)
file_out.close()

#Génération d'une empreinte de clé publique
filename = "public.pem"
with open(filename,"rb") as f:
    bytes = f.read() 
    hash = hashlib.sha256(bytes).hexdigest()
    print(hash,end="\n")

#https://pycryptodome.readthedocs.io/en/latest/src/cipher/oaep.html
#Chiffrement message
message = b"Alice paye 500 euros a Bob"
key = RSA.importKey(open("public.pem").read())
cipher = PKCS1_OAEP.new(key)
#conversion du hash pour utiliser encrypt
test=hash.encode('ascii')
#Appel et conversion timestamp
timestamp=datetime.datetime.now().timestamp()
timestamp=(str(timestamp)).encode('ascii')
test2=message+b"\n"+test+b"\n"+timestamp
ciphertext = cipher.encrypt(test2)

#Déchiffrement message
print("Cipher text = ",ciphertext)
key = RSA.importKey(open('private.pem').read())
cipher = PKCS1_OAEP.new(key)
messagefin = cipher.decrypt(ciphertext)
print(messagefin.decode("utf-8"))

#number of seconds since the epoch
#print(datetime.datetime.now().timestamp())
