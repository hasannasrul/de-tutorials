from snowflake.snowpark import Session
from snowflake.snowpark.functions import *

connection_parameters = {
    "account": "DRNHDAY-JL77246",
    "user": "NASRULHASAN",
    "password" : "***REMOVED***",
    "role" : "ACCOUNTADMIN",
    "warehouse" : "SNOWFLAKE_LEARNING_WH",
    "database" : "SNOWFLAKE_LEARNING_DB",
    "schema" : "NASRULHASAN_LOAD_SAMPLE_DATA_FROM_S3"
}

session = Session.builder.configs(connection_parameters).create()
df = session.sql("SELECT TOP 10 * FROM menu")
df1 = df.select(col("MENU_ITEM_NAME"))
print(df1.show())

# Select specific columns and add a new derived column
df_transformed = df.select(
    col("MENU_ITEM_NAME"),
    upper(col("ITEM_CATEGORY")).alias("CATEGORY_UPPER"),
    length(col("MENU_ITEM_NAME")).alias("NAME_LENGTH")
)

df_transformed.show()

df_filtered = df.filter(col("SALE_PRICE_USD") > 2)
df_grouped = df_filtered.group_by("ITEM_CATEGORY").agg(
    avg(col("SALE_PRICE_USD")).alias("AVG_PRICE"),
    count("*").alias("ITEM_COUNT")
)

df_grouped.show()

df_grouped.write.save_as_table(
    "MENU_AGG_RESULTS",
    mode="overwrite"  # other option: 'append'
)