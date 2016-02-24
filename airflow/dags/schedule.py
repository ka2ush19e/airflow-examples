# -*- coding: utf-8 -*-

from __future__ import absolute_import, print_function, division, unicode_literals
from airflow import DAG
from airflow.operators import DummyOperator
from datetime import datetime, timedelta

yesterday = datetime.combine(datetime.today() - timedelta(7), datetime.min.time())

default_args = {
    'owner': 'airflow',
    'start_date': yesterday,
}

dag = DAG('schedule', default_args=default_args, schedule_interval=timedelta(seconds=10))

t1 = DummyOperator(task_id='task1', dag=dag)
