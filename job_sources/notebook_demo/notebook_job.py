# Databricks notebook source

# COMMAND ----------

from pyspark.sql import SparkSession

# COMMAND ----------
dbutils.widgets.removeAll()
		
dbutils.widgets.text("env", "")
dbutils.widgets.text("day" , "")
		
env = dbutils.widgets.get("env")
day = dbutils.widgets.get("day")

print(f'This is a {env} job for the : {day}')