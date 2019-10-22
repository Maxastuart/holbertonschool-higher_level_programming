#!/usr/bin/python3
""" Unittest for 0x0C-python-almost_a_circle Rectangle class
"""
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """ Tests the Rectangle class's methods and attributes. """

    @classmethod
    def setUpClass(cls):
        cls.r1 = Rectangle(1, 1)
        cls.r2 = Rectangle(2, 2, 0, 0)
        cls.r200 = Rectangle(20, 10, id=200)
        cls.r201 = Rectangle(20, 10, 1, 1)

    def test_init(self):
        with self.assertRaises(TypeError):
            Rectangle()
        with self.assertRaises(TypeError):
            Rectangle(21)
        with self.assertRaises(TypeError):
            Rectangle(-3)
        with self.assertRaises(TypeError):
            Rectangle(0)
        with self.assertRaises(ValueError):
            Rectangle(1, 0)
        with self.assertRaises(ValueError):
            Rectangle(-1, 1)
        with self.assertRaises(ValueError):
            Rectangle(1, -1, 1, 1)
        with self.assertRaises(ValueError):
            Rectangle(1, 1, -1, 1)
        with self.assertRaises(ValueError):
            Rectangle(1, 1, 1, -1)

    def test_id(self):
        self.assertEqual(self.r1.id, 1)
        self.assertEqual(self.r2.id, 2)
        self.assertEqual(self.r200.id, 200)
        self.assertEqual(self.r201.id, 3)
        self.assertEqual(Rectangle._Base__nb_objects, 3)

    def test__str__(self):
        self.assertEqual(str(self.r1), "[Rectangle] (1) 0/0 - 1/1")
        self.assertEqual(str(self.r200), "[Rectangle] (200) 0/0 - 20/10")
        self.assertEqual(str(self.r201), "[Rectangle] (3) 1/1 - 20/10")

    def test_properties(self):
        self.assertEqual(self.r1.width, 1)
        self.assertEqual(self.r1.height, 1)
        self.assertEqual(self.r1.x, 0)
        self.assertEqual(self.r1.y, 0)
        self.assertEqual(self.r201.width, 20)
        self.assertEqual(self.r201.height, 10)
        self.assertEqual(self.r201.x, 1)
        self.assertEqual(self.r201.y, 1)

    def test_setters(self):
        with self.assertRaises(TypeError):
            self.r2.width = '1'
        with self.assertRaises(TypeError):
            self.r2.width = [1, 2]
        with self.assertRaises(TypeError):
            self.r2.width = {1, 2}
        with self.assertRaises(TypeError):
            self.r2.width = {1: 2}
        with self.assertRaises(TypeError):
            self.r2.width = 1, 2
        with self.assertRaises(TypeError):
            self.r2.width = True
        with self.assertRaises(ValueError):
            self.r2.width = -5
        self.r2.width = 5
        self.assertEqual(self.r2.width, 5)

    """
        (width, 
         height,
         x,
         y)

        test_area(self)
        test_display(self)
        test_update(self)
        test_to_dictionary(self)
"""

    def test_to_json_string(self):
        self.assertEqual(Rectangle.to_json_string(None), "[]")
        self.assertEqual(Rectangle.to_json_string([]), "[]")
        self.assertEqual(Rectangle.to_json_string([{}]), "[{}]")
        self.assertEqual(Rectangle.to_json_string([{}, {}]), "[{}, {}]")

    def test_from_json_string(self):
        self.assertEqual(Rectangle.from_json_string(None), [])
        self.assertEqual(Rectangle.from_json_string(""), [])
        self.assertEqual(Rectangle.from_json_string("[]"), [])
        self.assertEqual(Rectangle.from_json_string("[{}]"), [{}])
        self.assertEqual(Rectangle.from_json_string("[{}, {}]"), [{}, {}])

    def test_save_to_file(self):
        with self.assertRaises(TypeError):
            Rectangle.save_to_file()

    """
    def test_create(self):
        with self.assertRaises(TypeError):
            Rectangle.create()
    

    def test_load_from_file(self):
        with self.assertRaises(FileNotFoundError):
            Rectangle.load_from_file()
"""

if __name__ == "__main__":
    unittest.main()
