#!/usr/bin/env python3


import pandas as pd
from sklearn.metrics import fbeta_score
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import numpy as np
import joblib
import argparse
import os
import time
import csv

# This function will be applied to each row of the dataframe to calculate the features
def calculate_features(row,format,test_index):
    """
    Calculate features for each row of the dataframe.
    
    :param row: A row from the dataframe.
    :param format: Indicates 'training' or other formats.
    :param test_index: Index where creatinine tests start in the row.
    :return: A pandas Series with calculated features.
    """
    try:
        # Preprocess date conversion and filter out NaN values
        creatinine_dates = pd.to_datetime(row[test_index:len(row):2], errors='coerce')
        creatinine_results = row[test_index+1:len(row):2]
        
        # extract the creatinine date and result pairs
        valid_indices = ~pd.isna(creatinine_results)
        creatinine_pairs = [(date, result) for date, result, valid in zip(creatinine_dates, creatinine_results, valid_indices) if valid]
        
        # Initialize features
        if format == 'training':
            features = {
            'age': row['age'],
            'sex': 1 if row['sex'] == 'f' else 0,
            'aki': 1 if row['aki'] == 'y' else 0,
            'C1': 0, 'RV1': 0, 'RV2': 0, 'RV_ratio': 0, 'D': 0
            }
        else:
            features = {
            'age': row['age'],
            'sex': 1 if row['sex'] == 'f' else 0,
            'C1': 0, 'RV1': 0, 'RV2': 0, 'RV_ratio': 0, 'D': 0
            }

        if creatinine_pairs:
            c1_date, c1_value = creatinine_pairs[-1]
            features['C1'] = c1_value

            # Calculate RV1, RV2, and RV_ratio
            rv1_values = [result for date, result in creatinine_pairs if 0 < (c1_date - date).days <= 7 and c1_value != result]
            rv2_values = [result for date, result in creatinine_pairs if 7 < (c1_date - date).days <= 365 and c1_value != result]

            if rv1_values:
                features['RV1'] = min(rv1_values)
                features['RV_ratio'] = c1_value / features['RV1']
            elif rv2_values:
                features['RV2'] = np.median(rv2_values)
                features['RV_ratio'] = c1_value / features['RV2']

            # Calculate D value
            results_within_48_hours = [result for date, result in creatinine_pairs if (c1_date - date).total_seconds() / 3600 <= 48 and c1_value != result]
            if results_within_48_hours:
                features['D'] = c1_value - min(results_within_48_hours)

        return pd.Series(features)
    except Exception as e:
        print(f"Error calculating features: {e}")
        return pd.Series()


def determine_max_values_in_row(file_path):
    """
    Determine the maximum number of values in any row of a CSV file.
    
    :param file_path: Path to the CSV file.
    :return: Maximum number of values found in any row.
    """

    try:
        max_values = 0
        with open(file_path, 'r') as file:
            for line in file:
                values = line.strip().split(',')
                max_values = max(max_values, len(values))
        return max_values
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return 0

def create_headers(max_values,format):
    """
    Create a list of headers for the dataframe.
    
    :param max_values: The maximum number of values in a row.
    :param format: Indicates 'training' or other formats.
    :return: List of headers for the dataframe.
    """
    try:
        headers = ['age', 'sex']
        if format == 'training':
            headers.append('aki')
        for i in range((max_values - len(headers)) // 2):
            headers.extend([f'creatinine_date_{i}', f'creatinine_result_{i}'])
        return headers
    except Exception as e:
        print(f"Error creating headers: {e}")
        return []