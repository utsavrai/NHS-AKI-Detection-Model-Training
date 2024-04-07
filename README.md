# NHS-AKI-Detection-Model-Training

```markdown
## Instructions

### Prerequisites:
Before you begin, make sure to install the required packages as specified in `requirements.txt`.

#### Steps:
1. Install package dependencies by running:
   ```
   pip install -r requirements.txt
   ```

### Running `train.py`:
This script is responsible for training the machine learning model.

#### Steps:
1. Ensure you are in the directory containing both the `train.py` file and `training.csv`.
2. Execute the script with the following command:
   ```
   python3 train.py
   ```
   - This will process the training data from `training.csv`, train the model, and save it as `rf_model.joblib`.
   - If your training data file has a different name, please modify the script to match the file name.

### Running `test_utils.py` (Unit Tests):
These tests are designed to verify the functionality of the utilities used within the project.

#### Steps:
1. Be sure you're in the directory that includes the `test_utils.py` file.
2. Execute the unit tests by running:
   ```
   python3 -m unittest test_utils.py
   ```
   - This command will run all the test cases defined in `test_utils.py`, ensuring that the utility functions in `utils.py` work as expected.

### Running `model.py`:
You can run `model.py` either using Docker or directly on your local machine.

#### Docker Method:
1. Make sure you're in the directory with the `Dockerfile`.
2. Build the Docker image with the following command:
   ```
   docker build -t aki .
   ```
3. Run the Docker container, mounting the current directory to `/data` inside the container:
   ```
   docker run -v ${PWD}:/data aki
   ```

#### Local Method:
1. Navigate to the directory containing `model.py`.
2. Run the script using:
   ```
   python3 model.py
   ```
```