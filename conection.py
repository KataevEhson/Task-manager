from dotenv import load_dotenv
import asyncpg
import os




load_dotenv()



password_db = os.getenv("PASSWORD_DB")

async def connection():
    try:
        conn = await asyncpg.connect(
                port = 5432,
                host = "localhost",                       
                user = "postgres",
                database = "task2_db",
                password = password_db
        )
        return conn
    except Exception as error:
        print(f"Connection error: {error}")
        raise





async def create_table():
    conn = await connection()
    try:
        await conn.execute("""
        CREATE TABLE IF NOT EXISTS users(
            user_id serial primary key,
            full_name varchar(100) not null,
            age int check(age >= 18),
            email varchar(100) unique,
            is_active boolean default true,
            created_at timestamp default now()
        )                
                    """)
        print("Created sucsses")
    except Exception as error:
        print(f"Create table error: {error}")
    finally:
        await conn.close()
        
