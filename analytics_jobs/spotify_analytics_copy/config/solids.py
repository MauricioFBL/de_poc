from analytics_jobs.spotify_analytics.integration import *

import pandas as pd
from dagster import Output, op, job, RetryPolicy, String, Out

@op(description='load file in bq', tags={'Owner': 'Mauricio Bautista'})
def integration_op():
    integrate()


@job(tags={'Owner': 'Mauricio Bautista'})
def spotify_analytics_pipeline_copy():
    integration_op()