from dagster import schedule
from datetime import datetime, time, date
from analytics_jobs.spotify_analytics.config.solids import spotify_analytics_pipeline

@schedule(
    cron_schedule="0 12 */3 * *", # every three days at noon UTC (9am PST),
    job=spotify_analytics_pipeline,
    execution_timezone="America/Mexico_City")
def spotify_analytics_schedule(context):
    date = context.scheduled_execution_time.strftime("%y-%m-%d")
    return{
        "solids": {
            "integration_op": {"config": {"date": date}}
        }
    }
