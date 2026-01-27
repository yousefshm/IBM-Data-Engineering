from datetime import datetime, timedelta  # For scheduling
from airflow import DAG  # The core DAG class
from airflow.operators.python import PythonOperator  # Note: Updated import path
from airflow.operators.bash import BashOperator  # Note: Updated import path
from airflow.utils.dates import days_ago  # For easy date scheduling

default_args = {
    'owner': 'yousef',
    'start_date': days_ago(0),
    'email': 'dummy@email.com',
    'email_on_failure': True,
    'email_on_retry': True,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    dag_id='ETL_toll_data',
    schedule_interval=timedelta(days=1),
    default_args=default_args,
    description='Apache Airflow Final Assignment',
)

unzip_data = BashOperator(
    task_id='unzip_data',
    bash_command='tar -xzf /home/project/airflow/dags/finalassignment/tolldata.tgz',
    dag=dag,
)

extract_data_from_csv = BashOperator(
    task_id='extract_data_from_csv',
    bash_command= 'cut -d"," -f1-4 /home/project/airflow/dags/finalassignment/vehicle-data.csv > '
                '/home/project/airflow/dags/finalassignment/csv_data.csv',
    dag=dag,
)

extract_data_from_tsv = BashOperator(
    task_id= 'extract_data_from_tsv',
    bash_command= 'cut -d -f5-7 /home/project/airflow/dags/finalassignment/tollplaza-data.tsv >'
                '/home/project/airflow/dags/finalassignment/tsv-data.csv',
    dag=dag,
)

extract_data_from_fixed_width = BashOperator(
    task_id= 'extract_data_from_fixed_width',
    bash_command = 'cut -c59-67 /home/project/airflow/dags/finalassignment/payment-data.txt'
                ' | tr " " "," > '
                '/home/project/airflow/dags/finalassignment/fixed_width_data.csv',
                dag=dag,
)

consolidate_data = BashOperator(
    task_id= 'consolidate_data',
    bash_command= 'paste /home/project/airflow/dags/finalassignment/csv_data.csv '
                '/home/project/airflow/dags/finalassignment/tsv_data.csv '
                '/home/project/airflow/dags/finalassignment/fixed_width_data.csv '
                ' > /home/project/airflow/dags/finalassignment/extracted_data.csv ',
                dag=dag,
)

transform_data = BashOperator(
    task_id= 'transform_data',
    bash_command='cut -d, -f4 '
                '/home/project/airflow/dags/finalassignment/extracted_data.csv | '
                'tr \'[:lower:]\' \'[:upper:]\' > '
                '/home/project/airflow/dags/finalassignment/staging/transformed_data.csv',
    dag=dag,
)

#task Pipeline
unzip_data >> extract_data_from_csv >> extract_data_from_tsv >> extract_data_from_fixed_width \
    >> consolidate_data >> transform_data

