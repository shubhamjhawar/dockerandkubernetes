from airflow import DAG
from airflow.operators.postgres_operator import PostgresOperator
import datetime

DAG_ID = "postgres_operator_dag"

with DAG(
    dag_id=DAG_ID,
    start_date=datetime.datetime(2023, 2, 2),
    schedule_interval="@once",
    catchup=False,
) as dag:
    createtable_task = PostgresOperator(
        task_id="createtable_task",
        postgres_conn_id='postgres',
        sql="""
            CREATE TABLE IF NOT EXISTS EMP(
            name VARCHAR NOT NULL,
            profession VARCHAR NOT NULL,
            birth_date DATE NOT NULL,
            friend VARCHAR NOT NULL);
          """
    )

    populatetable_task = PostgresOperator(
        task_id="populatetable_task",
        postgres_conn_id='postgres',
        sql= """
            INSERT INTO EMP(name, profession, birth_date, friend)
            VALUES ('Max', 'Plumber', '1918-07-05', 'Jane'),
                   ('Susie', 'Engineer', '1919-05-01', 'Phil'),
                   ('Lester', 'Doctor', '1920-06-23', 'Lily'),
                   ('Quincy', 'Plumber', '1913-08-11', 'Anne');
            """
    )

    getusers_task = PostgresOperator(
        task_id="getusers_task",
        postgres_conn_id='postgres',
        sql= """
            SELECT * FROM EMP;    
            """
    )



createtable_task >> populatetable_task >> getusers_task
