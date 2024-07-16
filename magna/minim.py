import pandas as pd

# Sample list
data = [['Alice', 25, 'Engineer'],
        ['Bob', 30, 'Doctor'],
        ['Charlie', 28, 'Lawyer']]

# Convert list to dataframe
df = pd.DataFrame(data, columns=['Name', 'Age', 'Profession'])

print(df)
