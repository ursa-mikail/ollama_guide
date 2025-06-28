#install chromaDB
!pip install chromadb
!pip install sentence_transformers

data=[
1,"Founded in 1913 in Italy, this luxury automobile manufacturer has become synonymous with speed, elegance, and innovation. Renowned for its iconic prancing horse logo, it has a rich racing heritage and produces some of the most sought-after sports cars and supercars in the world.",
2,"Established in 1937 in Germany, this automobile giant is known for its engineering excellence, precision manufacturing, and cutting-edge technology. It offers a wide range of vehicles, from compact cars to luxury sedans and SUVs, and is recognized for its commitment to quality and performance.",
3,"With origins dating back to 1933 in Japan, this automotive company has grown into one of the largest and most influential in the world. It is celebrated for its reliability, fuel efficiency, and commitment to sustainability, producing a diverse lineup of cars, trucks, and hybrids.",
4,"This American automaker, founded in 1903, is a symbol of the nation's automotive industry. It has a storied history, from the introduction of the assembly line to iconic muscle cars and trucks. Today, it continues to innovate with electric and autonomous vehicles while honoring its heritage.",
5,"Founded in 1910 in France, this automotive brand is known for its elegance, luxury, and avant-garde design. It has a long history of producing high-end vehicles that blend performance with style, making it a favorite among discerning customers worldwide.",
6,"Originating in Sweden in 1927, this car manufacturer has built a reputation for safety, quality, and Scandinavian design. It is known for its commitment to innovation, including pioneering technologies such as turbocharging and autonomous driving features.",
7,"Established in 1909 in the United Kingdom, this iconic brand is synonymous with luxury, refinement, and timeless design. It has a long and distinguished history, producing some of the most iconic and desirable automobiles ever made.",
8,"This Japanese automaker, founded in 1937, has become one of the largest producers of vehicles in the world. It is known for its reliability, fuel efficiency, and advanced technology, offering a wide range of cars, trucks, and SUVs for consumers globally.",
9,"Founded in 1916 in Bavaria, Germany, this manufacturer has earned a reputation for producing high-performance, luxury vehicles that deliver both comfort and exhilarating driving experiences. It combines traditional craftsmanship with cutting-edge technology to create iconic automobiles.",
10,"Originating in Italy in 1963, this sports car manufacturer is famous for its sleek designs, powerful engines, and racing heritage. It has produced some of the most iconic and desirable sports cars in history, capturing the hearts of enthusiasts around the world.",
11,"Established in 1967 in Japan, this automotive brand has become synonymous with reliability, value, and innovation. It offers a diverse lineup of vehicles, from compact cars to hybrids and electric models, catering to a wide range of customers.",
12,"This luxury automobile manufacturer, founded in 1919 in Germany, is renowned for its engineering prowess, attention to detail, and uncompromising commitment to quality. It produces a range of luxury cars, including sedans, coupes, and SUVs, favored by discerning customers worldwide.",
13,"Founded in 1952 in Italy, this manufacturer is celebrated for its stylish and sporty cars, as well as its success in motorsports. It has a reputation for pushing the boundaries of automotive design and performance, creating some of the most iconic vehicles in the industry.",
14,"Originating in South Korea in 1967, this automotive brand has rapidly risen to prominence with its focus on quality, value, and innovation. It offers a diverse range of vehicles, including sedans, SUVs, and electric cars, catering to a global audience.",
15,"This British luxury car manufacturer, established in 1904, is renowned for its handcrafted automobiles, exquisite design, and unparalleled performance. It has a long-standing reputation for luxury and refinement, making it a symbol of automotive excellence.",
16,"Founded in 1926 in Sweden, this carmaker is known for its commitment to safety, environmental sustainability, and Scandinavian design. It has a strong reputation for producing reliable, practical cars with an emphasis on innovation and cutting-edge technology.",
17,"This Japanese multinational corporation, founded in 1933, is one of the largest automakers in the world. It is known for its diverse lineup of vehicles, including cars, trucks, hybrids, and electric vehicles, as well as its commitment to quality, innovation, and sustainability.",
18,"Originating in Italy in 1906, this manufacturer is renowned for its iconic sports cars, elegant grand tourers, and powerful engines. It has a long and storied history in motorsports, with numerous victories in prestigious races around the world.",
19,"Established in 1911 in Detroit, Michigan, this American automaker is one of the oldest and most iconic in the industry. It has played a significant role in shaping the automotive landscape, from introducing the mass-produced automobile to pioneering new technologies.",
20,"This Japanese automotive brand, founded in 1920, is known for its commitment to innovation, quality, and reliability. It offers a diverse lineup of vehicles, including compact cars, hybrids, and SUVs, catering to a global audience of customers.",
21,"Founded in 1954 in Germany, this luxury automobile manufacturer is renowned for its precision engineering, cutting-edge technology, and high-performance vehicles. It has a strong motorsport heritage and produces some of the most desirable cars on the road.",
22,"Originating in France in 1899, this automotive brand is known for its innovation, elegance, and distinctive design. It has a rich history of producing iconic vehicles, including luxury sedans, hatchbacks, and electric cars, with a focus on performance and style.",
23,"Established in 1917 in Italy, this manufacturer is synonymous with luxury, performance, and Italian style. It has a long history of producing some of the most desirable and exotic cars in the world, blending performance with elegance and craftsmanship.",
24,"This Japanese automaker, founded in 1933, is known for its commitment to quality, reliability, and advanced technology. It offers a diverse lineup of vehicles, including compact cars, hybrids, and SUVs, catering to a global customer base.",
25,"Founded in 1957 in Maranello, Italy, this manufacturer is synonymous with passion, performance, and racing heritage. It has a storied history in motorsports, with numerous victories in Formula One, and produces some of the most iconic sports cars in the world.",
26,"Originating in Munich, Germany, in 1916, this automotive brand is renowned for its luxury vehicles, high-performance engines, and technological innovation. It has a long history of producing iconic cars that combine driving pleasure with cutting-edge technology."
]

id_c=[]
description=[]
for e in range(0,len(data)):
    if e%2==0:
        id_c.append(data[e])
    else:
        description.append(data[e])
       
#create a dataframe
import pandas as pd
df=pd.DataFrame()
df["id"]=id_c
df["description"]=description
df

import chromadb
from chromadb import Documents
from chromadb.utils import embedding_functions


# create a database
client = chromadb.PersistentClient(path="/mnt/data/")


#load the transformer
sentence_transformer_ef = embedding_functions.SentenceTransformerEmbeddingFunction(model_name="microsoft/Orca-2-7b")
print("model loaded")

# create a table
collection = client.get_or_create_collection(name="test1")

# output=sentence_transformer_ef(tempsplits)
outputTotal=[]
descriptionTotal=[]
metadatas=[]
ids_t=[]

#!pip install gensim

from gensim.parsing.preprocessing import remove_stopwords
from gensim.parsing.preprocessing import preprocess_documents

for counter in range(0,df.shape[0]):
   

    ForEmbVector=preprocess_documents([df["description"][counter]])[0]
    text=""
    for each_w in ForEmbVector:
        text=text+" "+each_w
    text=text.rstrip().lstrip().strip()
    print("ForEmbVector: ",text)

    output=sentence_transformer_ef([text])
    description=df["description"][counter]
    meta={str(df["id"][counter]):str(len(df["description"][counter]))}
    id_c=df["id"][counter]

    
    outputTotal.append(output)
    descriptionTotal.append(description)
    metadatas.append(meta)
    ids_t.append(str(id_c))
    
    print(counter," done ")
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

print("Started")
for i in range(0,len(descriptionTotal)):
    collection.upsert(
        embeddings = outputTotal[i],
        documents = descriptionTotal[i],
        metadatas = [metadatas[i]],
        ids = ids_t[i]
    )
print("Finished")

# Initialize Chromadb client
sentence_transformer_ef = embedding_functions.SentenceTransformerEmbeddingFunction(model_name="microsoft/Orca-2-7b")
client = chromadb.PersistentClient(path="/mnt/data/")
collection = client.get_or_create_collection(
    name="test1", embedding_function=sentence_transformer_ef
)

# Perform the Chromadb query.

Query=preprocess_documents(["tell me about scandinavian car design"])[0]
Q=""
for each_w in Q:
    Q=Q+" "+each_w
Q=Q.rstrip().lstrip().strip()

results = collection.query(
    query_texts=[Q],
    n_results=1,
)

results["documents"]

doc=""
print(len(results["documents"][0]))
for e in results["documents"]:
    for con in e:
        doc=doc+con.rstrip().lstrip().strip()+" \n \n "

doc

!pip install langchain

import os
from langchain.llms import CTransformers
from langchain.prompts import PromptTemplate
from langchain.chains import MapReduceDocumentsChain, LLMChain, ReduceDocumentsChain, StuffDocumentsChain
import gc
import torch 
config = {'max_new_tokens': 200, 'temperature': 0.05, 'context_length': 1000}

llm = CTransformers(model='TheBloke/Mistral-7B-Instruct-v0.1-GGUF',model_file="mistral-7b-instruct-v0.1.Q4_K_M.gguf", config=config,threads=os.cpu_count(),gpu_layers=1)

template = """<s>[INST] You are a helpful, respectful and honest assistant.
You must summarize the {context} to answer the {question}. You must remove the irrelevant inforamtion to {question} from {context}:  
{context}
{question} [/INST] </s>
"""

#### Prompt
question_p = question
print("question: ",question_p)
context_p = doc 
print("context",context_p)
prompt = PromptTemplate(template=template, input_variables=["question","context"])
llm_chain = LLMChain(prompt=prompt, llm=llm)
response = llm_chain.run({"question":question_p,"context":context_p})

#    FinalAnswer=FinalAnswer+response+" \n ***************** \n"
print("✅")

print("=====================================================================")
print(response)
del llm_chain
del response
del llm
gc.collect()
torch.cuda.empty_cache() 



