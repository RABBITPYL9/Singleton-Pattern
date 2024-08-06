
import psycopg2

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
    

class Database(metaclass=Singleton):
    connection = None
    
    def connect(self):
        if self.connection is None:
            self.connection = psycopg2.connect(dbname='statsmon', user='admin', password='upt24', host='192.168.2.197')
            self.cursorobj = self.connection.cursor()
            self.execute = self.cursorobj.execute("""
                 update public.tests
                 set status = 'single'
                 where id = 315""")
            self.cursorobj.execute("commit;")
        return self.cursorobj




db1 = Database().connect()
print ("Database Objects DB1", db1)
