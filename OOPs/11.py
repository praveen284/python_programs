class S:
	def __init__(self,name,age):
		self.name=name
		self.age=age

	def show(self):
		print("Name:",self.name)
		print("Age:",self.age)

class J(S):
	def __init__(self,name,age,gender):
		super().__init__(name,age)
		self.gender=gender

	def show(self):
		super().show()
		print("Gender:",self.gender)

class P(S):
	def __init__(self,name,age,gender):
		super().__init__(name,age)
		self.gender=gender

	def show(self):
		super().show()
		print("Gender:",self.gender)

class R(S):
	def __init__(self,name,age,relation):
		super().__init__(name,age)
		self.relation=relation

	def show(self):
		super().show()
		print("Relation:",self.relation)

p=P("Praveen",21,"M")
j=J("Jayasree",21,"F")
r=R("Praveen-Jayasree",21,"Love")
p.show()
print("<<<------------>>>")
j.show()
print("<<<------------>>>")
r.show()