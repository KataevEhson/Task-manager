from conection import *
import asyncio

async def add_user(full_name, age, email):
    conn = await connection()
    try:
        await conn.execute("""
        INSERT INTO users(full_name, age, email) VALUES
        ($1, $2, $3)  
            """, full_name, age, email)
        print("User added")
    except Exception as error:
        print(f"Add user error: {error}") 
    finally:
        await conn.close()
        
            
async def get_user():
    conn = await connection()
    try:
        users = await conn.fetch("""
        select * from users
            """)
        return users
    except Exception as error:
        print(f"Get user error: {error}") 
    finally:
        await conn.close()
        
async def change_users(full_name, age, email, user_id):
    conn = await connection()
    try:
        await conn.execute("""
            UPDATE users
            SET full_name = $1, age = $2, email = $3
            WHERE user_id = $4
        """, full_name, age, email, user_id)

    except Exception as erorr:

        print(f"Update error {erorr}")
    finally:
        await conn.close()



async def drop_table(user_id):
    conn = await connection()
    try:
        await conn.execute("""
    DROP TABLE users
    WHERE user_id = %s
""", (user_id))
    except Exception as erorr:
        print(f"drop file error {erorr}")

    finally:
        await conn.close()        


