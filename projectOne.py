import pandas as pd

#Dataframe creation
df = pd.read_excel('CH202513.xlsx',sheet_name = 'Sheet2')

#Splitting names to make username
df[['Username', 'Last']] = df['Names'].str.split(' ',expand=True)

df['password'] = df['Username'] + df['Last'].str.slice(0,2)
df['UID'] = range(1030, 1030+len(df))
df['GID'] = 150
df['home_dir'] = '/home/' + df['Username']
df['shell'] = '/bin/bash'

#Filtering dataframe
df1 = df[['Username','password','UID','GID','Names','home_dir','shell']]

#Formatting the txt file
df1.to_csv('credentials.txt', header=None, sep=':', index=False)
print("Printed on credentials.txt")
