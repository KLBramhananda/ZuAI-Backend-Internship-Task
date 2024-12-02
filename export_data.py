import pandas as pd
import ast

df = pd.read_csv("nailib_data_cleaned.csv")

section_columns = [col for col in df.columns if col.startswith('sections.')]
print("Found section columns:", section_columns)

df['sections_combined'] = df[section_columns].apply(lambda row: [item for item in row if pd.notna(item)], axis=1)

df = df.drop(columns=section_columns)
gi
df.to_csv("nailib_data_cleaned_updated.csv", index=False)
df.to_excel("nailib_data_cleaned_updated.xlsx", index=False)

print("Combined Data Preview:")
print(df[['title', 'sections_combined']].head())

df['sections_combined'] = df['sections_combined'].apply(lambda x: ast.literal_eval(x) if isinstance(x, str) else x)

print("Parsed sections_combined column:")
print(df['sections_combined'].head())

print("Data cleaned and saved as 'nailib_data_cleaned_updated.csv' and 'nailib_data_cleaned_updated.xlsx'")
