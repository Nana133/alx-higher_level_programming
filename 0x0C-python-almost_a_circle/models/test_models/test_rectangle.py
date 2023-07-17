        r1.update(x=1, height=2, y=3, width=4, id=30)
        self.assertEqual(r1.__str__(), "[Rectangle] (30) 1/3 - 4/2")
        r1.update(id=67)
        self.assertEqual(r1.__str__(), "[Rectangle] (67) 1/3 - 4/2")
        r1.update(10, 10, 10, 10, 10, x=1, height=2, y=3, width=4, id=30)
        self.assertEqual(r1.__str__(), "[Rectangle] (10) 10/10 - 10/10")
        r1.update(45, x=1, height=2, y=3, width=4, id=30)
        self.assertEqual(r1.__str__(), "[Rectangle] (45) 10/10 - 10/10")
        r1.update(73, id=30)
        self.assertEqual(r1.__str__(), "[Rectangle] (73) 10/10 - 10/10")
        r1.update(50)
        self.assertEqual(r1.__str__(), "[Rectangle] (50) 10/10 - 10/10")
        r1.update()
        self.assertEqual(r1.__str__(), "[Rectangle] (50) 10/10 - 10/10")

    def test_dictionary_representation(self):
        """Checks to_dictionary method
        """
        r1 = Rectangle(10, 2, 1, 9)
        r1_dictionary = r1.to_dictionary()
        self.assertEqual(r1_dictionary, {'x': 1, 'y': 9, 'id': 1, 'height': 2,
                                         'width': 10})

        r2 = Rectangle(10, 2, 1, 9, 30)
        r2_dictionary = r2.to_dictionary()
        self.assertEqual(r2_dictionary, {'x': 1, 'y': 9, 'id': 30, 'height': 2,
                                         'width': 10})

        r3 = Rectangle(10, 2)
        r3_dictionary = r3.to_dictionary()
        self.assertEqual(r3_dictionary, {'x': 0, 'y': 0, 'id': 2, 'height': 2,
                                         'width': 10})

        r4 = Rectangle(10, 2)
        r4_dictionary = r4.to_dictionary()
        self.assertEqual(r4_dictionary, {'x': 0, 'y': 0, 'id': 3, 'height': 2,
                                         'width': 10})

        r5 = Rectangle(10, 2, 5, 6)
        r5_dictionary = r5.to_dictionary()
        self.assertEqual(r5_dictionary, {'x': 5, 'y': 6, 'id': 4, 'height': 2,
                                         'width': 10})

    def tearDown(self):
        """Tear down test method to reset class attribute
        """
        Base._Base__nb_objects = 0
        try:
            os.remove("Rectangle.json")
        except Exception:
            pass
        try:
            os.remove("Square.json")
        except Exception:
            pass
        try:
            os.remove("Rectangle.csv")
        except Exception:
            pass
        try:
            os.remove("Square.csv")
        except Exception:
            pass

if __name__ == '__main__':
    unittest.main()
