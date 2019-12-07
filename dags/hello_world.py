from datetime import datetime
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator

def print_hello():
    return 'Surya Prakash is a RockStar Data Engineer'

dag = DAG('hello_world', 
          description='Simple tutorial DAG',
          start_date=datetime(2019, 9, 16), 
          catchup=False)

dummy_operator = DummyOperator(task_id='dummy_task', retries=3, dag=dag)

hello_operator = PythonOperator(task_id='hello_task', python_callable=print_hello, dag=dag)

dummy_operator >> hello_operator