import pandas as pd

def extract_data():
    df = pd.read_csv("data/hr_data.csv")
    return df