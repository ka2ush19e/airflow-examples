# -*- coding: utf-8 -*-

from __future__ import absolute_import, print_function, division, unicode_literals
from airflow import DAG
from airflow.operators import DummyOperator
from airflow.utils import chain
from datetime import datetime, timedelta

yesterday = datetime.combine(datetime.today() - timedelta(7), datetime.min.time())

default_args = {
    'owner': 'airflow',
    'start_date': yesterday,
}

dag = DAG('sequence', default_args=default_args)

t1 = DummyOperator(task_id='task1', dag=dag)
t2 = DummyOperator(task_id='task2', dag=dag)
t3 = DummyOperator(task_id='task3', dag=dag)

chain(t1, t2, t3)
