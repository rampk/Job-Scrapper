import pandas as pd
from os import listdir


def arrange_columns():
    # List of files to be cleaned
    file_list = listdir('../Data/temp')

    df_all = pd.DataFrame()

    for file in file_list:
        file_path = '../Data/temp/' + file
        df = pd.read_csv(file_path)
        df_arranged = df[['job_title', 'company_name', 'job_location',
                          'job_salary', 'job_description', 'job_posted',
                          'posted_website', 'job_link']]
        df_all = pd.concat([df_all, df_arranged])
        # df_arranged.to_csv(file_path, index=False)

    return df_all


def unique_jobs(job_links, job_data):
    # job_links = pd.DataFrame(job_links, columns=['job_link'])
    job_data = pd.concat([job_data, job_links])
    job_data.drop_duplicates(subset=['job_link'], keep=False, inplace=True)
    return job_data
