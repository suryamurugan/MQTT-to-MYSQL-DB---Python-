'''PYTHON SCRIPT TO SUBSCRIBE TO A TOPIC AND INSERT INTO MYSQL DATABASE'''


import mysql.connector
import paho.mqtt.client as mqtt
import json
import datetime


#SQL CONNECTOR 
mydb = mysql.connector.connect(
  host="localhost",
  user="USER_NAME",
  passwd="YOUR_PASSWORD_HERE",
  database="YOUR_DB_NAME"
)

mycursor = mydb.cursor()

#ON_CONNECT 
def on_connect(mqttc, obj, flags, rc):
    print("rc: " + str(rc))

# ON_MESSAGE 
# Example: 
#def on_message(mqttc, obj, msg):
#    print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))

def on_message(mqttc, obj, msg):
#TO INSERT FOR A PARTICULAR TOPIC BASED ON DB 
	if msg.topic =='TOPIC_HERE':
		print(msg.payload.decode("utf-8"))
		d=json.loads(msg.payload.decode("utf-8"))
		ts = datetime.datetime.now()
		temp = d.get("temp")
		humidity = d.get("humidity")
		ec = d.get("ec")
		ph = d.get("ph")
		ts = datetime.datetime.now()
		sql = "INSERT INTO flow_hypt(id,ts,temp,humidity,ec,ph) VALUES (NULL,%s,%s, %s,%s,%s)"
		val = (ts,temp,humidity,ec,ph)
		print("sql is ",sql)
		print("val is ",val)
		mycursor.execute(sql, val)
		mydb.commit()
		print(mycursor.rowcount, "record inserted.")
	else:
		print(msg.payload.decode("utf-8"))

# ON_PUBLISH 
def on_publish(mqttc, obj, mid):
    print("mid: " + str(mid))

#ON_ SUBSCRIBE
def on_subscribe(mqttc, obj, mid, granted_qos):
    print("Subscribed: " + str(mid) + " " + str(granted_qos))
#ON_LOG
def on_log(mqttc, obj, level, string):
    print(string)



# If you want to use a specific client id, use
# mqttc = mqtt.Client("client-id")
# but note that the client id must be unique on the broker. Leaving the client
# id parameter empty will generate a random id for you.
mqttc = mqtt.Client()
mqttc.on_message = on_message
mqttc.on_connect = on_connect
mqttc.on_publish = on_publish
mqttc.on_subscribe = on_subscribe
# Uncomment to enable debug messages
# mqttc.on_log = on_log
mqttc.connect("localhost", 1883, 60)
mqttc.subscribe("TOPIC_HERE", 0)

mqttc.loop_forever()



