# Data analitycs example projects

This  is an examle of how to create a normal workflow for
analytics team.

## Configuration for the project

- Install gcloud cli
first of all we need to set our gcloud cli to interact with 
our objects storage ..... 
to do this please follow the next instructiosn 
https://cloud.google.com/sdk/docs/install?hl=es-419
- set default credentials
https://cloud.google.com/docs/authentication/provide-credentials-adc?hl=es-419

- intall requirements
```bash
python -m venv venv
venv/Scripts/activate
pip install -r requirements.txt
```
an example of how to implement the first ingestion is in [csv_to_gstorage.py](csv_to_gstorage.py)
