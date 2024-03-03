# Decision Tree Learning

This is a Python implementation of the decision tree learning algorithm, specifically a basic form of the ID3 (Iterative Dichotomiser 3) algorithm. Decision trees are a popular machine learning technique for classification and regression tasks.

## Description

The implementation consists of classes and functions to build a decision tree from a given dataset and print the constructed tree. It calculates entropy and information gain to determine the best attribute for splitting the dataset at each node of the tree.

## Files

- `decision_tree.py`: Contains the Python code for decision tree learning.
- `data.csv`: CSV file containing the dataset used for training the decision tree.

## Usage

1. Ensure you have Python installed on your system.
2. Install the required dependencies using `pip install pandas`.
3. Place your dataset in a CSV file named `data.csv`.
4. Run the `decision_tree.py` script using `python decision_tree.py`.
5. The script will output the constructed decision tree.

## Dataset Format

The dataset should be provided in a CSV format with the following columns:
- "Day": Identifier for each data instance.
- "Outlook": Weather outlook on a particular day (e.g., Sunny, Overcast, Rain).
- "Temperature": Temperature on a particular day (e.g., Hot, Mild, Cool).
- "Humidity": Humidity level on a particular day (e.g., High, Normal).
- "Wind": Wind strength on a particular day (e.g., Weak, Strong).
- "Play Tennis": Target variable indicating whether tennis was played on that day (e.g., Yes, No).

## Output

The output of the script will be the decision tree constructed from the provided dataset, printed in a human-readable format
