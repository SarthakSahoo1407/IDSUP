def precision(TP,FP,FN,TN):
    return TP/(TP+FP)
def recall(TP,FP,FN,TN):
    return TP/(TP+FN)
def accuracy(TP,FP,FN,TN):
    correct=TP+TN
    total=TP+FP+FN+TN
    return correct/total
def f1_score(precision,recall):
    return 2*precision*recall/(precision+recall)
def genericFunction(TP,FP,FN,TN):
    p=precision(TP,FP,FN,TN)
    r=recall(TP,FP,FN,TN)
    a=accuracy(TP,FP,FN,TN)
    f1=f1_score(p,r)
    print('Precision:',p)
    print('Recall:',r)
    print('Accuracy:',a)
    print('F1 Score:',f1)
def main():
    TP,FP,FN,TN=250,750,500,250
    print('From Given Cunfusion Matrix Data,')
    genericFunction(TP,FP,FN,TN)
    TP=int(input('Enter TP Value: '))
    FP=int(input('Enter FP Value: '))
    FN=int(input('Enter FN Value: '))
    TN=int(input('Enter TN Value: '))
    print('From Given User Input Data,')
    genericFunction(TP,FP,FN,TN)
    
main()