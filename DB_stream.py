import streamlit as st
import sqlite3
import pandas as pd
from time import sleep



st.title("데이터 베이스 연동")

datastore = st.empty()

while True:

    conn = sqlite3.connect('bar_qr_DB.db')
    cursor = conn.cursor()
    select_sql = "SELECT name FROM sqlite_master WHERE type='table';"
    cursor.execute(select_sql)
    tables = cursor.fetchall() # 조회 결과 가져오기

    table_name = [table[0] for table in tables]

    query = f"SELECT * FROM {table_name[1]}"
    df = pd.read_sql_query(query, conn)
    conn.close()

    with datastore.container():
        st.dataframe(df)
    sleep(1)

