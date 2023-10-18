import dotenv
from os import getenv
import redis


dotenv.load_dotenv()

r = redis.Redis(
  host=getenv('REDIS_HOST'),
  port=getenv('REDIS_PORT'),
  password=getenv('REDIS_PW'),
#   ssl=True
)

r.set('foo', 'bar')
print(r.get('foo'))