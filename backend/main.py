from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime
from controller import Cliente

app = FastAPI()

class Node:
    def __init__(self, data: Cliente):
        self.data = data            
        self.next = None            

class Queue:
    def __init__(self):
        self.head = None          
        self.tail = None            
        self._size = 0

    # Insere respeitando a regra de prioridade 
    def enqueue(self, cliente: Cliente):
        node = Node(cliente)
        
        # Fila Vazia
        if self.head is None:
            self.head = node
            self.tail = node
        
        else:
            self.tail.next = node
            self.tail = node
        self._size += 1
        return
        
    def deque(self):
        if self.head is None:
            return None
        removido = self.head
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        self._size -= 1
        return removido   
    
    def listar(self):
        elementos = []
        valor = self.head
        while valor:
            elementos.append(valor.data)
            valor = valor.next
        return elementos
        
if __name__ == "__main__":  
    import uvicorn  
  
    uvicorn.run(app, host="localhost", port=8000)