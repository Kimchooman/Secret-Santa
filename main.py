import random
import smtplib

def intitialize_server(user,password,obj):
	obj.starttls()
	obj.login(user,password)


class person:

	def __init__(self,name, email):

		self.name = name
		
		self.match = None

		self.email = email

class name_matcher:

	def __init__(self, person_ar, usr, passw):

		self.ar = person_ar

		self.server = smtplib.SMTP("smtp.gmail.com:587")

		self.user = usr
		
		intitialize_server(usr, passw, self.server)

		self.shuffled_ar = self.ar.copy()

		random.shuffle(self.shuffled_ar)

		for i in range(len(self.ar)):

			self.ar[i].match = self.shuffled_ar[i]

	def send_mail(self, person):

		self.server.sendmail(self.user, self.user, f"Hello, you partner for secret santa 2020 {person.name}.")
	
ar = [
	person("Ryan", "--------------------"),
	person("Jeffery", "-----------------"),
	person("RJ", "------------------------"),
	person("Sarah", "----------------------"),
	person("Danah", "-----------------------"),
	person("Caroline", "---------------------"),
	person("Matthew", "----------------------")
]

username = "-----------------"
password = "------------"

matcher = name_matcher(ar, username, password)

for person in matcher.ar:

	matcher.send_mail(person)
