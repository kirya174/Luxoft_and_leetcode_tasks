from html import entities


class LogAnalyserException(Exception):
    def __init__(self,innerException):
        super().__init__()
        self.innerException = innerException
        
def log_analyser(name):
    try:
        with open(name,"r") as log:
            entities = log.readlines()
        # To Do...
        return (2,3)
    except FileNotFoundError as e:
        raise LogAnalyserException(e)      


def log_analyser0(name):
    with open(name,"r") as log:
        entries = log.readlines()
    #... To Do....
    return (2,3)

#log_analyser0("x:\\log.txt")

try:
    log_analyser("x:\\log.txt")
except LogAnalyserException as e:
    print(f"Error during log analyser, reason {e.innerException}")