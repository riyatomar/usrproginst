
import pandas as pd
import re

# input the paths to the two hindi and ang corpus files here with format as shared in the emaila
hindi_data_path = '8stnd_3ch'
eng_data_path = '8stnd_3ch_eng'
#input the name of the final parallel corpus file, which can be directly used in the concept-id update code
pc_name = 'parallel_corpus.csv'




def get_new_id(row):
    id0 = row['hin_id']
    us_split = id0.split('_')
    us_split[-1] = re.sub("[^0-9]", "", us_split[-1])
    return '_'.join(us_split)




hin_df = pd.read_csv(hindi_data_path,sep = '  ',header=None)
eng_df = pd.read_csv(eng_data_path,sep = '\t',header=None)


hin_df.columns = ['hin_id','hin_sent']
eng_df.columns = ['eng_id','eng_sent']



hin_df['eng_id'] = hin_df.apply(lambda x: get_new_id(x),axis=1)

hin_df['eng_sent'] = hin_df.apply(lambda x:eng_df[eng_df['eng_id'] == x['eng_id']]['eng_sent'].values[0],axis=1)

hin_df.to_csv(pc_name,sep='\t')






