import unittest
from app.app import translate

class TranslatorTestCase(unittest.TestCase):
    def test_translation(self):
        result = translate("Hello, world!")
        self.assertEqual(result, "¡Hola, mundo!")

if __name__ == '__main__':
    unittest.main()
