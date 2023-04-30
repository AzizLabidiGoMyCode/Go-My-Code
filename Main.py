# import pandas as pd
import pandas as pd
# import numpy as np
import numpy as np

d = {'name': ['Anastasia', 'Dima', 'Katherine', 'James'], 'score': [12.5, 20 , 16.5, np.nan],
     'attempts': [1, 3, 2, 3], 'qualify': ['yes', 'no', 'yes', 'no']}
df = pd.DataFrame(d)
# deleting Dima form the dataframe using drop function
df = df.drop(df[df['name'] == 'Dima'].index)
df = df.drop(df[df['name'] == 'James'].index)
# adding a new value to the name table "aziz"
df.loc[4, 'name'] = 'aziz'
df.loc[4, 'score'] = 20
df.loc[4, 'attempts'] = '1'
df.loc[4, 'qualify'] = 'yes'
# deleting the attempts column
df = df.drop('attempts', axis=1)
# adding a new success column
my_list = [0 , 0, 0]
for i in range(len(d["score"])):
     print(d["score"][i])
     if d["score"][i] > 10 :
         my_list[i] = 1
df.insert(3, 'success', my_list)
# exporting the dataframe to a csv file
df.to_csv('my_data.csv')
print(df)
