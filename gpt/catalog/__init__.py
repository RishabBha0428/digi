#created fork
from kubernetes import client, config
import numpy as np


# Load kubeconfig file
config.load_kube_config()

def create_catalog():
# Create an instance of the API class
#Code to get all the running pods, but how do I format this into the example above
#for example, I assumed that the input would be a space, and the output would be a series of digis within that space
#is that a right assumption, or are we looking for more
    #code to get the running space as well?
    v1 = client.CoreV1Api()

    namespace = 'default' 
    catalog =  {}

    pods = v1.list_namespaced_pod(namespace)
    for pod in pods.items:
        if pod.status.phase == "Running":
            name = pod.metadata.name
            filtered_name = name[:name.index('-')]
            catalog[filtered_name] = name
    return catalog

catalog = create_catalog()

#example database of examples, can be generated prettu simply by looking at yaml file and feeding to gpt to generate questions, or knowing predetermined questions
examples = [
    {"input": "Turn on the lamp 1", "output": "l1"},
    {"input": "Lower the brightness on lammp 1", "output": "l1"},
    {"input": "Turn off the lights in my main room", "output": "l1"},
    {"input": "Lower the temperature in my room", "output": "l1"}
]

from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import faiss
from langchain.prompts import SemanticSimilarityExampleSelector

to_vectorize = [" ".join(digi.values()) for digi in examples]
embeddings = OpenAIEmbeddings()
vectorstore = faiss.from_texts(to_vectorize, embeddings, metadatas=examples)

example_selector = SemanticSimilarityExampleSelector(
    vectorstore=vectorstore,
    k=2,
)
example_selector.select_examples({"input": "turn on the room"})["digi"]
