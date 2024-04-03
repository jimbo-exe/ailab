#uninformed search.
import copy #to create deep copy of current state for children states.
open_stack=[]
closed_list=[]

class puzzle(object):
    def __init__(self, my_list, goal_list):
        self.current_state=my_list
        self.goal_state=goal_list
        self.empty_tile= self.getEmptyIndex()
        self.parent=None

    def getEmptyIndex(self):
        for i in range(9):
            if self.current_state[i]==0:
                return i #0 represents empty tile.

    def compare(self,p2):
        for i in range(0,9,1):
            if self.current_state[i]!=p2.current_state[i]:
                return False
        return True
    #this is used while checking the closed list

    def isgoalreached(self):
        for i in range(0,9,1):
            if (self.current_state[i]!=self.goal_state[i]):
                return False
        return True
    
    def displaysolution(self):
        print("------SOLUTION------")

        while (self.parent!=None):
            self.display()
            self=self.parent
        self.display()

    def down(self):
        #self.empty_tile= self.getEmptyIndex() #for task one, to perform moves on same state.
        if self.empty_tile != 6 and self.empty_tile !=7 and self.empty_tile !=8:
            temp= self.empty_tile # to store index of empty tile
            self.current_state[temp]=self.current_state[temp+3]
            self.current_state[temp+3]=0
            if(self.isgoalreached()):
                print("Goal is reached")
            return True
        else:
            #print("invalid move. cannot apply down move on lastr row")
            return False
    
    def up(self):
        #self.empty_tile= self.getEmptyIndex()
        if self.empty_tile !=0 and self.empty_tile !=1 and self.empty_tile !=2:
            temp= self.empty_tile
            self.current_state[temp]= self.current_state[temp-3]
            self.current_state[temp-3]=0
            if(self.isgoalreached()):
                print("Goal is reached")
            return True
        else:
            #print("invalid move. cannot perform up operation on first row")
            return False

    def right(self):
        #self.empty_tile= self.getEmptyIndex()
        if self.empty_tile !=2 and self.empty_tile!=5 and self.empty_tile!=8:
            temp= self.empty_tile
            self.current_state[temp]=self.current_state[temp+1]
            self.current_state[temp+1]=0
            if(self.isgoalreached()):
                print("Goal is reached")
            return True
        else:
            #print("invalid move. cannot perform right operation on last column")
            return False

    def left(self):
        self.empty_tile= self.getEmptyIndex()
        if self.empty_tile !=0 and self.empty_tile!=3 and self.empty_tile!=6:
            temp= self.empty_tile
            self.current_state[temp]=self.current_state[temp-1]
            self.current_state[temp-1]=0
            if(self.isgoalreached()):
                print("Goal is reached")
            return True
        else:
            #print("invalid move. cannot perform left operation on last column")
            return False

    def display(self):
        print("\n")
        for i in range(9):
            if(i==2 or i==5):
                
                print( self.current_state[i] , end =" \n")
            else:
                print(self.current_state[i], end =" ")


def CheckClosedList(p1):
    for node in closed_list:
        if p1.compare(node):
            print("INSIDE CLOSED")
            return True
        
    return False

def dfs(p1):
    open_stack.append(p1)

    while open_stack!=[]:
        current=open_stack.pop(0)#for bfs open_stack.pop(0). for dfs open_stack.pop()
        closed_list.append(current)
        print("current state popped from open:")
        current.display()

        if(current.isgoalreached()):
            current.display()
            current.displaysolution()
            break
        #order of operations: down, up, right, left:
        new_state=copy.deepcopy(current)
        if (new_state.down() and CheckClosedList(new_state)==False):
            open_stack.append(new_state)
            new_state.parent=current
            new_state.empty_tile = new_state.getEmptyIndex()
            new_state.display()
        else:
            del new_state

        new_state=copy.deepcopy(current)
        if (new_state.up() and CheckClosedList(new_state)==False):
            open_stack.append(new_state)
            new_state.parent=current
            new_state.empty_tile = new_state.getEmptyIndex()
            new_state.display()
        else:
            del new_state

        new_state=copy.deepcopy(current)
        if (new_state.right() and CheckClosedList(new_state)==False):
            open_stack.append(new_state)
            new_state.parent=current
            new_state.empty_tile = new_state.getEmptyIndex()
            new_state.display()
        else:
            del new_state

        new_state=copy.deepcopy(current)
        if (new_state.left() and CheckClosedList(new_state)==False):
            open_stack.append(new_state)
            new_state.parent=current
            new_state.empty_tile = new_state.getEmptyIndex()
            new_state.display()
        else:
            del new_state

def main():
    # my_list=[2,0,3,1,8,4,7,6,5] #initial state.
    # goal_list=[1,2,3,8,0,4,7,6,5]
    my_list=[2,8,1,0,4,3,7,6,5]
    goal_list=[1,2,3,8,0,4,7,6,5]
    open_stack=[]
    closed_list=[]
    p=puzzle(my_list,goal_list) #object
    print("initial state:")
    p.display()
    print("Starting uniform BFS: ")
    dfs(p)

main()