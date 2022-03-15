# more_scheduler_simulator

- Implemented a Discrete Event Simulator to calculate the Job Completetion Time (JCT) for some randomly generated jobs
  - FCFS - First Come First Served
  - SRTF - Shortest Remaining Time First
  - SRF - Shortest Resource First
  - Lottery
- To run the simulator `python/py/py.exe simulator.py -i <jobs.txt> -s <scheduler>`
  - Reads jobs from `jobs.txt`
- To generate random jobs `python/py/py.exe job_generator.py`
  - Produces `jobs.txt`
