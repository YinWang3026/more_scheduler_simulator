# more_scheduler_simulator

- Implemented a Discrete Event Simulator to calculate the Job Completetion Time (JCT) for some randomly generated jobs
  - FCFS - First Come First Served
  - SRTF - Shortest Remaining Time First
  - SRF - Smallest Resource First
  - Lottery - Random selection
- To run the simulator `simulator.py -h -v -t -q -i <jobs.txt> -s <scheduler>`
  - Reads jobs from `jobs.txt`
  - h for help
  - v for general debugging information
  - q for printing scheduler queue
  - t for showing simulation traces
  - Scheduler names are listed above
- To generate random jobs `python/py/py.exe job_generator.py`
  - Produces `jobs.txt`
