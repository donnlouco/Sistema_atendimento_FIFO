from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime

app = FastAPI()

class Node:
    def __init__(self, data=None):
        self.data = data            
        self.next = None            

class Queue:
    def __init__(self):
        self.head = None            # Início (próximo a ser chamado)
        self.tail = None            
        self._size = 0

    # Insere respeitando a regra de prioridade 
    def enqueue_by_priority(self, elem):
        node = Node(elem)
        
        # Fila Vazia
        if self.head is None:
            self.head = node
            self.tail = node
            self._size += 1
            return
        
        # Caso 2: O cliente é Normal 
        if elem["tipo"] == "Normal":
            self.tail.next = node
            self.tail = node
            self._size += 1
            return