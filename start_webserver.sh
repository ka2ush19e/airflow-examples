#!/bin/sh

export AIRFLOW_HOME=`pwd`/airflow
airflow webserver -p 8080
