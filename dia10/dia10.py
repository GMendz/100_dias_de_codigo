import pandas as pd

dados = {'nomes': ['Ari', 'Maria', 'Joana', 'Fernando', 'Carlos'],
        'departamento': ['TI', 'Marketing', 'TI', 'Recursos Humanos', 'TI'],
        'salario': [7130, 4864, 8501, 4900, 7640]}

df = pd.DataFrame(dados)

ti_employees = df[df['departamento'] == 'TI']

media_salarial_ti = ti_employees['salario'].mean()

print("A média salarial dos funcionários de TI é:", media_salarial_ti)