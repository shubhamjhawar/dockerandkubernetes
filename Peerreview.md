## Sonali's Approach

### Docker Task:


It has tables which just add timestamps and it contains the insert and create table as a task in dag 
It has all the files in docker-compose.yaml also it has airflow-scheduler,webserver,flower etc
The Docker task involves creating a DAG (Directed Acyclic Graph) in Airflow that adds the current time to a table at each run.
The DAG is created using the DAG class from the airflow module. It is configured with a specific dag_id, start_date, schedule_interval, and catchup settings.
Within the DAG, there are two tasks defined using the PostgresOperator from the airflow.providers.postgres.operators.postgres module.


### Kubernetes Task:

The Kubernetes task involves deploying a PostgreSQL database and an Airflow container in a Kubernetes cluster using Minikube.

### Comparision:

We followed the similar approach but the insert table differed in which sonali just added timestamp
