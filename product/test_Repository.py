import unittest
from product.product import Product
from productRepository import create, removeById, getById, getAllProducts


class TestRepository(unittest.TestCase):

    def setUp(self):
        self.product1 = create("Feijão", "Caldão", "2022-03-09", "2023-12-09")
        self.product2 = create("Arroz", "Tio João", "2022-03-09", "2023-11-09")

    def test_create(self):
        product = create("Farinha de trigo", "Anaconda", "2022-03-09", "2023-10-09")
        self.assertIsInstance(product, Product)
        self.assertEqual(product.type, "Farinha de trigo")
        self.assertEqual(product.brand, "Anaconda")
        self.assertEqual(product.dateEntry, "2022-03-09")
        self.assertEqual(product.expirationDate, "2023-10-09")
        self.assertIn(product, getAllProducts())

    def test_removeById(self):
        self.assertTrue(removeById(self.product1.id))
        self.assertFalse(removeById("invalid-id"))
        self.assertNotIn(self.product1, getAllProducts())

    def test_getById(self):
        self.assertEqual(getById(self.product2.id), self.product2)
        self.assertIsNone(getById("invalid-id"))

    def test_getAllProducts(self):
        self.assertEqual(getAllProducts(), [self.product1, self.product2])


if __name__ == '__main__':
    unittest.main()
