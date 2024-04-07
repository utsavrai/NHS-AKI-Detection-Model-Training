# NHS-AKI-Detection-Model-Training

## Instructions

### Prerequisites:
Before you begin, ensure you have installed the required packages as specified in `requirements.txt`.

#### Steps:
1. To install package dependencies, execute:
   ```sh
   pip install -r requirements.txt
   ```

### Running `train.py`:
This script is responsible for training the machine learning model.

#### Steps:
1. Make sure you are in the directory containing both the `train.py` file and `training.csv`.
2. Run the script with the command:
   ```sh
   python3 train.py
   ```
   - This will process the training data from `training.csv`, train the model, and save it as `rf_model.joblib`.
   - If your training data file has a different name, adjust the script accordingly.

### Running `test_utils.py` (Unit Tests):
These tests aim to verify the functionality of utilities within the project.

#### Steps:
1. Ensure you are in the directory that contains the `test_utils.py` file.
2. Run the unit tests with:
   ```sh
   python3 -m unittest test_utils.py
   ```
   - This will execute all test cases in `test_utils.py`, confirming that the functions in `utils.py` operate correctly.

### Running `model.py`:
`model.py` can be executed using Docker or directly on your local machine.

#### Docker Method:
1. Be in the directory containing the `Dockerfile`.
2. Build the Docker image using:
   ```sh
   docker build -t aki .
   ```
3. Run the Docker container, ensuring the current directory is mounted to `/data` inside the container:
   ```sh
   docker run -v ${PWD}:/data aki
   ```

#### Local Method:
1. Go to the directory containing `model.py`.
2. Execute the script with:
   ```sh
   python3 model.py
   ```