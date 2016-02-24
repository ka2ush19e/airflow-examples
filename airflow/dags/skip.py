# -*- coding: utf-8 -*-

from __future__ import absolute_import, print_function, division, unicode_literals
from airflow import DAG
from airflow.operators import DummyOperator, ShortCircuitOperator
from datetime import datetime, timedelta

yesterday = datetime.combine(datetime.today() - timedelta(7), datetime.min.time())

default_args = {
    'owner': 'airflow',
    'start_date': yesterday,
}

dag = DAG('skip', default_args=default_args)

t1 = DummyOperator(task_id='task1', dag=dag)
t2 = DummyOperator(task_id='task2', dag=dag)
t3 = DummyOperator(task_id='task3', dag=dag)

cond_true = ShortCircuitOperator(task_id='cond_t', python_callable=lambda: True, dag=dag)
cond_false = ShortCircuitOperator(task_id='cond_f', python_callable=lambda: False, dag=dag)

t1.set_downstream(cond_true)
cond_true.set_downstream(t2)

t1.set_downstream(cond_false)
cond_false.set_downstream(t3)
