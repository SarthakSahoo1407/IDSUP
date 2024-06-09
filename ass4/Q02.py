from collections import namedtuple
def generateNamedTuple():
    Roll_No=namedtuple("Roll_No",["Name","Branch","Year_Of_Admission"])
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
    Roll_No=generateNamedTuple()
    print('Named Tuple: Roll_No')
    for Roll in Roll_No:
        print(Roll)
    
main()