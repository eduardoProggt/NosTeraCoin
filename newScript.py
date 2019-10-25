import hashlib

class Owner:

	def __init__(self, name,bc):
		self.money = 0.0
		self.pseudonym = ""
		self.pseudonym = name
		#designtechnisch schwierig:
		self.blockchain = bc

	def spent(self, amount, consumer):
		if self.money > amount:
			self.money -= amount
			consumer.earn(amount)
			message = self.pseudonym + " gibt "+consumer.pseudonym +" "+str(amount)+" Coins."
			self.blockchain.addMessage(message)
	
	def earn(self, amount):
		self.money += amount

	def tell(self):
		print(self.pseudonym + " owns " + str(self.money) + " Coins.")
class Hasher:
	def hashMessage(msg):
		return hashlib.sha256(bytes(msg, 'utf-8')).hexdigest()

class Blockchain:
	def __init__(self):
		self.blocks = []
	def addMessage(self,newMessage):
		hashedMessage = Hasher.hashMessage(self.getLastHash()+newMessage)
		block = Block(newMessage,hashedMessage)
		self.blocks.append(block)
	def print(self):
		for block in self.blocks:
			print(block.toString())
	def getLastHash(self):
		if len(self.blocks) ==0:
			return ""
		return self.blocks[-1].hashOld


class Block:
	def __init__(self, message, hashOld):
		self.message = message
		self.hashOld = hashOld
	def toString(self):
		emptyspace = self.createEmptySpaceString(self.message)
		string = "--------------------------------||--------------------------------\n"
		string += "|"+self.message+emptyspace + "|\n|" + self.hashOld+"|"
		string += "\n--------------------------------||--------------------------------"
		return string
	def createEmptySpaceString(self,message):
		leerspaces = 64 - len(message)
		ret = ""
		for letter in range(0,leerspaces):
			ret+=" "
		return ret
myBlockChain = Blockchain()
nutzer1 = Owner("Andreas",myBlockChain)
nutzer2 = Owner("Britta",myBlockChain)

nutzer1.money = 10.0

nutzer1.tell()
nutzer1.spent(5.5,nutzer2)
nutzer1.spent(3.0,nutzer2)
nutzer2.spent(7.9,nutzer1)
nutzer1.spent(5.5,nutzer2)

myBlockChain.print()
nutzer1.tell()
nutzer2.tell()




