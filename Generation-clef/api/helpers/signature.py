from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256
from Crypto.Signature import PKCS1_v1_5

#Génération de la signature
print("Generation")
with open("test.txt", 'rb') as f: data = f.read()
h = SHA256.new(data)
print(h)
with open("private.pem", 'rb') as f: private_key = f.read()
rsa = RSA.importKey(private_key)
print(rsa)
signer = PKCS1_v1_5.new(rsa)
signature = signer.sign(h)
with open("signature.txt", 'wb') as f: f.write(signature)

#Vérification de la signature
print("Verification")
h = SHA256.new(data)
with open("public.pem",'rb') as f: public_key = f.read()
rsa = RSA.importKey(public_key)
signer = PKCS1_v1_5.new(rsa)
with open("signature.txt", 'rb') as f: signature = f.read()
rsp = "Success" if (signer.verify(h, signature)) else " Verification Failure"
print(rsp)