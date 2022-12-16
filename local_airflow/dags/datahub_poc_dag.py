from airflow import DAG
from airflow.operators.python_operator import PythonOperator

default_dag_args = {
    "start_date": "2022-12-15",
    "retries": 0,
}


with DAG(
    "datahub_poc_dag",
    schedule_interval="0 0 * * *",
    max_active_runs=1,
    default_args=default_dag_args,
    is_paused_upon_creation=True,
    catchup=False,
) as dag:

    def task_one_fn():
        print("This is task one")

    def task_two_fn(task_name):
        print(f"This is task {task_name}")

    task_one = PythonOperator(
        task_id="task_one",
        python_callable=task_one_fn,
    )

    task_two = PythonOperator(
        task_id="task_two",
        python_callable=task_two_fn,
        params=dict(task_name="two"),
        op_kwargs=dict(task_name="{{ params.task_name }}"),
    )
    
    task_one >> task_two