from google.cloud import bigquery
import pandas as pd

from config import PROJECT_ID, DATA_DIR

_client = None


def get_client() -> bigquery.Client:
    global _client
    if _client is None:
        _client = bigquery.Client(project=PROJECT_ID)
    return _client


def run_query(sql: str, save_as: str | None = None) -> pd.DataFrame:
    """Run `sql` against BigQuery and return a DataFrame.

    save_as=None         -> ad-hoc: nothing written to disk.
    save_as="some_name"  -> also written to data/some_name.parquet, overwriting
    """
    df = get_client().query(sql).to_dataframe()

    if save_as:
        DATA_DIR.mkdir(exist_ok=True)
        df.to_parquet(DATA_DIR / f"{save_as}.parquet", index=False)

    return df
