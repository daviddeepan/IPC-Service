from elasticsearch import Elasticsearch, helpers
import json
import requests
import sys

es = Elasticsearch('https://localhost:9200')

def get_data_from_text_file(self):
    return [l.strip() for l in open(str(self), encoding="utf8", errors='ignore')]

docs = get_data_from_text_file("ipc_id.json") 
print ("String docs length:", len(docs))

doc_list =[]
for num, doc in enumerate(docs):
    try:
        dict_doc = json.loads(json.dumps([doc]))
        doc_list += [dict_doc]

    except json.decoder.JSONDecodeError as err:
# print the errors
        print ("ERROR for num:", num, "-- JSONDecodeError:", err, "for doc:", doc)

print ("Dict docs length:", len(doc_list))
print(doc_list)

# try:
#     print ("\nAttempting to index the list of docs using helpers.bulk()")
#     resp = helpers.bulk(
#         es,
#         doc_list,
#         index = "full_index",
#         doc_type = "_doc"
#     )

#     print ("helpers.bulk() RESPONSE:", resp)
#     print ("helpers.bulk() RESPONSE:", json.dumps(resp, indent=4))

# except Exception as err:
#     print("Elasticsearch helpers.bulk() ERROR:", err)
#     quit()    