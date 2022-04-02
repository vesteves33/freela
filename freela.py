import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt
import seaborn as sns

from phonenumbers import number_type


path = Path(__file__).parent.absolute()

#lendo planilha em formato xlsx
try:
  df = pd.read_excel(path/'students.xlsx', sheet_name='Marks', engine='openpyxl')

except ValueError:
  df = pd.read_excel(path/'students.xlsx', sheet_name='Marks', engine='openpyxl')


turma_a = df.groupby('Class').get_group('A').mean(numeric_only=True)
turma_b = df.groupby('Class').get_group('B').mean(numeric_only=True)
turma_c = df.groupby('Class').get_group('C').mean(numeric_only=True)

# turma_a.to_excel(path/'results_turma_a.xlsx', sheet_name='results', index=False)
# turma_b.to_excel(path/'results_turma_b.xlsx', sheet_name='results', index=False)
# turma_c.to_excel(path/'results_turma_c.xlsx', sheet_name='results', index=False)
print('Turma A')
print(turma_a)

print('Turma B')
print(turma_b)

print('Turma C')
print(turma_c)