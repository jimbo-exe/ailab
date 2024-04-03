# steepest hill climbing algorithm
import copy #to create deep copy of current state for children states.
import sys #for getting max int value 
open=None #empty global variable
closed_list=[]
flag=0 #when goal not reached

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

    def heuristic_misplacedTiles(self):
        cnt=0 #counting the number of misplaced tiles. lesser the misplaced tiles, the better.
        for i in self.current_state:
            if self.current_state[i]!=self.goal_state[i]:
                cnt=cnt+1
        return cnt

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
    open=p1 
    while open!=None:
        current=open 
        closed_list.append(current)
        print("current state popped from open:")
        current.display()

        if(current.isgoalreached()):
            #flag=1
            current.display()
            current.displaysolution()
            break
        #order of operations: down, up, right, left:
        maxx= sys.maxsize 
        #maxx=current.heuristic_misplacedTiles()
        next_state=None
        # stores max int value.
        # choose the child state with best heuristic value to be in open.
        new_state=copy.deepcopy(current)
        if (new_state.down() and CheckClosedList(new_state)==False and new_state.heuristic_misplacedTiles()<maxx):
            maxx=new_state.heuristic_misplacedTiles()
            next_state=new_state
        else:
            del new_state

        new_state=copy.deepcopy(current)
        if (new_state.up() and CheckClosedList(new_state)==False and new_state.heuristic_misplacedTiles()<maxx):
        
            # new_state.parent=current
            # new_state.empty_tile = new_state.getEmptyIndex()
            # new_state.display()
            maxx=new_state.heuristic_misplacedTiles()
            next_state=new_state
        else:
            del new_state

        new_state=copy.deepcopy(current)
        if (new_state.right() and CheckClosedList(new_state)==False and new_state.heuristic_misplacedTiles()<maxx):

            maxx=new_state.heuristic_misplacedTiles()
            next_state=new_state
        else:
            del new_state

        new_state=copy.deepcopy(current)
        if (new_state.left() and CheckClosedList(new_state)==False and new_state.heuristic_misplacedTiles()<maxx):
            maxx=new_state.heuristic_misplacedTiles()
            next_state=new_state
        else:
            del new_state

        open =None

        if(next_state !=None):
            next_state.parent=current
            next_state.empty_tile=next_state.getEmptyIndex()
            print("best child state for current state is:")
            next_state.display()
            open= next_state
        

def main():
    my_list=[2,0,3,1,8,4,7,6,5] #initial state.
    goal_list=[1,2,3,8,0,4,7,6,5]
    # my_list=[2,8,1,0,4,3,7,6,5]
    # goal_list=[1,2,3,8,0,4,7,6,5]
    closed_list=[]
    p=puzzle(my_list,goal_list) #object
    print("initial state:")
    p.display()
    print("Starting  steepest hill climb search: ")
    flag=0
    dfs(p)
    # if(flag!=1):
    #     print("goal not reached")

main()