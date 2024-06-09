from dataclasses import dataclass
@dataclass
class Roll_No:
    name:str
    branch:str
    year_of_admission:int
def generateDataclass():
    Roll=[]
    R1=Roll_No('Rahul','C.S.E.',2017)
    Roll.append(R1)
    R2=Roll_No('Dabba','C.S.E.',2018)
    Roll.append(R2)
    R3=Roll_No('Soumya','C.S.E.',2019)
    Roll.append(R3)
    R4=Roll_No('Rituraj','C.S.E.',2020)
    Roll.append(R4)
    return Roll
    
def main():
    print('Dataclass:Roll_No')
    Roll=generateDataclass()
    for R in Roll:
        print(R)
        
main()