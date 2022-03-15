from collections import deque
from enum import Enum, auto
import sys, getopt

class State(Enum):
    CREATED =  auto()
    READY = auto()
    RUNNING = auto()
    BLOCKED = auto()
    DONE = auto()

class Transition(Enum):
    TO_RUN = auto()
    TO_READY = auto()
    TO_BLOCK = auto()
    TO_PREEMPT = auto()
    TO_DONE = auto()

class Process:
    id = 0
    def __init__(self, name, at, cp, tickets, cpus, state, stateTS) -> None:
        self.id = id
        id += 1

        self.name = name
        self.arrivalTime = at
        self.finishTime = -1

        self.cpus = cpus
        self.cpuTime = cp
        self.tickets = tickets

        self.remainingCpuTime = cp

        self.state = state # State
        self.stateTS = stateTS # Time that process became this state

    def __repr__(self) -> str:
        return "Name: %s, AT: %d, CPU: %d, Tickets: %d, FT: " \
            % (self.name, self.arrivalTime, self.cpuTime, self.tickets, self.finishTime)

class Event:
    # Class variables
    id = 0
    def __init__(self, ts, proc, trans) -> None:
        self.evtID = id
        id += 1
        self.timeStamp = ts
        self.process = proc
        self.transition = trans # enum
    
    def __repr__(self) -> str:
        return "%d:%d,%s" % (self.timeStamp, self.process.id, self.transition.name)
    

class EventQueue:
    def __init__(self) -> None:
        self.queue = deque()
    
    def getEvent(self) -> Event: 
        if len(self.queue) == 0:
            return None

        return self.queue.popleft()
    
    def putEvent(self, evt) -> None:
        index = 0
        while index < len(self.queue):
            if evt.timeStamp < self.queue[index].timeStamp:
                break
            index += 1
        self.queue.insert(index, evt)
    
    def getNextEvtTime(self) -> int:
        if len(self.queue) == 0:
            return None
        
        return self.queue[0].timeStamp
    
    def __repr__(self) -> str:
        s = ""
        for i in range(0,len(self.queue)):
            s += self.queue[i].__repr__() + " "
        return s

class Scheduler:
    def __init__(self, quantum=10000, prio=4) -> None:
        self.quantum = quantum
        self.maxprio = prio
        self.queue = deque()
    
    def getProcess(self) -> Process:
        if len(self.queue) == 0:
            return None
        
        return self.queue.popleft()
        
class FCFS(Scheduler): # First Come First Served
    def __init__(self) -> None:
        super().__init__()

    def addProcess(self, process) -> None:
        self.queue.append(process)

    def __repr__(self) -> str:
        return "FCFS"
    
class SRTF: # Shortest Remaning Time First
    def __init__(self) -> None:
        super().__init__()

    def addProcess(self, process) -> None:
        pass

    def __repr__(self) -> str:
        return "SRTF"

class SRF: # Smallest Resource First
    def __init__(self) -> None:
        self.queue = deque()

    def addProcess(self, process) -> None:
        pass

    def __repr__(self) -> str:
        return "SRF"

class Lottery: # Random
    def __init__(self) -> None:
        self.queue = deque()

    def addProcess(self, process) -> None:
        pass

    def getProcess(self) -> Process:
        # Overriding parent method
        pass

    def __repr__(self) -> str:
        return "Lottery"

def main(argv):
    ifile = ''
    scheduler = None
    try:
        opts, args = getopt.getopt(argv,"hi:s:",["help, ifile=, sched="])
        # getopt.getopt(args, options, [long_options])
        # ":" indicates that an argument is needed, otherwise just an option, like -h
    except getopt.GetoptError:
        print('simulator.py -i <jobs.txt> -s <scheduler>')
        sys.exit(1)
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print('simulator.py -i <jobs.txt> -s <scheduler>')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            ifile = arg
        elif opt in ("-s", "--sched"):
            if arg == "FCFS":
                scheduler = FCFS()
            elif arg == "SRTF":
                scheduler = SRTF()
            elif arg == "SRF":
                scheduler = SRF()
            elif arg == "Lottery":
                scheduler = Lottery()
    
    if ifile == "":
        print('Missing input file, exiting')
        sys.exit()
    
    if scheduler == None:
        print('Missing scheduler or used invalid name')
        sys.exit()

    with open(ifile, 'r') as f:
        print(f.readline().strip())
        for line in f.readlines():
            line = line.strip().split()
            print(line)
    
    # d = deque(["one, two, three"])
    # for i in range(0, len(d)):
    #     print(d[i])

def simulate():
    pass

if __name__ == "__main__":
   main(sys.argv[1:])
