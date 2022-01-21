from airflow import DAG, utils
from airflow.operators.ocean_spark import OceanSparkOperator

args = {
    "owner": "airflow",
    "email": [],
    "depends_on_past": False,
    "start_date": utils.dates.days_ago(0, second=1),
}


dag = DAG(dag_id="single-task", default_args=args, schedule_interval=None)

spark_pi_task = OceanSparkOperator(
    task_id="spark-pi",
    dag=dag,
    config_overrides={
        "type": "Scala",
        "sparkVersion": "3.2.0",
        "interactive": False,
        "image": "gcr.io/datamechanics/spark:platform-3.2-latest",
        "imagePullPolicy": "IfNotPresent",
        "mainClass": "org.apache.spark.examples.SparkPi",
        "mainApplicationFile": "local:///opt/spark/examples/jars/examples.jar",
        "arguments": ["10000"],
    },
)
