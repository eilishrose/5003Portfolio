import random
import operator
import matplotlib
import tkinter
matplotlib.use('TkAgg')
import matplotlib.pyplot
import AgentFramework
import time
import csv
import matplotlib.animation
import requests
import bs4

print("Start")

# Set the random seed to make the results reproducible and for testing and debugging purposes.

#random.seed(0)
#random.seed(1)

#Start time for raster processing
time_raster_start = time.process_time()

# Create lists for raster data
num_of_agents = 10
num_of_iterations = 100
neighbourhood = 20

# Set up lists
agents = []
environment =[]
td_ys = []
td_xs = []

#Figure for animating the agents
fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])

# Import raster data set and append data to list
f = open('in.txt', newline='' )
reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
for row in reader: 
    rowlist = []
    environment.append(rowlist)
    for value in row:
        rowlist.append(value)
        #print(value)
f.close()

#End time for raster processing
time_raster_end = time.process_time()

#Print raster processing time
time_raster = time_raster_end - time_raster_start
print("Time taken to process raster data", time_raster, "s") 

#Downloading x and y data
r = requests.get('http://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part9/data.html')
content = r.text                               
soup = bs4.BeautifulSoup(content, 'html.parser')
td_ys = soup.find_all(attrs={"class" : "y"})    #finds y
td_xs = soup.find_all(attrs={"class" : "x"})    #finds x
print(td_ys)                                    #prints y
print("\n", td_xs)                              #prints x                         

# Make the agents.
for i in range(num_of_agents):
    #agents.append(AgentFramework.Agent(random.randint(0,99),random.randint(0,99)))
    #agents.append(AgentFramework.Agent(environment, agents, random.randint(0,99), random.randint(0,99)))
    y = int(td_ys[i].text)
    x = int(td_xs[i].text)
    agents.append(AgentFramework.Agent(environment, agents, y, x))
    
num_of_agents = len(agents)
print("Number of agents", num_of_agents)

def update(frame_number):
    fig.clear()
    global carry_on
#Move the agents
#for j in range(num_of_iterations):
    for i in range(num_of_agents):
        agents[i].move()
        agents[i].eat()
        agents[i].share_with_neighbours(neighbourhood)
        
#Plot the agents

    matplotlib.pyplot.xlim(0, 99)
    matplotlib.pyplot.ylim(0, 99)
    matplotlib.pyplot.imshow(environment)
    for i in range(num_of_agents):
        matplotlib.pyplot.scatter(agents[i].x,agents[i].y)
        print(agents[i].y,agents[i].x)

#Function to run the animation
def run():
    '''
    Runs the animation.

    Returns
    -------
    None.

    '''
    animation=matplotlib.animation.FuncAnimation(fig, update, interval=1, repeat=False, frames=num_of_iterations)
    
    canvas.draw()
    
#Create GUI
root = tkinter.Tk()
root.wm_title("Model")
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

menu_bar = tkinter.Menu(root)
root.config(menu=menu_bar)
model_menu = tkinter.Menu(menu_bar)
menu_bar.add_cascade(label="Model", menu=model_menu)
model_menu.add_command(label="Run model", command=run) 
model_menu.add_command(label="Exit", command=root.destroy) #See references

#Terminates the loop 
def exiting(): 
    '''
    Terminates the loop when exiting the window

    Returns
    -------
    None.

    '''
    root.quit()
    root.destroy()

root.protocol('WM_DELETE_WINDOW', exiting)

tkinter.mainloop()

print("End")


