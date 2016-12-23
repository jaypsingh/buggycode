from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(3)

	def tearDown(self):
		self.browser.quit()

	def test_create_a_list(self):
		# Batman wants to create a to do list of manage the villans 
		# of Gotham city. So he goes online
		self.browser.get('http://localhost:8000')

		# He makes sure that the page title  mentions to-do 
		self.assertIn('To-Do',self.browser.title)
		self.fail('Finish The Test !!')

		# He Starts entering his To-Do items.
		# He wants to meet penguin first for some business
		# When he hits enter the page is updated with "meet penguin in his club"
		# He then updates Meet Captain Cool.. now who is this captain cool .. no body knows.
		# Any way his to do list is updated and shows both his appointment.

if __name__=="__main__":
	unittest.main(warnings='ignore')