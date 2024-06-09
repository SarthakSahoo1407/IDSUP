import random
import matplotlib.pyplot as plt
def generateRandomNumbers(number,start,end):
    random_numbers=[]
    for i in range(number):
        random_numbers.append(random.randint(start,end))
    return random_numbers
def main():
    number,start,end=100,1,100
    random_numbers=generateRandomNumbers(number,start,end)
    print('Generated Random Numbers:',random_numbers)
    plt.hist(random_numbers,bins=10,color='pink',edgecolor='red')
    plt.xlabel('Generated Random Numbers Range 1 to 100 Including')
    plt.ylabel('Frequency Count')
    plt.title('Generated Random Numbers Range 1 to 100 Including Vs Frequency Count')
    plt.show()

main()