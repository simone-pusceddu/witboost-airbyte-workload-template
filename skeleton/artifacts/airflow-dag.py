from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from cloudera.cdp.airflow.operators.cde_operator import CDEJobRunOperator
from cloudera.cdp.airflow.operators.cdw_operator import CDWOperator

default_args = {
    'owner': '${{ values.developmentGroup }}',
    'depends_on_past': False,
    'email': ['email@domain.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 0,
    'retry_delay': timedelta(minutes=5)
}

# NOTES:
#   - specify start_date and schedule interval considering that they are in UTC
#   - we recommend to check https://airflow.apache.org/docs/apache-airflow/1.10.15/dag-run.html for more information
#   - an Airflow DAG execution is run AFTER its associated data interval;
#     so if you set start_date as today and let's say schedule_interval at 2am (UTC), the next execution will be done tomorrow at 2am (UTC);
#     therefore if you want the first execution to happen today, set the start_date to yesterday
#   - we set catchup=False in order to not kick off a DAG Run for any interval that has not been run since the last execution date;
#     this does not work as expected, so make sure you set the start_date properly to exactly what you need.
#     if not, you will get two runs when you would expect one

dag = DAG(
    '${{ values.jobName }}',
    default_args=default_args,
    start_date=datetime(2021, 12, 16),  # THIS IS UTC
    schedule_interval='30 17 * * *', # THIS IS UTC
    catchup=False,
    is_paused_upon_creation=False
)


start = DummyOperator(task_id='start', dag=dag)

## OPERATOR EXAMPLES

# spark_job = CDEJobRunOperator(
#     task_id='cde_spark_job',
#     dag=dag,
#     job_name='airflow-spark-job',
# )

# hive_job = CDWOperator(
#     task_id='cdw_hive_job',
#     dag=dag,
#     cli_conn_id='hive-vw-connid',
#     hql="""
# show databases;
# """,
#     schema='schema_name',
#     use_proxy_user=False,
#     query_isolation=False
# )

end = DummyOperator(task_id='end', dag=dag)

start >> end
