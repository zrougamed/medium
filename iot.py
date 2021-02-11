#!/usr/bin/python3
import sys
from typing import Optional, Any
import pyTigerGraphBeta as tg

def schema():
    res = conn.gsql("""
CREATE GRAPH ioT ()    
CREATE SCHEMA_CHANGE JOB change_schema_of_ioT  FOR GRAPH ioT {

ADD VERTEX Location (PRIMARY_ID Points STRING, Latitude FLOAT, Longitude FLOAT) WITH primary_id_as_attribute="TRUE"; 
ADD VERTEX Measurement (PRIMARY_ID meas_id STRING, dm_name STRING, dm_value FLOAT, dm_date STRING, dm_unit STRING, dm_abv_unit STRING)  WITH primary_id_as_attribute="TRUE"; 
ADD VERTEX Device (PRIMARY_ID device_id STRING, location_id STRING, topic STRING)  WITH primary_id_as_attribute="TRUE"; 
ADD VERTEX Topic (PRIMARY_ID  topic_name STRING, topic_description STRING, topic_type STRING)  WITH primary_id_as_attribute="TRUE";
ADD VERTEX MQTT (PRIMARY_ID  id STRING, topic STRING, payload STRING, datetime STRING)  WITH primary_id_as_attribute="TRUE";

ADD UNDIRECTED EDGE device_topic (FROM Device, TO Topic);
ADD UNDIRECTED EDGE measurement_topic (FROM Measurement, TO Topic);
ADD UNDIRECTED EDGE device_location (FROM Device, TO Location);
ADD UNDIRECTED EDGE device_measurement (FROM Device, TO Measurement);
    
}
RUN SCHEMA_CHANGE JOB change_schema_of_ioT
DROP JOB change_schema_of_ioT
""")
    for e in res:
        print(e)



def usage():
    print("the usage is :\n")
    print("python3 ioT.py <tag>.i.tgcloud.io tigergraph password")

server =sys.argv[1] 
user =sys.argv[2] 
password =sys.argv[3] 
if (server !="" and user != "" and password != ""):
    try:
        conn = tg.TigerGraphConnection(host=server,username=user,password=password,version="3.0.5")
        conn.getVer()
    except Exception as e:
        usage()
    print("DDL ...")
    schema()
    print("Schema ceated !")
else:
    usage()












