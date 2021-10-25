import plotly.express as px
import pandas as pd 
import os
from numpy import *

path = r'C:/Users/Vicky/Desktop/ANLY503/Assignment 5/eco/05/08'


def get_file():                
    files =os.listdir(path)
    files.sort()
    list= []
    for file in files:
        if not  os.path.isdir(path +file):   
            f_name = str(file)        
#             print(f_name)
            tr = '\\'  
            filename = path + tr + f_name        
            list.append(filename)  
    return list 

list = get_file()
list1 = []
for i in list:
    data = pd.read_csv(i).mean()
    list1.append(data)


value1 = [27,9,11,12,168,1,31,16]
value2 = [5,6,12,9,45,25,33,0.24]

import plotly.graph_objects as go
from plotly.subplots import make_subplots

labels1 = ['Fridge','Kitchen appliances','Lamp','Stereo and laptop','Freezer','Tablet','Entertainment','Microwave']
labels2 = ['Tablet','Coffee machine','Fountain','Microwave','Fridge','Entertainment','PC','Kettle']

fig = make_subplots(rows=1, cols=2, specs=[[{'type':'domain'}, {'type':'domain'}]])
fig.add_trace(go.Pie(labels=labels1, values=value1, name="Household 4"),
              1, 1)
fig.add_trace(go.Pie(labels=labels2, values=value2, name="Household 5"),
              1, 2)

fig.update_traces(hole=.4, hoverinfo="label+percent+name")

fig.update_layout(
    title_text="Average Plug Data of two households 2012-2013",
    annotations=[dict(text='Household 4', x=0.18, y=0.5, font_size=20, showarrow=False),
                 dict(text='Household 5', x=0.82, y=0.5, font_size=20, showarrow=False)])
fig.show()
fig.write_html("plotly.html")


    
    


