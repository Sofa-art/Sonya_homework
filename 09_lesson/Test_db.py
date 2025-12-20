import pytest
import requests
from sqlalchemy import create_engine, inspect, text

db_connection_string = "postgresql://postgres:Zima2025#@localhost:5432/postgres"
db = create_engine(db_connection_string)

# Используем инспектор для получения информации о таблицах
def test_db_connection():
	inspector = inspect(db)
	names = inspector.get_table_names()
	assert names[0] == 'users'

# Добавляем нового студента
def test_insert():
    connection = db.connect()
    transaction = connection.begin()
    sql = text("INSERT INTO users(user_id, user_email) VALUES (:new_id, :new_email)")
    connection.execute(sql, {'new_id':14500,'new_email':'SkyPro@net.ru'})

# Удаляем нового студента
    sql=text("delete from users where user_id= :new_id")
    connection.execute(sql,{"new_id":14500})
    transaction.commit()
    connection.close()
    
#Изменяем id у студента
def test_update():
    connection = db.connect()
    transaction = connection.begin()
    sql = text("INSERT INTO users(user_id, user_email) VALUES (:new_id, :new_email)")
    connection.execute(sql, {'new_id':14500,'new_email':'SkyPro@net.ru'})
    sql = text("UPDATE users SET user_email= :email WHERE user_id = :id")
    connection.execute(sql, {"email": 'SkyPro@net.ru', "id": 14501})
    sql=text("delete from users where user_id= :new_id")
    connection.execute(sql,{"new_id":14501})

    transaction.commit()
    connection.close()

#Удаляем студента
def test_delete():
    connection = db.connect()
    transaction = connection.begin()
    sql = text("INSERT INTO users(user_id, user_email) VALUES (:new_id, :new_email)")
    connection.execute(sql, {'new_id':14500,'new_email':'SkyPro@net.ru'})
    sql = text("DELETE FROM users WHERE user_id = :id")
    connection.execute(sql, {"id": 14500})
    transaction.commit()
    connection.close()

	
    

	

