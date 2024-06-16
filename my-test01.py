from airflow import DAG
import datetime
import pendulum 
import airflow.decorators import dag
from airflow.operators.bash import BashOperator

#1 with as 문으로 DAG 선언(생성)

with DAG(
    dag_id="dags_bash_operator",
    schedule="0 0 * * *",
    start_date=pendulum.datetime(2024,6,10, tz="Asia/Seoul"),
    catchup=False
) as dag:
    bash_t1= BashOperator(
        task_id="bash_t1",
        bash_command="echo whoami"
    )

    bash_t2=BashOperator(
        task_id="bash_t2",
        bash_command="echo $HOSTNAME",

    )
    bash_t1 >> bash_t2

#2 표준생성자 이용하여 DAG선언
my_dag = DAG(
    dag_id="dags_bash_operator_standard"
    start_date=pendulum.datetime(2024,6,1),
    schedule=" 0 0 * * *",
    catchup=False,
    tags=["example", "example2"]
)

bash_t1=BashOperator(
            task_id="bash_t1",
            bash_command=" ",
            dag=my_dag)
bash_t1 >> bash_t2

#3 @데코레이터를 이용하여 DAG선언

@dag(start_date=datetime.datetime(2024,1,1), schedule=None, dag_id="dag_operator")

def generate_dag():
    bash_t1=BashOperator(task_id="bash_t1", bash_command="echo whoami")
    bash_t1 >> bash_t2

generate_dag()


