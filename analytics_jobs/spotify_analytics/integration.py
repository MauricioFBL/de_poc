import analytics_jobs.util_scripts.csv_to_gstorage as tbq
import datetime as dt


def integrate() -> None:
    today = dt.datetime.today()
    data = tbq.read_csv_files('./inputs/spotify.csv')
    tbq.load_to_gstorage(
        data, 
        f'spotify_data/raw/spotify_data_{today.strftime("%Y%m%d")}.csv')