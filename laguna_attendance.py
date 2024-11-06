import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

#downloaded data from fingerprint scanner
biometrics = pd.read_csv('laguna_bio_info.csv')
user = pd.read_csv('user_id.csv')

#Capturing time in HH:MM format only
biometrics['time'] = pd.to_datetime(biometrics['time'], format='%H:%M:%S', errors='coerce').dt.strftime('%H:%M')
biometrics.head()

#Creating list in time column by grouping id and date
grouped = (biometrics
           .groupby(['id', 'date'])
           .agg(lambda x: list(x) if len(x) > 0 else [None])
           .reset_index())

# Flattening the multi-level columns
result = grouped.apply(lambda row: pd.Series({
    'id': row['id'],
    'date': row['date'],
    'checkin': [time for i, time in zip(row['type'], row['time']) if i == 0],
    'checkout': [time for i, time in zip(row['type'], row['time']) if i == 1],
    'breakin': [time for i, time in zip(row['type'], row['time']) if i == 3],
    'breakout': [time for i, time in zip(row['type'], row['time']) if i == 2],
    'unknown': [time for i, time in zip(row['type'], row['time']) if i not in [0, 1, 2, 3]]
}), axis=1)

result.head()

#Filtering results to capture biometrics record in October and November
result['date'] = pd.to_datetime(result['date'])
result_10_11 = result[(result['date'].dt.month == 10) | (result['date'].dt.month == 11)]
result_10_11.head()

#Joining user_id to biometrics record to identify names that correspond to id
merged_data = pd.merge(user,result_10_11, on='id', how='left')
merged_data.head()

#Exporting as excel file in different sheets per employee name
with pd.ExcelWriter('grouped_ids_output.xlsx') as writer:
    # Group by 'Name' and write each group to a separate sheet
    for name, group in merged_data.groupby('Name'):
        sheet_name = name  # Name the sheet based on the 'Name' value
        group.to_excel(writer, sheet_name=sheet_name, index=False)