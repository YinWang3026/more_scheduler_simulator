from random import randint

currentTime = 0
with open("jobs.txt", 'w') as f:
    f.write("JobName ArrivalTime Work Tickets CPUs\n")
    for i in range(0, 26):
        if i != 0:
            f.write("\n")

        arrivialTime = randint(0, 5)
        work = randint(100, 1000)
        tickets = randint(10, 100)
        cpus = randint(1,8)
        currentTime += arrivialTime
        
        f.write("%c %d %d %d %d" % (chr(65+i), currentTime, work, tickets, cpus))
