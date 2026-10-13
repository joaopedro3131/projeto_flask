import sqlite3
import psycopg2 

DB_PATH =  "postgresql://neondb_owner:npg_qxKr2TFbDG8t@ep-curly-rice-b8ov1iu6-pooler.c-14.us-east-1.aws.neon.tech/neondb?channel_binding=require&sslmode=require"

def get_connection():
    conn = psycopg2.connect(DB_PATH)
    return conn