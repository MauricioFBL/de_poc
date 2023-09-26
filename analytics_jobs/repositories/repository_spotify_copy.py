from dagster import repository

from analytics_jobs.spotify_analytics_copy.config.solids import spotify_analytics_pipeline_copy
from analytics_jobs.spotify_analytics_copy.config.schedule import spotify_analytics_schedule_copy

@repository(name="Spotify_copy")
def spotify_repository():
    return [
        spotify_analytics_pipeline_copy ,spotify_analytics_schedule_copy
    ]