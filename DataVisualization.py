# Author: Derrick Joyce
# 10/22/2019
# Uses baby_names.csv and manipulates data to be visualized.

import matplotlib.pyplot as plt


class Datapoint:
    def __init__(self,year,gender,ethnicity,name,count,rank):
        self.year=year
        self.gender=gender
        self.ethnicity=ethnicity
        self.name=name
        self.count=count
        self.rank=rank
    
    def __repr__(self): #Basically a to string method
        return f"({self.name}, {self.gender}, {self.ethnicity})"
        
def load_data():
    data = []
    with open("baby_names.csv","r") as f:
        f.readline()
        for line in f:
            line = line.strip("\n").split(",")
            data.append(Datapoint(line[0], line[1],line[2],line[3], int(line[4]),(line[5])))
    return data
           
def plot_donut(data):
    labels = data.keys()
    values = [data[label] for label in labels]
    plt.pie(values,labels=labels)
    my_circle=plt.Circle((0,0),0.5,color='white')
    p=plt.gcf()
    p.gca().add_artist(my_circle)
    plt.show()
        
def plot_line(data): #plots the population over time in a line graph
    x = [key for key in data]
    x.sort()
    y = [data[label] for label in x]
    plt.plot(x,y)
    plt.show()
    
def plot_bar(data): #plots the population over time as a bar graph
    x = [key for key in data]
    y = [data[label] for label in x]
    plt.plot(x,y)
    plt.show()
    
if __name__ == "__main__": #'''main function'''
    data=load_data()
    #print(data)
    
    year = {}
    for person in data:
        if person.year in year:
            year[person.year]+=person.count
        else:
            year[person.year]=person.count
    plot_line(year)
    
    male, female=0,0
    for person in data:
        if person.gender =="FEMALE":
            female+=1
        else:
            male+=1
            
    print('Number of Males:',male, '\n'+ 'Number of Females:' ,female) #prints donut chart of males versus females
    plot_donut(dict({
            
            f'Male: {male/(male+female)*100}':male,
            f'Female: {female/(male+female)*100}':female
            }))
    
    ethnicities = dict() #Gathers the number of people in each ethnicity and plots
    for person in data:
        if(person.ethnicity in ethnicities):
            ethnicities[person.ethnicity]+=person.count
        else:
            ethnicities[person.ethnicity]=person.count
    print(ethnicities)
    plot_donut(ethnicities)
