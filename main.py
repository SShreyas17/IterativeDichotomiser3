import pandas as pd
import math

# Define a class for nodes in the decision tree
class Node:
    def __init__(self, attribute=None, value=None, result=None):
        self.attribute = attribute  # Splitting attribute
        self.value = value          # Value of the splitting attribute
        self.result = result        # Class label if the node is a leaf
        self.children = {}          # Dictionary to store children nodes

# Function to calculate entropy of a dataset
def calculate_entropy(df):
    classes = df['Play Tennis'].unique()
    entropy = 0
    total = len(df)
    for c in classes:
        p = len(df[df['Play Tennis'] == c]) / total
        entropy -= p * math.log2(p)
    return entropy

# Function to calculate information gain of an attribute
def calculate_information_gain(df, attribute):
    values = df[attribute].unique()
    gain = calculate_entropy(df)
    total = len(df)
    for v in values:
        subset = df[df[attribute] == v]
        gain -= (len(subset) / total) * calculate_entropy(subset)
    return gain

# Function to determine the majority class in a dataset
def get_majority_class(df):
    return df['Play Tennis'].mode()[0]

# Function to build the decision tree recursively
def build_tree(df, attributes):
    if len(df['Play Tennis'].unique()) == 1:
        return Node(result=df['Play Tennis'].iloc[0])
    
    if len(attributes) == 0:
        return Node(result=get_majority_class(df))

    max_gain = -1
    best_attr = None
    for attr in attributes:
        gain = calculate_information_gain(df, attr)
        if gain > max_gain:
            max_gain = gain
            best_attr = attr
    
    root = Node(attribute=best_attr)
    for value in df[best_attr].unique():
        subset = df[df[best_attr] == value]
        if len(subset) == 0:
            root.children[value] = Node(result=get_majority_class(df))
        else:
            root.children[value] = build_tree(subset.drop(columns=[best_attr]), [a for a in attributes if a != best_attr])
    return root

# Function to print the decision tree in a readable format
def print_tree(node, depth=0):
    if node.result is not None:
        print('  ' * depth, "Result:", node.result)
        return
    print('  ' * depth, "Attribute:", node.attribute)
    for value, child in node.children.items():
        print('  ' * (depth + 1), "Value:", value)
        print_tree(child, depth + 2)

# Read data from CSV
data = pd.read_csv("data.csv")

# Build the decision tree
root = build_tree(data, ['Outlook', 'Temperature', 'Humidity', 'Wind'])

# Print the decision tree
print_tree(root)
