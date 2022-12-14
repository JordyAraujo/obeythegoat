from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
import time

MAX_WAIT = 10

class NewVisitorTest(LiveServerTestCase):
    
    def setUp(self):
        # O usuário abre o navegador
        self.browser = webdriver.Firefox()


    def tearDown(self):
        # O usuário fecha o navegador
        return self.browser.quit()


    def wait_for_row_in_list_table(self, row_text):
        start_time = time.time()
        while True:
            try:
                table = self.browser.find_element(By.ID, 'id_list_table')
                rows = table.find_elements(By.TAG_NAME, 'tr')
                self.assertIn(row_text, [row.text for row in rows])
                return
            except (AssertionError, WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
                time.sleep(0.5)


    def test_can_start_a_list_and_retrieve_it_later(self):
        # O usuário acessa a aplicação
        self.browser.get(self.live_server_url)

        # Confere o título e o cabeçalho da página
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element(By.TAG_NAME, 'h1').text
        self.assertIn('To-Do', header_text)

        # Existe uma caixa de texto para adicionar um item à lista
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

        self.wait_for_row_in_list_table('1: Buy peacock feathers')

        # Ainda há uma caixa de texto para adicionar um item à lista
        inputbox = self.browser.find_element(By.ID, 'id_new_item')
        # Ela adiciona mais um item
        inputbox.send_keys('Use peacock feathers to make a fly')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        # A página atualiza novamente, agora mostrando os dois itens
        self.wait_for_row_in_list_table('1: Buy peacock feathers')
        self.wait_for_row_in_list_table('2: Use peacock feathers to make a fly')

        self.fail('Finish the test!')