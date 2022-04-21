import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

excel_file_1 = 'shift-data.xlsx'
excel_file_2 = 'third-shift-data.xlsx'

# create a dataframe that you can print, manipulate, etc.
# list sheet name (default is sheet 1)
df_first_shift = pd.read_excel(excel_file_1, sheet_name='first')
df_second_shift = pd.read_excel(excel_file_1, sheet_name='second')
df_third_shift = pd.read_excel(excel_file_2)

# join the dataframes on matching column headers (MUST BE EXACT)
df_all = pd.concat([df_first_shift, df_second_shift, df_third_shift])

# Calculations
pivot = df_all.groupby(['Shift']).mean()
# .loc allows you to select multiple rows
# [:] indicates all row, and then input each column you want
shift_productivity = pivot.loc[:, "Production Run Time (Min)":"Products Produced (Units)"]
print(shift_productivity)

# Graphing (can change formatting per documentation)
shift_productivity.plot(kind='bar')
plt.savefig('plot.png')
plt.show() # does not work in WSL, must use Python digital environment

# export to excel
df_all.to_excel("output.xlsx")