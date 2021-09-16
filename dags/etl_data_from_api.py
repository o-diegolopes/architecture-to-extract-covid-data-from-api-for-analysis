# airflow related

from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.apache.hdfs.hooks.hdfs import HDFSHook

# others packeges
from datetime import timedelta
from datetime import datetime

default_args = {
    "owner": "Diego Lopes",
    "depends_on_past": False,
    # "start_date": datetime(2020, 1, 23),
    # "email_on_failure": False,
    # "email_on_retry": False,
    "retries": 3,
    "retry_delay": timedelta(minutes=3),
    "provide_context": True
}


class ExtractDataFromApi:
    """
        Returns the data from API.

                Parameters:

                Returns:
                        df_data (dataframe): Pandas dataframe with the batch data.
    """

    def __init__(self):
        self.__init__()
