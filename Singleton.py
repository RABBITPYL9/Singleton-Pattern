
import psycopg2
#NEW

class Singleton(type):

    """
    Метакласс Singleton. Необходим для ограничения кол-ва инстансов класса (1 инстанс)
    Пример использованиея: class DbConnection(metaclass=Singleton): 
    """
    _instances = {}


    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class DDbConnection(metaclass=Singleton):
    def __init__(self):
        db_connection = psycopg2.connect(dbname='statsmon', user='admin', password='admin', host='localhost')
        
        cursor = db_connection.cursor()
        request = """
                 update public.tests
                 set status = 'single'
                 where id = 315"""
        cursor.execute(request)
        cursor.execute("commit;")


db_connect = DDbConnection()
