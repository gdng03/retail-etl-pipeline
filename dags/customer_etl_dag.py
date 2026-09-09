from airflow import DAG
from airflow.providers.standard.operators.python import PythonOperator
from datetime import datetime

from src.pipelines.customer_pipeline import run_customer_pipeline


with DAG(
    dag_id="customer_etl_dag",
    start_date=datetime(2026, 8, 1),
    schedule="@daily",
    catchup=False,
) as dag:

    customer_etl = PythonOperator(
        task_id="customer_etl",
        python_callable=run_customer_pipeline,
    )