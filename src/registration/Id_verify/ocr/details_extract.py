from __future__ import print_function
import re

class DetailsExtracter:
	def __init__(self):

		self.name = []
		self.email = []
		self.phone = [] 
		self.date = []
		self.college = []
		self.address = []

		self.flag = 0
		self.count = 0
	
	def reset(self):

		self.name = []
		self.email = []
		self.phone = [] 
		self.date = []
		self.college = []
		self.address = []

		self.flag = 0
		self.count = 0

	def arr2str(self, arr):
		string = ''
		for element in arr:
			string = string + ' ' + element
		return string.strip()

	def extractName(self, words, line):
		"""
		Get Name from extracted text
		"""
		for word in ['name','name:']:
			if word in words:
				_name = line.replace(word,'')
				_name = _name.rstrip()
				_name = _name.lstrip()
				_name = _name.replace("8", "B")
				_name = _name.replace("0", "D")
				_name = _name.replace("6", "G")
				_name = _name.replace("1", "I")
				_name = re.sub('[^a-zA-Z] +', ' ', _name)
				self.name.append(_name.upper())

	def extractSchool(self, words, line):
		for word in ['college', 'institute', 'school', 'vidyalaya' , 'university', 'academy']:
			if word in words:
				_college = line.rstrip()
				_college = _college.lstrip()
				_college = _college.replace("8", "B")
				_college = _college.replace("0", "D")
				_college = _college.replace("6", "G")
				_college = _college.replace("1", "I")
				_college = re.sub('[^a-zA-Z] +', ' ', _college)
				self.college.append(_college)

	def extractEmail(self, words):
		for word in words:
			_email = re.findall(r'[\w\.-]+@[\w\.-]+',word)
			self.email = list(set(self.email + _email))

	def extractPhone(self, words):
		for word in words:
			phone_search = re.search(r'((\+*)((0[ -]+)*|(91 )*)(\d{12}|\d{10})| )|\d{5}([- ]*)\d{6}',word)
			if phone_search is not None:
				_phone = word.rstrip()
				_phone = _phone.lstrip()
				_phone = _phone.replace(" ", "")
				self.phone.append(_phone)

	def extractDateOfBirth(self, words):
		for word in words:
			dob_search = re.search('(\d{2})[/.-](\d{2})[/.-](\d{4})$', word)
			if dob_search is not None:
				dob = word.rstrip()
				dob = dob.lstrip()
				dob = dob.replace('l', '/')
				dob = dob.replace('L', '/')
				dob = dob.replace('I', '/')
				dob = dob.replace('i', '/')
				dob = dob.replace('|', '/')
				dob = dob.replace('\"', '/1')
				dob = dob.replace(" ", "")
				self.date.append(dob)

	def extractAddress(self, words, line):

		add = ['address', 'add', 'add.','address:', 'add:', 'add.:']

		for word in words:
						
			for word in add:
				if word in words:
					self.flag = 1

			if self.flag==1:
				self.count += 1
				self.address.append(line)

			if self.count == 3:
				self.flag = 0


	def extractDetails(self, text):

		for line in text:

			temp = line.lower()

			wordss = temp.split(' ')

			words = []

			for word in wordss:
				word = word.replace(';',':')
				words.append(word)
			
			self.extractName(words, line.lower())
			self.extractSchool(words)
			self.extractPhone(words)
			self.extractEmail(words)
			self.extractDateOfBirth(words)
			self.extractAddress(words)

		data = {}
		data['name']    = self.arr2str(self.name) 
		data['college'] = self.arr2str(self.college)
		data['dates']   = self.arr2str(self.date)
		data['emails']  = self.arr2str(self.email)
		data['phones']  = self.arr2str(self.phone)
		data['address'] = self.arr2str(self.address)
		return data
