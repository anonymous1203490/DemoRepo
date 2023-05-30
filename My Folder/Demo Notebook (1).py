# Databricks notebook source
print("Hello World!")

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC SELECT "hello world from SQL"

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC # Sample markdown table
# MAGIC (similar to Github readme)
# MAGIC
# MAGIC |user_id|user_name|
# MAGIC |-------|---------|
# MAGIC |   1   |   Adam  |

# COMMAND ----------

# MAGIC %md
# MAGIC ###### Run another notebook in this notebook using %run

# COMMAND ----------

# MAGIC %run ./Includes/Setup

# COMMAND ----------

full_name

# COMMAND ----------

# MAGIC %md
# MAGIC ###### Use magic command %fs to work with the file system

# COMMAND ----------

# MAGIC %fs ls '/databricks-datasets'

# COMMAND ----------

dbutils.help()

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC db.utils is good for interacting with the databricks file system or the environment

# COMMAND ----------

dbutils.fs.help()

# COMMAND ----------

files = dbutils.fs.ls('/databricks-datasets')

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC Note: dbutils is more useful than the fs command because you can use dbutils as part of python code

# COMMAND ----------

display(files)
#the display function renders the variable results in a tabular format

# COMMAND ----------

# using the revision history in a notebook, a user can easily delete using the trash symbol, so we can use repos which provide source control.
