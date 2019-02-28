from __future__  import print_function  # Python 2/3 compatibility

from gremlin_python import statics
from gremlin_python.structure.graph import Graph
from gremlin_python.process.graph_traversal import __
from gremlin_python.process.strategies import *
from gremlin_python.driver.driver_remote_connection import DriverRemoteConnection

import boto3
import json

### Read file
text_for_conversion = "crime.txt"
with open(text_for_conversion, 'r') as myfile:
    data=myfile.read().replace('\n', '')

#print (data)

comprehend = boto3.client(service_name='comprehend', region_name='us-east-1')
#print(json.dumps(comprehend.detect_key_phrases(Text=data, LanguageCode='en'), sort_keys=True, indent=4))
resultDict = comprehend.detect_entities(Text=data, LanguageCode='es')
graph = Graph()

#Insert data in the graph database
g = graph.traversal().withRemote(DriverRemoteConnection('wss://crime.cw8vc2udxxa2.us-east-1.neptune.amazonaws.com:8182/gremlin','g'))

g.V().drop().toSet()
g.addV('kidnapping').property('case','33545').property('city','Bogota').property('crime','Y').next()

for x in resultDict["Entities"]:
    g.addV(x["Type"]).property('value', x["Text"]).next()
    g.V().has('kidnapping','case','33545').as_("a").V().has(x["Type"],'value',x["Text"]).addE('evidence').to('a').next()
    
#print(g.V().valueMap().toList())
print(g.V().valueMap().toList())