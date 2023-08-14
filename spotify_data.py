import pandas as pd
from google.cloud import storage
import os
from datetime import datetime as dt

def load_csv_files(filename):
    df = pd.read_csv(filename)
    df['created_date'] = (str)(dt.today())
    return df


def load_to_gstorage(data):
    print(data.head())
    # client = storage.Client.from_service_account_json(json_credentials_path='file.json')
    client = storage.Client()
    # The bucket on GCS in which to write the CSV file
    # bucket = client.bucket('gs://data_projects_mfbl')
    bucket = client.get_bucket('data_projects_mfbl')
    # client.get_bucket('https://console.cloud.google.com/storage/browser/data_projects_mfbl')
    # # The name assigned to the CSV file on GCS
    blob = bucket.blob('spotify_data/my_data.csv')
    blob.upload_from_string(data.to_csv(), 'text/csv')
    # # data.to_csv('gs://data_projects_mfbl/spotify_data/exaple.csv')
    

if __name__ == "__main__":
    data = load_csv_files('spotify.csv')
    load_to_gstorage(data)