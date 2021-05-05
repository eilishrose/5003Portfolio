import random

class Agent:
    
    
    # def __init__(self):
    #     self.y = random.randint(0,99)
    #     self.x = random.randint(0,99)   
        
    def __init__(self, environment, agents, y, x):
        '''
        Parameters
        ----------
        environment : TYPE
            environment that the agents are moving within
        agents : TYPE
            location of the agents
        y : TYPE
            y coordinate of the agents
        x : TYPE
            x coordinate of the agents

        Returns
        -------
        None.

        '''
        self.y = y
        self.x = x
        self.environment = environment
        self.store = 0
        self.agents = agents
       
    
    # Function to move agents
    def move(self):
        '''
        Random coordinates for the agents that are within the environment.

        Returns
        -------
        None.

        '''
        if random.random() < 0.5:
            self.y = (self.y + 1) % 100
        else:
            self.y = (self.y - 1) % 100

        if random.random() < 0.5:
            self.x = (self.x + 1) % 100
        else:
            self.x = (self.x - 1) % 100
            
        if random.random() < 0.5:
            self.y = (self.y + 1) % 100
        else:
            self.y = (self.y - 1) % 100

        if random.random() < 0.5:
            self.x = (self.x + 1) % 100
        else:
            self.x = (self.x - 1) % 100
            
    # Function to eat data
    def eat(self):
        '''
        Chooses how much an agent consumes based on the value.

        Returns
        -------
        None.

        '''
        if self.environment[self.y][self.x] > 10:
            self.environment[self.y][self.x] -= 10
            self.store += 10
            
    # Share with neighbours
    def share_with_neighbours(self, neighbourhood):
        '''
        Agents sharing distance between each other. 

        Parameters
        ----------
        neighbourhood : TYPE
            Checks, based on agents self store, whether the agents share with their neighbours.

        Returns
        -------
        None.

        '''
        for agent in self.agents:
             dist = self.distance_between(agent)
             if dist <= neighbourhood:
                #print("close, store before self", self.store, "other",agent.store)
                sum = self.store + agent.store
                ave = sum /2
                self.store = ave
                agent.store = ave
                #print("store after self", self.store, "store after",agent.store)
             #else:
                #print("far", dist)

    def distance_between(self, agent):
        '''
        Distance calculated between 'self' and 'agent'

        Parameters
        ----------
        agent : TYPE
            Agent to find the distance between.

        Returns
        -------
        TYPE
            Distance between 'self' and 'agent'
        '''
        return (((self.x - agent.x)**2) + ((self.y - agent.y)**2))**0.5