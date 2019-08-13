# MQTT-to-MYSQL-DB---Python-



**1 - INSTALL MYSQL CONNECTOR**
python3 -m pip install mysql-connector
or
pip3 install mysql-connector

**2 - INSTALL PAHO-MQTT**
python3 -m pip install paho-mqtt
or
pip3 install paho-mqtt

**3 - MYSQL CREDENTIALS**
set host,user,passwd,database

**4 - SUBSCRIBE TO TOPIC** 
  mqttc.subscribe("TOPIC_HERE", 0) 
 
**5 - Set TOPIC on_message if needed**
  if msg.topic =='TOPIC_HERE':
  
**6 - CREATE MY SQL TABLE - replace table_name**
CREATE TABLE table_name(id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, ts TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, temp VARCHAR(10) NOT NULL,humidity VARCHAR(10) NOT NULL, ec VARCHAR(10) NOT NULL, ph VARCHAR(10) NOT NULL);

**7 - MQTT MESSAGE FORMAT**
  mqtt message body is a dictionary/json object : {"temp":"27","humidity":"10","ec":"700","ph":"8"}


