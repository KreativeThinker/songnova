"""
Data handling for local user.
"""
import pymysql  # type:ignore

local_user_database = pymysql.connect(
    host="localhost",
    user="ghost",
    password="123"
)
cursor = local_user_database.cursor()
