#created fork#created fork
import numpy as np
catalog = [
    {"input": "lounge", "output": ["lamp", "oven", "building", "rooms"]},
    {"input": "airport", "output": ["plane", "speaker", "cargo"]},

    {"input": "office", "output": ["fan", "phone", "plug", "underdesk"]},
]

from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import faiss
from langchain.prompts import SemanticSimilarityExampleSelector

to_vectorize = [" ".join(digi.values()) for digi in catalog]
embeddings = OpenAIEmbeddings()
vectorstore = faiss.from_texts(to_vectorize, embeddings, metadatas=catalog)

example_selector = SemanticSimilarityExampleSelector(
    vectorstore=vectorstore,
    k=2,
)

example_selector.select_examples({"input": "turn on the room"})["digi"]


"""
from kubernetes import client, config

config.load_incluster_config()()

v1=client.CoreV1Api()
print("Listing pods with their IPs:")
ret = v1.list_pod_for_all_namespaces(watch=False)
for i in ret.items:
    print("%s\t%s\t%s" % (i.status.pod_ip, i.metadata.namespace, i.metadata.name))

"""

