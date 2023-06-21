
# Docker & Kubernetes Assignment
The dags folder contains .py files for the dags created in correspondence to question-1. The .yaml files contains details of configuration required required for other tasks.

### Docker Task
1. Created a dag which adds the current time to the table at each run.
2. Below are importing statements required
      ```
      from airflow import DAG
      from datetime import datetime
      from airflow.providers.postgres.operators.postgres import PostgresOperator
      ```
3. Create table task, below is the code does it
  ```
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

    

createtable_task >> populatetable_task 

  ```
5. The following are the dependencies set in the dag.

```    
   create_table >> insert_value
```
### Snapshots
- Dag in the airflow
<img width="885" alt="Screenshot 2023-06-21 at 5 10 36 PM" src="https://github.com/chakradharsrinivas16/Docker_Assignment/assets/66582610/ad668455-6ce8-42f7-a10f-e3e7704d911a">

- Entries in the table

<img width="327" alt="Screenshot 2023-06-21 at 5 11 21 PM" src="https://github.com/chakradharsrinivas16/Docker_Assignment/assets/66582610/41bd634c-f4a8-4327-83fa-01a1abc63ae4">


### Kubernetes Task

Installed minikube to make a kubernetes cluster using the following commands.

```
brew install minikube
minikube start
```
Using the postgres-deployment.yaml file the pod containing postgres container was created.
To connect postgres and airflow install the dependencies in postgres container. We need to run below commands to open postgres container terminal.

```
kubectl apply -f postgres-deployment.yaml
minikube ssh
docker exec -it -u root postgres-container-id /bin/bash
```

```
apt-get -y update
apt-get  -y install build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev wget 
wget https://www.python.org/ftp/python/3.7.12/Python-3.7.12.tgz
tar -xf Python-3.7.12.tgz
cd /Python-3.7.12
./configure --enable-optimizations
make -j $(nproc)
make altinstall
# STEPS TO INSTALL AIRFLOW VERSION 2.5.0
apt-get install libpq-dev
pip3.7 install "apache-airflow[postgres]==2.5.0" --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-2.5.0/constraints-3.7.txt"
export AIRFLOW__CORE__SQL_ALCHEMY_CONN=postgresql://airflow:airflow@localhost:5432/airflow

airflow db init
airflow users create -u airflow -p airflow -f <fname> -l <lname> -e <mail> -r Admin
```

Then created a service of type clusterIP by running postgres-service.yaml to give access to postgres pods inside the cluster. The following command was used.

```
kubectl apply -f postgres-service.yaml
```

Using the airflow-deployment.yaml file the pod containing airflow container was made. The following command was used,
```
kubectl apply -f airflow-deployment.yaml
```

Creating dags and tasks in airflow scheduler.
```
minikube ssh
# for creating dag
docker exec -it -u root airflow-scheduler-id /bin/bash
cd dags
#installed vim by running these commands
apt-get update
apt install vim
vim time_task.py
# Write same dag file content here
```

Now, we can access the airflow webserver by running the command minikube service airflow. My airflow is accessible on below url Upon logging in, the dag was visible, then created a postgres connection and then ran my dag, it has been succesfully executed.

<img width="574" alt="Screenshot 2023-06-21 at 5 12 20 PM" src="https://github.com/chakradharsrinivas16/Docker_Assignment/assets/66582610/44f66f14-6f6a-4ca5-931f-21a82b7db970">

Dag looks like this - 
<img width="692" alt="Screenshot 2023-06-21 at 5 13 12 PM" src="https://github.com/chakradharsrinivas16/Docker_Assignment/assets/66582610/1c0a3dd0-cd90-473c-8994-f431aef9d664">

Validation of entry -

<img width="327" alt="Screenshot 2023-06-21 at 5 11 21 PM" src="https://github.com/chakradharsrinivas16/Docker_Assignment/assets/66582610/41bd634c-f4a8-4327-83fa-01a1abc63ae4">



