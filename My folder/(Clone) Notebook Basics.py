# Databricks notebook source
print("Hello")

# COMMAND ----------

# MAGIC %fs ls '/databricks-datasets'

# COMMAND ----------

dbutils.help()

# COMMAND ----------

files = dbutils.fs.ls('/databricks-datasets/')
print(files)

# COMMAND ----------

display(files)

# COMMAND ----------


