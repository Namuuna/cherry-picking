import json
from priority_map import AlertPriorities
from input import alerts
import time 
import bisect 
import operator
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

class CherryPicking:
    def __init__(self):
        self.priority_map = AlertPriorities.templates
        self.type_weights = {}
        self.ordered_list = {}

    def process_map(self):
        title_weights = {}

        for priority, values  in self.priority_map.items():
            for item in values:
                temp = {}
                #create type and title weights 
                alert_type = item.get("alert_type")
                alert_subtype = item.get("alert_subtype")
                temp['Type'] = alert_type
                temp['SubType'] = alert_subtype
                self.type_weights[str(temp)] = 6 - priority

    def read_input(self):
        for alert in alerts:
            details = alert["Details"]
            priority = self.type_weights[str(details)]
            alert_id = alert["_id"]
            self.ordered_list[alert_id] = priority
        self.ordered_list = sorted(self.ordered_list.items(), key=operator.itemgetter(1))

    def get_top(self):
        pass

        
def get_cosine(x,y):
    pass

obj = CherryPicking()
obj.process_map()
obj.read_input()
obj.get_top()
    




