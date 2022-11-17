from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
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

        # Confere o título e o cabeçalho da página
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element(By.TAG_NAME, 'h1').text
        self.assertIn('To-Do', header_text)

        # Ela é convidada a adicionar um item à lista
        inputbox = self.browser.find_element(By.ID, 'id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # Ela adiciona "Comprar penas de pavão" a uma caixa de texto
        inputbox.send_keys('Buy peacock feathers')

        # Quando ela pressiona Enter, a página atualiza, agora listando
        # "1: Buy peacock feathers"
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        table = self.browser.find_element(By.ID, 'id_list_table')
        rows = table.find_elements(By.TAG_NAME, 'tr')
        self.assertTrue(
            any(row.text == '1: Buy peacock feathers' for row in rows),
            "New to-do item did not appear in table"
        )

        self.fail('Finish the test!')

if __name__ == '__main__':
    unittest.main()