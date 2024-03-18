import psycopg2

def connect():
    try:
      connection = psycopg2.connect(
          host="localhost",
          database="SchoolApplication",
          user="postgres",
          password="7685"
      )
      return connection
    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL", error)
        exit(1)


def close(con):
    if con is not None:
        con.close()
