import pandas as pd
import ast

df = pd.read_csv("nailib_data_cleaned_updated.csv")

def clean_sections_combined(sections):
    try:
        sections_list = ast.literal_eval(sections)
        return "; ".join(set(sections_list))
    except Exception as e:
        return sections

df["sections_combined"] = df["sections_combined"].apply(clean_sections_combined)

df.to_csv("nailib_data_final_cleaned.csv", index=False)
print("Data cleaned and saved as 'nailib_data_final_cleaned.csv'")
