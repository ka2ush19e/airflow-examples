# -*- coding: utf-8 -*-

from __future__ import absolute_import, print_function, division, unicode_literals
from airflow import DAG
from airflow.operators import BranchPythonOperator, DummyOperator
from airflow.utils import chain
from datetime import datetime, timedelta
import random

yesterday = datetime.combine(datetime.today() - timedelta(7), datetime.min.time())

default_args = {
    'owner': 'airflow',
    'start_date': yesterday,
}

dag = DAG('branch', default_args=default_args)

t1 = DummyOperator(task_id='task1', dag=dag)

b1 = DummyOperator(task_id='branch1', dag=dag)
b2 = DummyOperator(task_id='branch2', dag=dag)
b3 = DummyOperator(task_id='branch3', dag=dag)

select = BranchPythonOperator(
    task_id='select',
    python_callable=lambda: random.choice(['branch1', 'branch2', 'branch3']),
    dag=dag
)

chain(t1, select)
chain(select, b1)
chain(select, b2)
chain(select, b3)
