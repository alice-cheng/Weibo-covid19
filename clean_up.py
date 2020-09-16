# with open('results.csv','r',encoding='utf-8') as in_file, open('results_cleaned.csv','w',errors = 'ignore') as out_file:
#     seen = set() # set for fast O(1) amortized lookup
#     for line in in_file:
#         if line in seen: continue # skip duplicate
#
#         seen.add(line)
#         out_file.write(line)

import pandas as pd
from pprint import pprint

df = pd.read_csv('results.csv',index_col = False)


# cleaned data after removing duplicates is (380,2)
df.drop(df.columns[0], axis = 1,inplace = True)


df.columns = ['time_stamp', 'post']
df = df.drop_duplicates(subset = ['post'],keep = 'first')
df.reset_index(drop=True,inplace = True)
pd.to_datetime(df.time_stamp)
# pprint(df)

df.to_csv('results_cleaned.csv',sep='\t', encoding='utf-8')
