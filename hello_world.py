# librerias de report
import unittest
from pyunitreport import HTMLTestRunner

# libreria de selenium
from selenium import webdriver


# clase que va 
class HelloWorld(unittest.TestCase) :

    """ va ejecutar todo lo necesaria antes de hacer una prueba".\n
    Va a preparar el entorno de la prueba misma."""
    
    # 5. Hacer para que las pruebas corran en una sola 
    # ventana y no se este cerrando
    # usar @classmetho y reemplazar agregar al nombre del metodo Class y cambiar self por cls, 
    # tambien en el metodo tearDown
    @classmethod
    def setUpClass(cls):
    # def setUp(self) -> None:
        # return super().setUp()
        
        # 1. Lo que se va hacer
        cls.driver = webdriver.Chrome(executable_path= './drivers/chromedriver') # linux
        # self.driver = webdriver.Chrome(executable_path= r'C://Documents/selenium/chromedriver.exe') # windows

        # 2. el navegador va ser driver
        driver = cls.driver

        # 3. decirle al driver que espere implicitamente 10sg antes de realizar la siguiente acción
        driver.implicitly_wait(10)


    """Tests"""

    """caso de prueba, donde se va a realizar el test y unas acciones
    para que el navegador lo automatice"""
    # 4. tests
    def test_hello_world(self):
        driver = self.driver

        # vaya a la pagina
        driver.get('https://www.platzi.com')

    def test_visit_wikipedia(self):
        driver = self.driver
        driver.get('https://www.wikipedia.org')




    """Otras acciones para finalizar"""
    @classmethod
    def tearDownClass(cls):
        # return super().tearDown()
        
        # cerrar las ventanas cuando se hagan las pruebas
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2, testRunner=HTMLTestRunner(output='reportes', report_name='hello-world-report'))