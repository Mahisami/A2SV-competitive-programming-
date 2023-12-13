class OrderedStream:

    def __init__(self, n: int):
        self.stream = [""] * (n + 1)
        self.total_elements = n
        self.pointer = 1
        
    def insert(self, id_key: int, value: str) -> List[str]:
        output = []
        self.stream[id_key] = value
        
       
        while self.pointer <= self.total_elements and self.stream[self.pointer] != "":
            output.append(self.stream[self.pointer])
            self.pointer += 1
        
        return output