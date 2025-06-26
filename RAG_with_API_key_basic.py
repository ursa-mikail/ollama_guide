#!pip install llama_cloud_services pydantic
import os
from llama_cloud_services import LlamaExtract
from pydantic import BaseModel, Field

# LLAMA_CLOUD_API_KEY =os.environ['LLAMA_CLOUD_API_KEY'] 

# Set Llama Cloud API key: https://cloud.llamaindex.ai/project/a8335057-cdbb-4dc6-a0db-ff3bc4105cd0/api-key
# Note: the following is ciphered key
os.environ['LLAMA_CLOUD_API_KEY'] = 'U2FsdGVkX1+Go4FQJJIPfXpHvcexn2WRe1lR+5m4A+KREJPmTY6qJvG/GYkHe7Aoc0w8I3Se6As/ZFv/gCPcj7CVrq2QOet6qMHrXUh1E7o='
LLAMA_CLOUD_API_KEY = os.environ['LLAMA_CLOUD_API_KEY']


class ExtractArtefacts(BaseModel):
    postcode: str = Field(description="Extract all of the US postcodes from the the document")
    ip_addresses: str = Field(description="Find all the IP address")
    email_address: str = Field(description="Find all the email addresses")
    bank_details: str = Field(description="Find all the bank details and sort codes")
    telephone: str= Field(description="Find all the telephone addresses and their location")
    passwords: str= Field(description="Find all the passwords")
    credit_card: str = Field(description="Find all the credit card details")
    mac_address: str = Field(description="Find all the MAC addresses")
    cities: str = Field(description="Find all the UK cities or towns")

llama_extract = LlamaExtract()

from llama_cloud.types import ExtractConfig, ExtractMode

config = ExtractConfig(use_reasoning=True,cite_sources=True, 
    extraction_mode=ExtractMode.MULTIMODAL)

agent = llama_extract.create_agent(name="artefact-parser", data_schema=ExtractArtefacts, config=config)
# agent = llama_extract.get_agent(name="artefact-parser")

artefact_info = agent.extract("example.pdf")
print(artefact_info.data)
print(artefact_info.extraction_metadata)


################################################################################################

# !pip install llama_cloud_services pydantic

import os
import uuid
from llama_cloud_services import LlamaExtract
from pydantic import BaseModel, Field
from llama_cloud.types import ExtractConfig, ExtractMode

# Set Llama Cloud API key: https://cloud.llamaindex.ai/project/a8335057-cdbb-4dc6-a0db-ff3bc4105cd0/api-key
# Note: the following is ciphered key
os.environ['LLAMA_CLOUD_API_KEY'] = 'U2FsdGVkX1+Go4FQJJIPfXpHvcexn2WRe1lR+5m4A+KREJPmTY6qJvG/GYkHe7Aoc0w8I3Se6As/ZFv/gCPcj7CVrq2QOet6qMHrXUh1E7o='

# Define schema for extraction
class ExtractArtefacts(BaseModel):
    names: str = Field(description="Find all names")

# Initialize the extractor and config
llama_extract = LlamaExtract()
config = ExtractConfig(
    use_reasoning=True,
    cite_sources=True,
    extraction_mode=ExtractMode.MULTIMODAL
)

agent_name = "artefact-parser"

# Try to get the agent or create it
try:
    agent = llama_extract.get_agent(name=agent_name)
    print(f"✅ Using existing agent: {agent_name}")
except Exception as e:
    if "404" in str(e):
        print(f"⚙️ Agent not found. Creating new agent: {agent_name}")
        agent = llama_extract.create_agent(
            name=agent_name,
            data_schema=ExtractArtefacts,
            config=config
        )
    else:
        raise RuntimeError(f"Agent retrieval/creation failed: {e}")

# Run extraction
pdf_path = "example.pdf"
if not os.path.exists(pdf_path):
    raise FileNotFoundError(f"❌ File not found: {pdf_path}")

artefact_info = agent.extract(pdf_path)

# Display results
print("📄 Extracted Data:")
print(artefact_info.data)

print("\n🧠 Extraction Metadata (Reasoning/Citations):")
print(artefact_info.extraction_metadata)

