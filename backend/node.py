from model import Cliente


class Node:
    def __init__(self, data: Cliente):
        self.data = data            
        self.next = None            

class Queue:
    def __init__(self):
        self.head = None          
        self.tail = None            
        self._size = 0
        
    def enqueue(self, cliente: Cliente):
        node = Node(cliente)
    
        if self.head is None:
            self.head = node
            self.tail = node
        
        else:
            if cliente.tipo == "Preferencial":
                node.next = self.head
                self.head = node
            else:
                self.tail.next = node
                self.tail = node
        self._size += 1
        return
        
    def dequeue(self):
        if self.head is None:
            return None
        removido = self.head.data
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        self._size -= 1
        return removido   
    
    def to_list(self):
        elementos = []
        valor = self.head
        while valor:
            elementos.append(valor.data.model_dump())
            valor = valor.next
        return elementos
    
    def remove_specific(self, nome: str):
        atual = self.head
        anterior = None
        if self.head is None:
            return None
        while atual:
            if nome == atual.data.nome:
                if anterior is None:
                    self.head = atual.next
                    if self.head is None:
                        self.tail = None
                else:
                    anterior.next = atual.next
                    if atual.next is None:
                        self.tail = anterior
                self._size -= 1
                return True
            anterior = atual
            atual = atual.next
            
        return False
    
fila_sistema = Queue()  
historico_sistema = []