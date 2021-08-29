### airflow related

from airflow import DAG
from airflow.operators.bash import BashOperator

# others packeges
from datetime import timedelta
from datetime import datetime

default_args = {
    "owner": "diego",
    "retries": 3,
    "retry_delay": timedelta(minutes=3)
}

with DAG(
    dag_id="first_dag",
    description="This is my first dag",
    start_date=datetime(2021, 8, 29, 2),
    schedule_interval='@daily',
    default_args=default_args
) as dag:
    task1 = BashOperator(
        task_id="first_task",
        bash_command="echo hello world"
    )

    task1
