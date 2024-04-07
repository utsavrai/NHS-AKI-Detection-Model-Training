import unittest
from utils import *

class TestUtils(unittest.TestCase):
    
    def test_calculate_features(self):
        # Example test for calculate_features function
        row = pd.Series({'age': 45, 'sex': 'f', 'aki': 'y', 'creatinine_date_0': '2021-01-01', 'creatinine_result_0': 1.2})
        format = 'training'
        test_index = 3
        expected_output = pd.Series({'age': 45, 'sex': 1, 'aki': 1, 'C1': 1.2,  'RV1': 0, 'RV2': 0, 'RV_ratio': 0, 'D': 0})  
        result = calculate_features(row, format, test_index)
        pd.testing.assert_series_equal(result, expected_output)

    def test_determine_max_values_in_row(self):
        # Example test for determine_max_values_in_row function
        test_file = 'test.csv' 
        expected_max_values = 20  # Expected number of columns
        self.assertEqual(determine_max_values_in_row(test_file), expected_max_values)

    def test_create_headers(self):
        # Example test for create_headers function
        max_values = 20
        format = 'training'
        expected_headers = ['age', 'sex', 'aki', 'creatinine_date_0', 'creatinine_result_0', 'creatinine_date_1','creatinine_result_1','creatinine_date_2','creatinine_result_2','creatinine_date_3','creatinine_result_3','creatinine_date_4','creatinine_result_4','creatinine_date_5','creatinine_result_5','creatinine_date_6','creatinine_result_6','creatinine_date_7','creatinine_result_7']
        self.assertEqual(create_headers(max_values, format), expected_headers)

if __name__ == '__main__':
    unittest.main()
