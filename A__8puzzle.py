#Assignment 5 -- (8 PUZZLE PROBLEM --INFORMED SEARCH)
#Using A* Search
import copy
open_stack=[]
closed_list=[]
class puzzle(object):
    def _init_(self,initial,goal):
        self.parent=None
        self.level=0
        self.state_no=1
        self.curr=initial
        self.empty=self.getemptyindex()
        self.goal=goal
    def getemptyindex(self):
        for i in range(0,9):
            if (self.curr[i]==0):
                return i
    def compare(self,p2):
        for i in range(0,9,1):
            if self.curr[i]!=p2.curr[i]:
                return False
        return True
    #this is used while checking the closed list
    def display_state(self):
        self.state_no+=1
        for i in range(0,9,3):
            print(self.curr[i],"\t",self.curr[i+1],"\t",self.curr[i+2])
        print("\n")
    def isgoalreached(self):
        for i in range(0,9,1):
            if (self.curr[i]!=self.goal[i]):
                return False
        return True
    def displaysolution(self):
        print("------SOLUTION------")

        while (self.parent!=None):
            print("STATE ",self.state_no)
            self.display_state()
            self=self.parent
        print("STATE ",self.state_no)
        self.display_state()
    def heuristic_misplacedTiles(self):
        cnt=0
        for i in self.curr:
            if self.curr[i]!=self.goal[i]:
                cnt+=1
        return cnt
    def sort_parameter(self):
        return self.level+self.heuristic_misplacedTiles()
#below function is not being used
    def _lt_(self,other):
        if self.heuristic_misplacedTiles()<other.heuristic_misplacedTiles():
            return True
        else:
            return False
    #can be correct tiles or manhattan distance           
    #sorting methods -- operator overloading, sort it using new function, passing key  
    #actions
    #if has logic created for rules -- up,down,left and right here the (order)work on the empty spaces
    def up(self):
        
        if (self.empty-3>=0):
            print("Up being performed")
            self.curr[self.empty],self.curr[self.empty-3]=self.curr[self.empty-3],self.curr[self.empty]
            self.empty=self.empty-3
            if(self.isgoalreached()):
                print("Goal is reached")
            return True


        else:
            #print("Invalid Move")
            return False
        
    def down(self):
        
        if (self.empty+3<=8):
            print("Down being performed")
            self.curr[self.empty],self.curr[self.empty+3]=self.curr[self.empty+3],self.curr[self.empty]
            self.empty=self.empty+3
            if(self.isgoalreached()):
                print("Goal is reached")
            return True
            
        else:
            #print("Invalid Move")
            return False
    

    def left(self):
        
        if(self.empty%3!=0):
            print("Left being performed")
            self.curr[self.empty],self.curr[self.empty-1]=self.curr[self.empty-1],self.curr[self.empty]
            self.empty=self.empty-1
            if(self.isgoalreached()):
                print("Goal is reached")
            return True
            
        else:
            
            #print("Invalid Move")
            return False
        
    def right(self):
        
        if(self.empty%3!=2):
            print("Right being performed")
            self.curr[self.empty],self.curr[self.empty+1]=self.curr[self.empty+1],self.curr[self.empty]
            self.empty=self.empty+1
            if(self.isgoalreached()):
                print("Goal is reached")
            return True
            
        else:
            #print("Invalid Move")
            return False
def CheckClosedList(p1):
    for node in closed_list:
        if p1.compare(node):
            print("INSIDE CLOSED")
            return True
    return False           
def Afs(p1):
    open_stack.append(p1)
    while open_stack!=[]:
        open_stack.sort(key=lambda x: x.sort_parameter())
        current=open_stack.pop(0)#for bfs open_stack.pop(0)
        closed_list.append(current)
        #current.display_state()
        #below if is not needed as it is a part of the actions itself
        if(current.isgoalreached()):
            current.display_state()
            current.displaysolution()
            break

        new_state=copy.deepcopy(current)
        if (new_state.up() and CheckClosedList(new_state)==False):
            open_stack.append(new_state)
            new_state.parent=current
            new_state.level+=1
            new_state.display_state()
            if new_state.isgoalreached():
                new_state.displaysolution()
                break
        else:
            del new_state
                
        new_state=copy.deepcopy(current)
        if (new_state.down() and CheckClosedList(new_state)==False):
            open_stack.append(new_state)
            new_state.parent=current
            new_state.level+=1
            new_state.display_state()
            if new_state.isgoalreached():
                new_state.displaysolution()
                break
                
        else:
            del new_state
            
        new_state=copy.deepcopy(current)
        if (new_state.left() and CheckClosedList(new_state)==False):
            open_stack.append(new_state)
            new_state.parent=current
            new_state.level+=1
            new_state.display_state()
            if new_state.isgoalreached():
                new_state.displaysolution()
                break
        else:
            del new_state
                
        new_state=copy.deepcopy(current)
        if (new_state.right() and CheckClosedList(new_state)==False):
            open_stack.append(new_state)
            new_state.parent=current
            new_state.level+=1
            new_state.display_state()
            if new_state.isgoalreached():
                new_state.displaysolution()
                break
        else:
            del new_state
                



def main():
    #can be 1D or 2D Array
    initial=[2,8,1,0,4,3,7,6,5]
    goal=[1,2,3,8,0,4,7,6,5]
    open_stack=[]
    closed_list=[]
    p=puzzle(initial,goal)
    Afs(p)
    #Testing all moves and constraints
    
main()