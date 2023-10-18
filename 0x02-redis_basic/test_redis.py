import dotenv
from os import getenv
import redis


dotenv.load_dotenv()

r = redis.Redis()
r.ping()

r.set('foo', 'bar')
print(r.get('foo'))