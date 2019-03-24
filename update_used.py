from conf import HOST_URL
from datetime import datetime
import requests

result = requests.get(HOST_URL + '/update/used')

with open('update_used.log', 'a') as f:
    f.write(str(datetime.utcnow()) + '---' + str(result.status_code) + '\n')
