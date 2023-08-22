# Data analitycs capstone projects

This  is an examle of how to create a normal workflow for
analytics team.

## Project structure & description
This is a capstone project so we divide the project in 5 main stages
the project run on gcp 
### Stages
 - Ingestion 
 - preprocessing & aggregation
 - modeling & procession
 - orquestration & warehousing
 - dashboarding


### Stack
- gcp
    - iam
    - bigquery
    - cloud storage
    - compute engine
- python 
    - spark
    - dagster
- power bi 

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
