import pandas as pd
from google.cloud import storage
import os
from datetime import datetime as dt

def read_csv_files(route: str) -> pd.DataFrame:
    """
    This function read the csv in the indicated route

    Args:
        route (str): route string example 'C:/users/file.txt'

    Returns:
        DataFrame: readed csv file 
    """    
    df = pd.read_csv(route)
    df['created_date'] = (str)(dt.today())
    return df


def load_to_gstorage(data: pd.DataFrame, output_route: str) -> None:
    """
    Upload the readed file to gstorage

    Args:
        data (pd.DataFrame): dataframe to upload
        output_route (str): g storage destination
    """    
    client = storage.Client()
    # The bucket on GCS in which to write the CSV file
    bucket = client.get_bucket('data_projects_mfbl')
    # # The name assigned to the CSV file on GCS
    blob = bucket.blob(output_route)
    blob.upload_from_string(data.to_csv(), 'text/csv')
    # # data.to_csv('gs://data_projects_mfbl/spotify_data/exaple.csv')
    

if __name__ == "__main__":
    data = read_csv_files('./inputs/spotify.csv')
    load_to_gstorage(data, 'spotify_data/spotify_data.csv')