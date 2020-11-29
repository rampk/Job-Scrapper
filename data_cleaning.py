import pandas as pd

# List of files to be cleaned
file_list = ['indeed.csv']


def arrange_columns(df_data):
    df_arranged = df_data[['job_title', 'company_name', 'job_location',
                           'job_salary', 'job_description', 'job_posted',
                           'posted_website', 'job_link']]
    return df_arranged


for file in file_list:
    file_path = '../Data/temp/' + file
    df = pd.read_csv(file_path)
    df = arrange_columns(df)
    df.to_csv(file_path,index=False)
