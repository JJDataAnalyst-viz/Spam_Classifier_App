import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
sys.path.append('/opt/airflow/src')
import os
from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator



from nlp.pipeline.main_pipeline import main



default_args = {
    'owner' : 'sciopsengineer',
    'retries' : 3,
    'retry_delay' : timedelta(minutes=2),
}

with DAG(
    dag_id = 'DAG-model',
    default_args = default_args,
    description = 'Ingest,Transform and Train Model',
    start_date = datetime(2025,4,26),
    tags = ['main_dag','python','bash'],
    schedule_interval = '@weekly'
) as dag:
    task1 = BashOperator(
        task_id = 'task1',
        bash_command = 'echo Ingesting data...'
    )


    task2 = BashOperator(
        task_id = 'task2',
        bash_command = 'echo Transforming and Modeling data..'
    )

    train_model = PythonOperator(
        task_id = 'train_model',
        python_callable = main
    )

    end = BashOperator(
        task_id = 'end',
        bash_command = 'echo Operation was successfull'
    )


    [task1,task2] >> train_model >> end
