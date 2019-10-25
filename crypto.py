from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
import hashlib


def main():
	private_key = generatePK()
	message = b"A message I want to sign"
	signature = createSignature(message,private_key)
	public_key = private_key.public_key()
	verify(message, signature,public_key)

def generatePK():

	return rsa.generate_private_key(
	    public_exponent=65537,
	    key_size=2048,
	    backend=default_backend()
	)

def createSignature(message,private_key):
	return private_key.sign(
	    message,
	    padding.PSS(
	        mgf=padding.MGF1(hashes.SHA256()),
	        salt_length=padding.PSS.MAX_LENGTH
	    ),
	    hashes.SHA256()
	)


def verify(message, signature,public_key):
	
	public_key.verify(
	    signature,
	    message,
	    padding.PSS(
	        mgf=padding.MGF1(hashes.SHA256()),
	        salt_length=padding.PSS.MAX_LENGTH
	    ),
	    hashes.SHA256()
	)

main()