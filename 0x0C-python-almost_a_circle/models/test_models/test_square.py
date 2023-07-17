        s1.update(10)
        self.assertEqual(s1.__str__(), "[Square] (10) 0/0 - 5")
        s1.update(1, 2)
        self.assertEqual(s1.__str__(), "[Square] (1) 0/0 - 2")
        s1.update(1, 2, 3)
        self.assertEqual(s1.__str__(), "[Square] (1) 3/0 - 2")
        s1.update(1, 2, 3, 4)
        self.assertEqual(s1.__str__(), "[Square] (1) 3/4 - 2")
        s1.update(x=12)
        self.assertEqual(s1.__str__(), "[Square] (1) 12/4 - 2")
        s1.update(size=7, y=1)
        self.assertEqual(s1.__str__(), "[Square] (1) 12/1 - 7")
        s1.update(size=7, id=89, y=1)
        self.assertEqual(s1.__str__(), "[Square] (89) 12/1 - 7")
        s1.update(10, 10, 10, 10, x=1, size=2, y=3, id=30)
        self.assertEqual(s1.__str__(), "[Square] (10) 10/10 - 10")
        s1.update(73, id=30)
        self.assertEqual(s1.__str__(), "[Square] (73) 10/10 - 10")
        s1.update(50)
        self.assertEqual(s1.__str__(), "[Square] (50) 10/10 - 10")

    def test_dictionary_representation(self):
        """Check to_dictionary method
        """
        s1 = Square(10, 2, 1)
        s1_dictionary = s1.to_dictionary()
        self.assertEqual(s1_dictionary, {'x': 2, 'y': 1, 'id': 1, 'size': 10})

        s2 = Square(1, 1)
        s2_dictionary = s2.to_dictionary()
        self.assertEqual(s2_dictionary, {'x': 1, 'y': 0, 'id': 2, 'size': 1})

        s3 = Square(10, 0, 2)
        s3_dictionary = s3.to_dictionary()
        self.assertEqual(s3_dictionary, {'x': 0, 'y': 2, 'id': 3, 'size': 10})

        s4 = Square(10)
        s4_dictionary = s4.to_dictionary()
        self.assertEqual(s4_dictionary, {'x': 0, 'y': 0, 'id': 4, 'size': 10})

        s5 = Square(10, 2, 5, 6)
        s5_dictionary = s5.to_dictionary()
        self.assertEqual(s5_dictionary, {'x': 2, 'y': 5, 'id': 6, 'size': 10})

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
