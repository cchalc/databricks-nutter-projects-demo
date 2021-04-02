# Databricks notebook source
# JOD - adding a comment here
default_name = "DefaultUnknown"

dbutils.widgets.text("name", default_name, "Enter user name")
user_name = dbutils.widgets.get("name")
if user_name == "DefaultUnknown":
  greeting = "ERROR"
else:
  greeting = f"Hello {user_name}"
  
dbutils.notebook.exit(greeting)

# COMMAND ----------

# just a change
