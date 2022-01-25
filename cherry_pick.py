import json
from turtle import title
from priority_map import AlertPriorities
import 

types_to_subtypes_relations = {
    "AttackIndication": [
        "BlackMarket",
        "BotDataForSale",
    ],
    "DataLeakage": [
        "ConfidentialDocumentLeakage",
        "ConfidentialInformationExposed",
        "CredentialsLeakage",
        "ExposedMentionsOnGithub",
    ],
    "VIP": [
    "BlackMarket",
    ]
}

priority_map = AlertPriorities.templates

def process_map():
    type_weights = {}
    title_weights = {}

    for priority, values  in priority_map.items():
        for item in values:
            #create type and title weights 
            alert_type = item.get("alert_type")
            alert_subtype = item.get("alert_subtype")
            type_weights[",".join([alert_type,alert_subtype])] = 6 - priority 
            titles = item.get("title_identifiers")
            title_weights[",".join(titles)] = 6 - priority
    print(type_weights)
    print(title_weights)

# def get_cos_similarity(inp1, inp2):


# process_map()   
    
alerts = [
        {
            '_id': '000000001',
            'Title': 'A company\'s confidential document was exposed publicly',
            'Details': {
                'Type': 'DataLeakage',
                'SubType': 'ConfidentialDocumentLeakage'
            }
        },
        {
            '_id': '000000002',
            'Title': 'A bot server with credentials for a company',
            'Details': {
                'Type': 'AttackIndication',
                'SubType': 'BotDataForSale'
            }
        },
]



