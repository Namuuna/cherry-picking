from priority_map import AlertPriorities
from input import alerts
import operator
import timeit
import nltk
nltk.download('punkt')
from nltk.tokenize import word_tokenize


class CherryPicking:
    def __init__(self):
        self.priority_map = AlertPriorities.templates
        self.type_weights = {}
        self.title_weights = {}
        self.type_title = {}
        self.scored = {}
        self.process_map()

    def process_map(self):
        weight_coef = len(self.priority_map) + 1
        for priority, values in self.priority_map.items():
            for item in values:
                temp = {}
                #create type and title weights 
                alert_type = item.get("alert_type")
                alert_subtype = item.get("alert_subtype")
                temp['Type'] = alert_type
                temp['SubType'] = alert_subtype
                self.type_weights[str(temp)] = weight_coef- priority
                title_identifier = item.get("title_identifiers")[0]
                self.type_title[str(temp)] = title_identifier
                #recalculate weight for title identifier if repeated
                if title_identifier in self.title_weights:
                    weight = self.title_weights[title_identifier]
                    self.title_weights[title_identifier] = (weight_coef - weight + priority) // 2
                else:
                    self.title_weights[title_identifier] = weight_coef - priority

    def cherry_pick(self):        
        for alert in alerts:
            score = 0
            alert_id = alert["_id"]
            #get weight by type and subtype
            details = alert["Details"]
            priority_type = self.type_weights[str(details)]
            score += priority_type

            #get title weight 
            alert_title = alert["Title"]
            map_title = self.type_title[str(details)]
            #get cosine value
            cos_sim = get_cosine(alert_title, map_title)
            priority_title = self.title_weights[str(map_title)]
            #add title weight by multiplying by the coefficient (cosine similarity)
            score += (priority_title * cos_sim)

            self.scored[alert_id] = score

        self.scored = sorted(self.scored.items(), key=operator.itemgetter(1), reverse=True)
        if len(self.scored) > 4:
            self.scored = self.scored[:4]

        print(self.scored)
        return self.scored

  
def get_cosine(input1,input2):
    input1 = input1.lower()
    input2 = input2.lower()

    l1 = word_tokenize(input1) 
    l2 = word_tokenize(input2)
    s1, s2 = set(l1), set(l2)

    l1, l2 = [], []
    vec = s1.union(s2) 
    for w in vec:
        if w in s1: l1.append(1) 
        else: l1.append(0)
        if w in s2: l2.append(1)
        else: l2.append(0)
    c = 0

    for i in range(len(vec)):
            c+= l1[i]*l2[i]
    cosine = c / float((sum(l1)*sum(l2))**0.5)
    return cosine


alg = CherryPicking()
print(f"Execution time:",timeit.timeit('alg.cherry_pick()', 'from __main__ import CherryPicking, alg', number=1))
    




