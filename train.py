#!/usr/bin/env python3

from utils import *

def main():
    """
    Main function to train a Random Forest model for AKI prediction.
    It reads the training data, performs feature engineering, trains the model,
    and evaluates its performance using the F3 score. The model is saved
    if it meets the deployment criteria.
    """
    try:
        __location__ = os.path.realpath(
            os.path.join(os.getcwd(), os.path.dirname(__file__)))

        # Determine the maximum number of attributes per row/patient in the training file
        train_max_cols = determine_max_values_in_row(os.path.join(__location__, 'training.csv'))

        # Create necessary missing headers using the train_max_cols value
        train_headers = create_headers(train_max_cols, 'training')

        # Load the dataframe using appropriate headers created for missing columns
        df = pd.read_csv(os.path.join(__location__, 'training.csv'),
                         index_col=None,
                         sep=',',
                         skiprows=1,
                         names=train_headers,
                         on_bad_lines='warn'
                         )

        start_time = time.time()
        # Create new features based on AKI prediction algorithm parameters
        df_features = df.apply(lambda row: calculate_features(row, 'training', 3), axis=1) # 3 because for training.csv we have age,sec, and aki
        print("--- %s seconds for feature engineering ---" % (time.time() - start_time))

        # Split the dataset into features and target label
        X = df_features.drop('aki', axis=1)
        y = df_features['aki']

        # Split the data into training and validation sets
        X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)

        # Train the random forest model
        model = RandomForestClassifier()
        start_time = time.time()
        model.fit(X_train, y_train)
        print("--- %s seconds for random forest model fitting ---" % (time.time() - start_time))
        # Predict on validation set
        y_pred = model.predict(X_val)

        # Save the model to a file
        model_filename = 'rf_model.joblib'
        joblib.dump(model, model_filename)
        print(f"Model saved to {model_filename}")

        # Calculate F3 score
        f3_score = fbeta_score(y_val, y_pred, beta=3)
        print(f"F3 Score: {f3_score}")

        # Deployment decision
        if f3_score > 0.7:
            print("The model meets the criteria for deployment.")
        else:
            print("The model does not meet the criteria for deployment.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
