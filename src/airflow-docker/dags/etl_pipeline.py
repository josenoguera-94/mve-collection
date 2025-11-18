from airflow.decorators import dag, task
from datetime import datetime, timedelta

from extract import Extract
from transform import Transform
from load import Load

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 1, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1),
}


@dag(
    dag_id='etl_pipeline',
    default_args=default_args,
    description='A simple ETL pipeline example with file storage',
    catchup=False,
    tags=['example', 'etl'],
)
def etl_pipeline():

    @task
    def extract_task():
        extractor = Extract()
        file_path = extractor.run()
        return file_path

    @task
    def transform_task(input_path: str):
        transformer = Transform()
        output_path = transformer.run(input_path)
        return output_path

    @task
    def load_task(input_path: str):
        loader = Load()
        num_rows = loader.run(input_path)
        return f"Loaded {num_rows} rows"

    extract_result = extract_task()
    transform_result = transform_task(extract_result)
    load_result = load_task(transform_result)

    extract_result >> transform_result >> load_result


# Instantiate the DAG with a conventional variable name
dag = etl_pipeline()
