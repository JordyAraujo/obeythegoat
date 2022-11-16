from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
    
    def setUp(self):
        # O usuário abre o navegador
        self.browser = webdriver.Firefox()

    def tearDown(self):
        # O usuário fecha o navegador
        return self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # O usuário acessa a aplicação
        self.browser.get('http://localhost:8000')

        # Confere o título da página
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')

if __name__ == '__main__':
    unittest.main()