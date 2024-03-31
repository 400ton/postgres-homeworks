import csv
import os
import psycopg2

bd = ['employees_data.csv', 'customers_data.csv', 'orders_data.csv']
bd_name = ['employees', 'customers', 'orders']


def add_data_in_bd(database, database_name):
    """Скрипт для заполнения данными таблиц в БД Postgres."""
    conn = psycopg2.connect(host='localhost', database='north', user='postgres', password='12345')
    cur = conn.cursor()
    for i in range(len(bd)):
        with open(os.path.join('north_data', database[i]), 'r') as csvfile:
            header = next(csvfile)
            csvreader = csv.reader(csvfile)
            for row in csvreader:
                values = '%s, ' * len(row)
                cur.execute(f"INSERT INTO {database_name[i]} VALUES ({values[:-2]})", row)
            conn.commit()
    cur.close()
    conn.close()


if __name__ == '__main__':
    add_data_in_bd(bd, bd_name)
