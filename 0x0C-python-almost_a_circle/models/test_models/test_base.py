        self.assertTrue(type(list_output) == list)

        list_input = []
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_output, [])
        self.assertTrue(type(list_output) == list)

        json_list_input = Rectangle.to_json_string(None)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_output, [])
        self.assertTrue(type(list_output) == list)

    def test_create(self):
        """Checks create method
        """
        # Checks create Rectangle
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual(str(r2), "[Rectangle] (1) 1/0 - 3/5")
        self.assertFalse(r1 is r2)
        self.assertFalse(r1 == r2)

        r1 = Rectangle(3, 5)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual(str(r2), "[Rectangle] (3) 0/0 - 3/5")
        self.assertFalse(r1 is r2)
        self.assertFalse(r1 == r2)

        r1 = Rectangle(3, 5, 3, 4, 89)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual(str(r2), "[Rectangle] (89) 3/4 - 3/5")
        self.assertFalse(r1 is r2)
        self.assertFalse(r1 == r2)

        r1 = Rectangle(3, 5, 3, 4)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual(str(r2), "[Rectangle] (6) 3/4 - 3/5")
        self.assertFalse(r1 is r2)
        self.assertFalse(r1 == r2)

        # Checks for create square
        s1 = Square(3, 5, 1)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertEqual(str(s2), "[Square] (8) 5/1 - 3")
        self.assertFalse(s1 is s2)
        self.assertFalse(s1 == s2)

        s1 = Square(3, 5)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertEqual(str(s2), "[Square] (10) 5/0 - 3")
        self.assertFalse(s1 is s2)
        self.assertFalse(s1 == s2)

        s1 = Square(3, 5, 3, 89)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertEqual(str(s2), "[Square] (89) 5/3 - 3")
        self.assertFalse(s1 is s2)
        self.assertFalse(s1 == s2)

        s1 = Square(50)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertEqual(str(s2), "[Square] (13) 0/0 - 50")
        self.assertFalse(s1 is s2)
        self.assertFalse(s1 == s2)

    def test_load_from_file(self):
        """Checks for load_from_file
        """
        # Check for rectangle load from file
        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(str(list_rectangles_output), "[]")

        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rectangles_input = [r1, r2]
        Rectangle.save_to_file(list_rectangles_input)
        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(str(r1), str(list_rectangles_output[0]))
        self.assertEqual(str(r2), str(list_rectangles_output[1]))

        r1 = Rectangle(10, 50)
        r2 = Rectangle(2, 4, 0, 0, 89)
        list_rectangles_input = [r1, r2]
        Rectangle.save_to_file(list_rectangles_input)
        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(str(r1), str(list_rectangles_output[0]))
        self.assertEqual(str(r2), str(list_rectangles_output[1]))

        r1 = Rectangle(10, 50)
        r2 = Rectangle(2, 4, 0, 0)
        list_rectangles_input = [r1, r2]
        Rectangle.save_to_file(list_rectangles_input)
        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(str(r1), str(list_rectangles_output[0]))
        self.assertEqual(str(r2), str(list_rectangles_output[1]))

        # Check for square load from file
        list_square_output = Square.load_from_file()
        self.assertEqual(str(list_square_output), "[]")

        s1 = Square(10, 7, 2, 8)
        s2 = Square(2, 4)
        list_square_input = [s1, s2]
        Square.save_to_file(list_square_input)
        list_square_output = Square.load_from_file()
        self.assertEqual(str(s1), str(list_square_output[0]))
        self.assertEqual(str(s2), str(list_square_output[1]))

        s1 = Square(10, 50)
        s2 = Square(2, 0, 0, 89)
        list_square_input = [s1, s2]
        Square.save_to_file(list_square_input)
        list_square_output = Square.load_from_file()
        self.assertEqual(str(s1), str(list_square_output[0]))
        self.assertEqual(str(s2), str(list_square_output[1]))

        s1 = Square(10, 50)
        s2 = Square(2, 4, 0, 0)
        list_square_input = [s1, s2]
        Square.save_to_file(list_square_input)
        list_square_output = Square.load_from_file()
        self.assertEqual(str(s1), str(list_square_output[0]))
        self.assertEqual(str(s2), str(list_square_output[1]))

    def test_save_csv(self):
        """Checks save_csv method
        """
        # Checks save to csv file
        Rectangle.save_to_file_csv(None)
        with open("Rectangle.csv", "r") as file:
            self.assertEqual(file.read(), '[]')

        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file_csv([r1, r2])
        sum_expected = sum(list(map(lambda x: ord(x), 'id,width,height,x,y\n'
                                    '1,10,7,2,8\n'
                                    '2,2,4,0,0\n')))
        with open("Rectangle.csv", "r") as file:
            sum_read = sum(list(map(lambda x: ord(x), file.read())))
            self.assertEqual(sum_read, sum_expected)

        r1 = Rectangle(10, 7)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file_csv([r1, r2])
        with open("Rectangle.csv", "r") as file:
            sum_read = sum(list(map(lambda x: ord(x), file.read())))
            sum_expected = sum(list(map(lambda x: ord(x),
                                        'id,width,height,x,y\n'
                                        '3,10,7,0,0\n'
                                        '4,2,4,0,0\n')))
            self.assertEqual(sum_read, sum_expected)

    def test_load_csv(self):
        """Checks load_csv method
        """
        list_rectangles_output = Rectangle.load_from_file_csv()
        self.assertEqual(str(list_rectangles_output), "[]")

        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rectangles_input = [r1, r2]
        Rectangle.save_to_file_csv(list_rectangles_input)
        list_rectangles_output = Rectangle.load_from_file_csv()
        self.assertEqual(str(r1), str(list_rectangles_output[0]))
        self.assertEqual(str(r2), str(list_rectangles_output[1]))

        r1 = Rectangle(10, 50)
        r2 = Rectangle(2, 4, 0, 0, 89)
        list_rectangles_input = [r1, r2]
        Rectangle.save_to_file_csv(list_rectangles_input)
        list_rectangles_output = Rectangle.load_from_file_csv()
        self.assertEqual(str(r1), str(list_rectangles_output[0]))
        self.assertEqual(str(r2), str(list_rectangles_output[1]))

        r1 = Rectangle(10, 50)
        r2 = Rectangle(2, 4, 0, 0)
        list_rectangles_input = [r1, r2]
        Rectangle.save_to_file_csv(list_rectangles_input)
        list_rectangles_output = Rectangle.load_from_file_csv()
        self.assertEqual(str(r1), str(list_rectangles_output[0]))
        self.assertEqual(str(r2), str(list_rectangles_output[1]))

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
