import pandas as pd

def transform_data(df):

    # Clean column names
    df.columns = df.columns.str.lower().str.replace(" ", "_")

    # Handle missing values
    df.dropna(inplace=True)

    # Convert attrition to numeric
    df['attrition'] = df['attrition'].map({'Yes': 1, 'No': 0})

    # Create age group
    df['age_group'] = pd.cut(
        df['age'],
        bins=[18, 25, 35, 45, 60],
        labels=['18-25', '25-35', '35-45', '45-60']
    )

    return df