import streamlit as st
import mysql.connector
conn=mysql.connector.connect(
    
    
    host=st.secrets[""],
    root=st.secrets[""],
    database=st.secrets[""],
    password=st.secrets[""],
    port=st.secrets[""]
    
)


cursor=conn.cursor()

cursor.execute("""
               create table if not exists  users(
                   id int primary key auto_increment,
                   name varchar(50) not null,
                   email varchar(50) unique,
                   password varchar(50) not null
               )
               
               """)



cursor.execute("""
               create table if not exists files(
                   id int primary key auto_increment,
                   user_id int,
                   file_name varchar(255),
                   file_type varchar(100),
                   file_url text,
                   upload_date timestamp default current_timestamp,
                   foreign key(user_id) references user(id)
               )
               
               """)
conn.commit()

print("table created successfully")
