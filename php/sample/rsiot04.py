import http.client as httpc
import json
import time

# http header
headers = { "charset" : "utf-8", "Content-Type": "application/json" }

print("=== read ===")
pdata = {}
jdata = json.dumps(pdata, ensure_ascii = 'False')
conn = httpc.HTTPConnection("cerlab29.andrew.cmu.edu")
conn.request("POST", "/RSIoT-2018/rsiot04/rsiot04.php", jdata, headers) # read from DB
response = conn.getresponse()
print(response.read().decode())

print("=== write ===")
pdata = {"opr":"w", "Line": 10}
jdata = json.dumps(pdata, ensure_ascii = 'False')
conn = httpc.HTTPConnection("cerlab29.andrew.cmu.edu")
conn.request("POST", "/RSIoT-2018/rsiot04/rsiot04.php", jdata, headers) # write to DB
response = conn.getresponse()
print(response.read().decode())

#pdata = json.loads(response.read().decode())
#ht2 = time.time();
#print("%.3fsec" % (t2-t1))
#print(pdata)
