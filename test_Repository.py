import unittest
from product.product import Product
from product.productRepository import create, removeById, getById, getAllProducts


class TestRepository(unittest.TestCase):

   
    def test_create(self):
        product = create("Farinha de trigo", "Anaconda", "2022-03-09", "2023-10-09")
        self.assertIsInstance(product, Product)
        self.assertEqual(product.type, "Farinha de trigo")
        self.assertEqual(product.brand, "Anaconda")
        self.assertEqual(product.dateEntry, "2022-03-09")
        self.assertEqual(product.expirationDate, "2023-10-09")
       

    def test_removeById(self):
        product1 = create("Feijão", "Caldão", "2022-03-09", "2023-12-09")
        self.assertTrue(removeById(product1.id))
        #self.assertFalse(removeById("invalid-id"))
        self.assertIsNone(getById(product1.id))

    def test_getById(self):
        product2 = create("Arroz", "Tio João", "2022-03-09", "2023-11-09")
        self.assertEqual(getById(product2.id), product2)
    
    def test_getById_returnNone_whenIdIsInvalid(self):
        self.assertIsNone(getById("invalid-id"))

    def test_getAllProducts(self):
        listProducts = getAllProducts()

        self.assertEqual(len(listProducts), 2)


if __name__ == '__main__':
    unittest.main()
