from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(
    dag_id="sales_ingestion",
    start_date=datetime(2025,1,1),
    schedule="@daily",
    catchup=False
) as dag:

    ingest_sales = BashOperator(
        task_id="run_sales_job",
        bash_command="""
        python /opt/airflow/pyspark/sales_ingestion.py
        """
    )
