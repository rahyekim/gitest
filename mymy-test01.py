from airflow import DAG
import datetime
import pendulum
from airflow.operators.bash import BashOperator

with DAG(
    dag_id ="dags_bash_select_fruit"
    ,schedule=None
    ,start_time=(2024, 6,15, tz="Asia/Seoul")
    ,catchup=False
    ,tag="practice"

)as dag:
    
    t1_orange= BashOperator(
        task_id= "t1_orange"
        ,bash_command="bash /opt/airflow/plugins/shell/select_fruit.sh ORANGE"

    )

    t2_avocado= BashOperator(
        task_id= "t2_avocado"
        ,bash_command="bash /opt/airflow/plugins/shell/select_fruit.sh AVOCADO"


    )

    t1_orange >> t2_avocado