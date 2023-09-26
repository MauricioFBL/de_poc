from dagster import repository

from analytics_jobs.spotify_analytics.config.solids import spotify_analytics_pipeline
from analytics_jobs.spotify_analytics.config.schedule import spotify_analytics_schedule

@repository(name="Spotify")
def spotify_repository():
    return [
        spotify_analytics_pipeline ,spotify_analytics_schedule
    ]