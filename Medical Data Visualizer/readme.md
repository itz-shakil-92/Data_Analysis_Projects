# Medical Data Visualizer

This project aims to visualize and make calculations from medical examination data using matplotlib, seaborn, and pandas. The dataset values were collected during medical examinations.

## Data Description

The dataset contains the following columns:

- `id`: Patient ID
- `age`: Age of the patient in days
- `sex`: Gender of the patient
- `height`: Height of the patient in centimeters
- `weight`: Weight of the patient in kilograms
- `ap_hi`: Systolic blood pressure
- `ap_lo`: Diastolic blood pressure
- `cholesterol`: Cholesterol level (1: normal, 2: above normal, 3: well above normal)
- `gluc`: Glucose level (1: normal, 2: above normal, 3: well above normal)
- `smoke`: Whether the patient smokes or not (binary)
- `alco`: Whether the patient consumes alcohol or not (binary)
- `active`: Whether the patient is physically active or not (binary)
- `cardio`: Presence or absence of cardiovascular disease (binary)

## Tasks

1. Add an `overweight` column to the data. To determine if a person is overweight, calculate their BMI by dividing their weight in kilograms by the square of their height in meters. If the BMI is greater than 25, then the person is considered overweight.
2. Normalize the data by making 0 always good and 1 always bad. For cholesterol and glucose levels, if the value is 1, set it to 0; if it's greater than 1, set it to 1.
3. Draw a categorical plot that shows the value counts of the categorical features split by the presence or absence of cardiovascular disease.
4. Clean the data by filtering out incorrect segments, such as diastolic pressure being higher than systolic, and extreme values for height and weight.
5. Create a correlation matrix using the dataset and plot it as a heatmap, masking the upper triangle.

## Usage

1. Clone this repository:

git clone https://github.com/itz-shakil-92/Data_Analysis_Projects/medical-data-visualizer.git


2. Install the required dependencies:

pip install -r requirements.txt


3. Run the main script:


## Files

- `medical_data_visualizer.py`: Contains the implementation of the data visualization tasks.
- `test_module.py`: Contains unit tests to verify the correctness of the implemented functions.
- `medical_examination.csv`: CSV file containing the medical examination data.
- `main.py`: Entry point for running the project.

## Credits

This project is part of the Python curriculum on [freeCodeCamp.org](https://www.freecodecamp.org/). The dataset is provided by freeCodeCamp.org.
