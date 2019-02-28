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
    if (x["Type"] == "PERSON"):
       property="name"
    else:
       property="value"

    g.addV(x["Type"]).property(property, x["Text"]).next()
    g.V().has('kidnapping','case','33545').as_("a").V().has(x["Type"], property,x["Text"]).addE('evidence').to('a').next()

#print(g.V().valueMap().toList())


##### PREVISOUS CASES
g. \
addV('PERSON').property('name','Bill').property('birthdate', '1988-03-22'). \
addV('PERSON').property('name','Sarah').property('birthdate', '1992-05-03'). \
addV('PERSON').property('name','Ben').property('birthdate', '1989-10-21'). \
addV('PERSON').property('name','Lucy').property('birthdate', '1998-01-17'). \
addV('PERSON').property('name','Colin').property('birthdate', '2001-08-14'). \
addV('PERSON').property('name','Emily').property('birthdate', '1998-03-05'). \
addV('PERSON').property('name','Gordon').property('birthdate', '2002-12-04'). \
addV('PERSON').property('name','Kate').property('birthdate', '1995-02-12'). \
addV('PERSON').property('name','Peter').property('birthdate', '2001-02-27'). \
addV('PERSON').property('name','Terry').property('birthdate', '1989-10-02'). \
addV('PERSON').property('name','Alistair').property('birthdate', '1992-06-30'). \
addV('PERSON').property('name','Eve').property('birthdate', '2000-05-13'). \
addV('PERSON').property('name','Gary').property('birthdate', '1998-09-20'). \
addV('PERSON').property('name','Mary').property('birthdate', '1997-01-27'). \
addV('PERSON').property('name','Charlie').property('birthdate', '1989-11-02'). \
addV('PERSON').property('name','Sue').property('birthdate', '1994-03-08'). \
addV('PERSON').property('name','Arnold').property('birthdate', '2002-07-23'). \
addV('PERSON').property('name','Chloe').property('birthdate', '1988-11-04'). \
addV('PERSON').property('name','Henry').property('birthdate', '1996-03-15'). \
addV('PERSON').property('name','Josie').property('birthdate', '2003-08-21'). \
V().hasLabel('PERSON').has('name','Sarah').as_('a').V().hasLabel('PERSON').has('name','Bill').addE('FRIEND').to('a').property('strength',1). \
V().hasLabel('PERSON').has('name','Colin').as_('a').V().hasLabel('PERSON').has('name','Bill').addE('FRIEND').to('a').property('strength',2). \
V().hasLabel('PERSON').has('name','Terry').as_('a').V().hasLabel('PERSON').has('name','Bill').addE('FRIEND').to('a').property('strength',3). \
V().hasLabel('PERSON').has('name','Peter').as_('a').V().hasLabel('PERSON').has('name','Colin').addE('FRIEND').to('a').property('strength',1). \
V().hasLabel('PERSON').has('name','Kate').as_('a').V().hasLabel('PERSON').has('name','Ben').addE('FRIEND').to('a').property('strength',2). \
V().hasLabel('PERSON').has('name','Kate').as_('a').V().hasLabel('PERSON').has('name','Lucy').addE('FRIEND').to('a').property('strength',3). \
V().hasLabel('PERSON').has('name','Eve').as_('a').V().hasLabel('PERSON').has('name','Lucy').addE('FRIEND').to('a').property('strength',1). \
V().hasLabel('PERSON').has('name','Alistair').as_('a').V().hasLabel('PERSON').has('name','Kate').addE('FRIEND').to('a').property('strength',2). \
V().hasLabel('PERSON').has('name','Gary').as_('a').V().hasLabel('PERSON').has('name','Colin').addE('FRIEND').to('a').property('strength',3). \
V().hasLabel('PERSON').has('name','Gordon').as_('a').V().hasLabel('PERSON').has('name','Emily').addE('FRIEND').to('a').property('strength',1). \
V().hasLabel('PERSON').has('name','Alistair').as_('a').V().hasLabel('PERSON').has('name','Emily').addE('FRIEND').to('a').property('strength',3). \
V().hasLabel('PERSON').has('name','Terry').as_('a').V().hasLabel('PERSON').has('name','Gordon').addE('FRIEND').to('a').property('strength',3). \
V().hasLabel('PERSON').has('name','Alistair').as_('a').V().hasLabel('PERSON').has('name','Terry').addE('FRIEND').to('a').property('strength',1). \
V().hasLabel('PERSON').has('name','Gary').as_('a').V().hasLabel('PERSON').has('name','Terry').addE('FRIEND').to('a').property('strength',2). \
V().hasLabel('PERSON').has('name','Mary').as_('a').V().hasLabel('PERSON').has('name','Terry').addE('FRIEND').to('a').property('strength',3). \
V().hasLabel('PERSON').has('name','Henry').as_('a').V().hasLabel('PERSON').has('name','Alistair').addE('FRIEND').to('a').property('strength',1). \
V().hasLabel('PERSON').has('name','Sue').as_('a').V().hasLabel('PERSON').has('name','Eve').addE('FRIEND').to('a').property('strength',2). \
V().hasLabel('PERSON').has('name','Sue').as_('a').V().hasLabel('PERSON').has('name','Charlie').addE('FRIEND').to('a').property('strength',3). \
V().hasLabel('PERSON').has('name','Josie').as_('a').V().hasLabel('PERSON').has('name','Charlie').addE('FRIEND').to('a').property('strength',1). \
V().hasLabel('PERSON').has('name','Henry').as_('a').V().hasLabel('PERSON').has('name','Charlie').addE('FRIEND').to('a').property('strength',2). \
V().hasLabel('PERSON').has('name','Henry').as_('a').V().hasLabel('PERSON').has('name','Mary').addE('FRIEND').to('a').property('strength',3). \
V().hasLabel('PERSON').has('name','Mary').as_('a').V().hasLabel('PERSON').has('name','Gary').addE('FRIEND').to('a').property('strength',1). \
V().hasLabel('PERSON').has('name','Henry').as_('a').V().hasLabel('PERSON').has('name','Gary').addE('FRIEND').to('a').property('strength',2). \
V().hasLabel('PERSON').has('name','Chloe').as_('a').V().hasLabel('PERSON').has('name','Gary').addE('FRIEND').to('a').property('strength',3). \
V().hasLabel('PERSON').has('name','Henry').as_('a').V().hasLabel('PERSON').has('name','Arnold').addE('FRIEND').to('a').property('strength',1). \
V().hasLabel('PERSON').has('name','Alex Coqueiro').as_('a').V().hasLabel('PERSON').has('name','Sarah').addE('SAME_SCHOOL').to('a').property('strength',1). \
V().hasLabel('PERSON').has('name','Maria Hernan').as_('a').V().hasLabel('PERSON').has('name','Henry').addE('COWORKER').to('a').property('strength',1). \
next()

print(g.V().valueMap().toList())