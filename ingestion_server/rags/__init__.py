from ingestion_server.rags.lancedb_rag import LanceDB
from ingestion_server.rags.mongoDB_rag import MongoDB
from ingestion_server.rags.base import BaseRAG

from typing import Dict

RAGProviders : Dict[str, BaseRAG] = {
    "LanceDB": LanceDB,
    "MongoDB": MongoDB
}