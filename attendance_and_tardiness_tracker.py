import pandas as pd

# Load the data using .dat file
column_names = ['id', 'date', 'time', 'drop_1', 'type', 'drop_2', 'drop_3']
raw = pd.read_csv('biometric_punch.dat', header=None, names=column_names, delimiter=r'\s+')

# Drop unnecessary columns
raw_converted = raw.drop(['drop_1', 'drop_2', 'drop_3'], axis=1)


#ATTENDACE TRACKER

biometrics = raw_converted
user = pd.read_csv('user_id.csv')

#Capturing time in HH:MM format only
biometrics['time'] = pd.to_datetime(biometrics['time'], format='%H:%M:%S', errors='coerce').dt.strftime('%H:%M')
biometrics.head()

#Dropping duplicate rows
biometrics = biometrics.drop_duplicates()

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

#Filtering results to capture biometrics record in October onwards
result['date'] = pd.to_datetime(result['date'])
result_filtered = result[(result['date'].dt.month >= 10)] # Modify this row to capture desired date
result_filtered.head()

#Joining user_id to biometrics record to identify names that correspond to id
merged_data = pd.merge(user,result_filtered, on='id', how='left')
merged_data.head()

#Exporting as excel file in different sheets per employee name
with pd.ExcelWriter('output_grouped.xlsx') as writer:
    # Group by 'Name' and write each group to a separate sheet
    for name, group in merged_data.groupby('Name'):
        sheet_name = name  # Name the sheet based on the 'Name' value
        group.to_excel(writer, sheet_name=sheet_name, index=False)




#TARDINESS TRACKER

#Limit time format at "hh:mm"
raw_converted['time']=raw_converted['time'].str[:5]
raw_converted = raw_converted.drop_duplicates(subset='time')

# Reset the index
biometrics = raw_converted.reset_index(drop=True)

# Convert time and date columns as datetime type
biometrics['date'] = pd.to_datetime(biometrics['date'])
biometrics['time'] = pd.to_datetime(biometrics['time'],format='%H:%M').dt.time
bio = biometrics[biometrics['date'].dt.month >=8]

# Filter data for late employees
filtered_biometrics = bio[
    (bio['type'] == 0) & #Check-in type
    (bio['date'].dt.month >= 8) & # Modify this line to the desired date and timeframe
    ((bio['time'] >= pd.to_datetime("06:01").time()) & (bio['time'] <= pd.to_datetime("10:00").time()) |      # Day Shift records
     (bio['time'] >= pd.to_datetime("18:01").time()) & (bio['time'] <= pd.to_datetime("22:00").time()))       # Night shift records
]

# Group by id, count number of late and show times and dates of late
late_employees = filtered_biometrics.groupby('id').agg(
    count=('id', 'size'),               # Count of records for each id
    times=('time', list),               # List of time values for each id
    dates=('date', list)                # List of date values for each id
).reset_index()

# Format the 'dates' column to 'YY:MM:DD'
late_employees['dates'] = late_employees['dates'].apply(
    lambda x: [d.strftime('%m-%d-%y') for d in x]
)

# Format the 'times' column to 'HH:MM'
late_employees['times'] = late_employees['times'].apply(
    lambda x: [t.strftime('%H:%M') for t in x]
)
late_employees['count'] = late_employees['count']
late_employees['count'] = late_employees['count'].astype('str')

#Join with user_id file
user = pd.read_csv('user_id.csv')
name_late_employees = pd.merge(user,late_employees,how='left',on='id').fillna(0)

#Print the result
print(name_late_employees)

#Export as an excel file
name_late_employees.to_excel('late_employees_record.xlsx',index=False)
