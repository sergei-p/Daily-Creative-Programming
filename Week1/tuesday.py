class Encryption:
	def encrypt(self, value: str) -> str:
		encryptedString = ""
		for c in value:
			encryptedString += chr(ord(c) * 2)

		return encryptedString

	def decrypt(self, value: str) -> str:
		decryptedString = ""
		for c in value:
			decryptedString += chr(ord(c) // 2)
		return decryptedString

if __name__ == "__main__":
	valueToEncrypt= input("Enter Value For Encryption: ")
	print("Your Original Value Is: ", valueToEncrypt)
	encrypt1 = Encryption()
	
	cipher = encrypt1.encrypt(valueToEncrypt)
	print("Your Encrypted Value Is: ", end="")
	print(cipher)

	decryptedValue = encrypt1.decrypt(cipher)
	print("Your Decrypted Value Is: ", end="")
	print(decryptedValue)