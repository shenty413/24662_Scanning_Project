import http.client as httpc
import json
import time
import random

# http header
headers = { "charset" : "utf-8", "Content-Type": "application/json" }

while True:
    print("=== read ===")
    pdata = {}
    jdata = json.dumps(pdata, ensure_ascii = 'False')
    conn = httpc.HTTPConnection("cerlab29.andrew.cmu.edu")
    conn.request("POST", "/RSIoT-2018/rsiot05/rsiot05.php", jdata, headers) # read from DB
    response = conn.getresponse()
    result = response.read().decode()
    #print(response.read().decode()))
    #print(result)
    #pdata = json.loads(response.read().decode())
    pdata = json.loads(result)
    print(pdata[0]['Angle'])


    #print("=== write ===")
    # pdata = {"opr":"w", "Angle":random.random()}
    # jdata = json.dumps(pdata, ensure_ascii = 'False')
    # conn = httpc.HTTPConnection("cerlab29.andrew.cmu.edu")
    # conn.request("POST", "/RSIoT-2018/rsiot05/rsiot05.php", jdata, headers) # write to DB
    # response = conn.getresponse()
    #print(response.read().decode())

    time.sleep(1.0)

#pdata = json.loads(response.read().decode())
#ht2 = time.time();
#print("%.3fsec" % (t2-t1))
#print(pdata)



#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Point

def talker():
	pub = rospy.Publisher('chatter', Point, queue_size=10)
	rospy.init_node('talker', anonymous=True)
	rate = rospy.Rate(10) # 10hz
	while not rospy.is_shutdown():
		hello_str = "hello world %s" % rospy.get_time()
		rospy.loginfo(hello_str)
		pub.publish(hello_str)
		rate.sleep()

if __name__ == '__main__':
	try:
		talker()
	except rospy.ROSInterruptException:
		pass



# def talker():
# 	pub = rospy.Publisher('chatter', String, queue_size=10)
# 	rospy.init_node('talker', anonymous=True)
# 	rate = rospy.Rate(10) # 10hz
# 	while not rospy.is_shutdown():
# 		hello_str = "hello world %s" % rospy.get_time()
# 		rospy.loginfo(hello_str)
# 		pub.publish(hello_str)
# 		rate.sleep()

# if __name__ == '__main__':
# 	try:
# 		talker()
# 	except rospy.ROSInterruptException:
# 		pass


