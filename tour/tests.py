from django.test import TestCase,Client

# Create your tests here.

class mytest(TestCase):
	def testmain(self):
		c=Client()
		testlist=['/homepage','/SignUp','/Attraction','/ChosenAttraction/Attraction','/ChosenAttraction','/Profile','/init']

		for onetest in testlist:
			response = c.get(onetest)
			print(onetest,response)
		return response