import requests
import json
import datetime

today = datetime.date.today()
tomorrow = today + datetime.timedelta(days=1)
last_7d = today - datetime.timedelta(days=7)
raw = '{"template":"logstash-*","version":60001,"settings":{"index.refresh_interval":"5s"},"mappings":{"_default_":{"dynamic_templates":[{"message_field":{"path_match":"message","match_mapping_type":"string","mapping":{"type":"text","norms":false}}},{"string_fields":{"match":"*","match_mapping_type":"string","mapping":{"type":"text","norms":false,"fields":{"keyword":{"type":"keyword","ignore_above":256}}}}}],"properties":{"@timestamp":{"type":"date"},"@version":{"type":"keyword"},"geoip":{"dynamic":true,"properties":{"ip":{"type":"ip"},"location":{"type":"geo_point"},"latitude":{"type":"half_float"},"longitude":{"type":"half_float"}}}}}}}'
data = json.loads(raw)
create_index = requests.put('http://elasticsearch-client:9200/logstash-{}'.format(tomorrow.strftime('%Y.%m.%d')), json=data)
print(create_index.status_code)
print(create_index.content)
# Auto delete old log
#delete_index = requests.delete('http://elasticsearch-client:9200/logstash-{}'.format(last_4d.strftime('%Y.%m.%d')))
#print(delete_index.status_code)
#print(delete_index.content)
