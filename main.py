from servive import *
from conection import *
import asyncio
import time


async def main():
    await create_table()
    while True:
        n = int(input("\n1)create user\n2)get users\n3)change user: \n4)drop table\nChouse one: "))
        match n:
            case 1:
                await add_user(input("Enter your Full name: "), int(input("Enter your age: ")), input("Enter your email: "))
            case 2:
                users = await get_user()
                for user in users:
                    print(f"""
    id:{user["user_id"]}
    Fullname:{user["full_name"]}
    Age:{user["age"]}
    Email:{user["email"]}
                        """)
            case 3:
                name = input("Введите ваше имя: ")
                age = int(input("Введите ваш возраст: "))
                emial = input("введите ваш email: ")
                user_id = int(input("Введите ваш id: "))
                await change_users(name, age,emial, user_id)
            case 4:
                await drop_table()
                print("Table drop succesifull")
            case _:
                break
                        


if __name__ == "__main__":
    asyncio.run(main())