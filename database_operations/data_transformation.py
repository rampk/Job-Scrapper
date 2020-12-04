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
    job_data = pd.merge(job_data, job_links,
                        indicator=True, how='outer').query('_merge=="left_only"').drop('_merge', axis=1)
    job_data.drop_duplicates(subset=['job_link'], inplace=True)
    return job_data
