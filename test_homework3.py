import unittest
from homework3 import create_dataframe

class CreateDataframeTest(unittest.TestCase):

    def test_column_names(self):
        df = create_dataframe("class.db")
        self.assertEqual(set(df.columns), set(["video_id", "category_id", "language"]))

    def test_row_cardinality(self):
        df = create_dataframe("class.db")
        self.assertTrue(len(df) >= 10)

    def test_key(self):
        key_columns = ("video_id", "category_id", "language")
        df = create_dataframe("class.db")
        self.assertEqual(len(df), len(df.drop_duplicates(subset=key_columns)))

    def test_invalid_path_exception(self):
        self.assertRaises(ValueError, create_dataframe, "class_db")


if __name__ == "__main__":
    unittest.main()
