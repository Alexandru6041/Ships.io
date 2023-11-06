import json

class Question:
    def __init__(self, statement:str, choices:tuple[str], correct:int):
        self.statement = statement
        self.choices = choices
        self.correct = correct
    
    def as_json(self) -> str:
        d = {'statement': self.statement, 'choices': list(self.choices), 'correct': self.correct}
        return json.dumps(d)
    
    def as_bytes(self) -> bytes:
        return self.as_json().encode()
    
    @staticmethod
    def from_json(data:str):
        d = json.loads(data)
        return Question(d['statement'], tuple(d['choices']), d['correct'])
