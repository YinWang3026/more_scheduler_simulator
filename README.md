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
- FCFS Trace and Result
  
```FCFS
  currentTime: 5, procName: A, timeInPrevState: 0, from: State.CREATED to: READY
  currentTime: 5, procName: A, timeInPrevState: 0, from: State.READY to: RUN
  currentTime: 9, procName: B, timeInPrevState: 0, from: State.CREATED to: READY
  currentTime: 10, procName: C, timeInPrevState: 0, from: State.CREATED to: READY
  currentTime: 11, procName: D, timeInPrevState: 0, from: State.CREATED to: READY
  currentTime: 11, procName: E, timeInPrevState: 0, from: State.CREATED to: READY
  currentTime: 15, procName: F, timeInPrevState: 0, from: State.CREATED to: READY
  currentTime: 20, procName: G, timeInPrevState: 0, from: State.CREATED to: READY
  currentTime: 21, procName: H, timeInPrevState: 0, from: State.CREATED to: READY
  currentTime: 25, procName: I, timeInPrevState: 0, from: State.CREATED to: READY
  currentTime: 27, procName: J, timeInPrevState: 0, from: State.CREATED to: READY
  currentTime: 32, procName: K, timeInPrevState: 0, from: State.CREATED to: READY
  currentTime: 32, procName: L, timeInPrevState: 0, from: State.CREATED to: READY
  currentTime: 35, procName: M, timeInPrevState: 0, from: State.CREATED to: READY
  currentTime: 35, procName: N, timeInPrevState: 0, from: State.CREATED to: READY
  currentTime: 38, procName: O, timeInPrevState: 0, from: State.CREATED to: READY
  currentTime: 39, procName: P, timeInPrevState: 0, from: State.CREATED to: READY
  currentTime: 42, procName: Q, timeInPrevState: 0, from: State.CREATED to: READY
  currentTime: 42, procName: R, timeInPrevState: 0, from: State.CREATED to: READY
  currentTime: 47, procName: S, timeInPrevState: 0, from: State.CREATED to: READY
  currentTime: 48, procName: T, timeInPrevState: 0, from: State.CREATED to: READY
  currentTime: 51, procName: U, timeInPrevState: 0, from: State.CREATED to: READY
  currentTime: 55, procName: V, timeInPrevState: 0, from: State.CREATED to: READY
  currentTime: 58, procName: W, timeInPrevState: 0, from: State.CREATED to: READY
  currentTime: 63, procName: X, timeInPrevState: 0, from: State.CREATED to: READY
  currentTime: 65, procName: Y, timeInPrevState: 0, from: State.CREATED to: READY
  currentTime: 68, procName: Z, timeInPrevState: 0, from: State.CREATED to: READY
  currentTime: 197, procName: A, timeInPrevState: 192, from: State.RUN to: DONE
  currentTime: 197, procName: B, timeInPrevState: 188, from: State.READY to: RUN
  currentTime: 535, procName: B, timeInPrevState: 338, from: State.RUN to: DONE
  currentTime: 535, procName: C, timeInPrevState: 525, from: State.READY to: RUN
  currentTime: 694, procName: C, timeInPrevState: 159, from: State.RUN to: DONE
  currentTime: 694, procName: D, timeInPrevState: 683, from: State.READY to: RUN
  currentTime: 1467, procName: D, timeInPrevState: 773, from: State.RUN to: DONE
  currentTime: 1467, procName: E, timeInPrevState: 1456, from: State.READY to: RUN
  currentTime: 2415, procName: E, timeInPrevState: 948, from: State.RUN to: DONE
  currentTime: 2415, procName: F, timeInPrevState: 2400, from: State.READY to: RUN
  currentTime: 2723, procName: F, timeInPrevState: 308, from: State.RUN to: DONE
  currentTime: 2723, procName: G, timeInPrevState: 2703, from: State.READY to: RUN
  currentTime: 3258, procName: G, timeInPrevState: 535, from: State.RUN to: DONE
  currentTime: 3258, procName: H, timeInPrevState: 3237, from: State.READY to: RUN
  currentTime: 3537, procName: H, timeInPrevState: 279, from: State.RUN to: DONE
  currentTime: 3537, procName: I, timeInPrevState: 3512, from: State.READY to: RUN
  currentTime: 4468, procName: I, timeInPrevState: 931, from: State.RUN to: DONE
  currentTime: 4468, procName: J, timeInPrevState: 4441, from: State.READY to: RUN
  currentTime: 4769, procName: J, timeInPrevState: 301, from: State.RUN to: DONE
  currentTime: 4769, procName: K, timeInPrevState: 4737, from: State.READY to: RUN
  currentTime: 5396, procName: K, timeInPrevState: 627, from: State.RUN to: DONE
  currentTime: 5396, procName: L, timeInPrevState: 5364, from: State.READY to: RUN
  currentTime: 5716, procName: L, timeInPrevState: 320, from: State.RUN to: DONE
  currentTime: 5716, procName: M, timeInPrevState: 5681, from: State.READY to: RUN
  currentTime: 6210, procName: M, timeInPrevState: 494, from: State.RUN to: DONE
  currentTime: 6210, procName: N, timeInPrevState: 6175, from: State.READY to: RUN
  currentTime: 6520, procName: N, timeInPrevState: 310, from: State.RUN to: DONE
  currentTime: 6520, procName: O, timeInPrevState: 6482, from: State.READY to: RUN
  currentTime: 6713, procName: O, timeInPrevState: 193, from: State.RUN to: DONE
  currentTime: 6713, procName: P, timeInPrevState: 6674, from: State.READY to: RUN
  currentTime: 7290, procName: P, timeInPrevState: 577, from: State.RUN to: DONE
  currentTime: 7290, procName: Q, timeInPrevState: 7248, from: State.READY to: RUN
  currentTime: 8005, procName: Q, timeInPrevState: 715, from: State.RUN to: DONE
  currentTime: 8005, procName: R, timeInPrevState: 7963, from: State.READY to: RUN
  currentTime: 8535, procName: R, timeInPrevState: 530, from: State.RUN to: DONE
  currentTime: 8535, procName: S, timeInPrevState: 8488, from: State.READY to: RUN
  currentTime: 8849, procName: S, timeInPrevState: 314, from: State.RUN to: DONE
  currentTime: 8849, procName: T, timeInPrevState: 8801, from: State.READY to: RUN
  currentTime: 9644, procName: T, timeInPrevState: 795, from: State.RUN to: DONE
  currentTime: 9644, procName: U, timeInPrevState: 9593, from: State.READY to: RUN
  currentTime: 10606, procName: U, timeInPrevState: 962, from: State.RUN to: DONE
  currentTime: 10606, procName: V, timeInPrevState: 10551, from: State.READY to: RUN
  currentTime: 10975, procName: V, timeInPrevState: 369, from: State.RUN to: DONE
  currentTime: 10975, procName: W, timeInPrevState: 10917, from: State.READY to: RUN
  currentTime: 11823, procName: W, timeInPrevState: 848, from: State.RUN to: DONE
  currentTime: 11823, procName: X, timeInPrevState: 11760, from: State.READY to: RUN
  currentTime: 12280, procName: X, timeInPrevState: 457, from: State.RUN to: DONE
  currentTime: 12280, procName: Y, timeInPrevState: 12215, from: State.READY to: RUN
  currentTime: 12655, procName: Y, timeInPrevState: 375, from: State.RUN to: DONE
  currentTime: 12655, procName: Z, timeInPrevState: 12587, from: State.READY to: RUN
  currentTime: 13002, procName: Z, timeInPrevState: 347, from: State.RUN to: DONE
  Results
  Name: A, AT: 5, Work: 192, Tickets: 95, Resource: 1, ExecStartTime: 5, FinishTime: 197, WaitTime: 0, JCT: 1.00
  Name: B, AT: 9, Work: 338, Tickets: 78, Resource: 5, ExecStartTime: 197, FinishTime: 535, WaitTime: 188, JCT: 1.56
  Name: C, AT: 10, Work: 159, Tickets: 31, Resource: 8, ExecStartTime: 535, FinishTime: 694, WaitTime: 525, JCT: 4.30
  Name: D, AT: 11, Work: 773, Tickets: 29, Resource: 7, ExecStartTime: 694, FinishTime: 1467, WaitTime: 683, JCT: 1.88
  Name: E, AT: 11, Work: 948, Tickets: 93, Resource: 2, ExecStartTime: 1467, FinishTime: 2415, WaitTime: 1456, JCT: 2.54
  Name: F, AT: 15, Work: 308, Tickets: 37, Resource: 3, ExecStartTime: 2415, FinishTime: 2723, WaitTime: 2400, JCT: 8.79
  Name: G, AT: 20, Work: 535, Tickets: 86, Resource: 6, ExecStartTime: 2723, FinishTime: 3258, WaitTime: 2703, JCT: 6.05
  Name: H, AT: 21, Work: 279, Tickets: 95, Resource: 1, ExecStartTime: 3258, FinishTime: 3537, WaitTime: 3237, JCT: 12.60
  Name: I, AT: 25, Work: 931, Tickets: 28, Resource: 6, ExecStartTime: 3537, FinishTime: 4468, WaitTime: 3512, JCT: 4.77
  Name: J, AT: 27, Work: 301, Tickets: 44, Resource: 2, ExecStartTime: 4468, FinishTime: 4769, WaitTime: 4441, JCT: 15.75
  Name: K, AT: 32, Work: 627, Tickets: 67, Resource: 1, ExecStartTime: 4769, FinishTime: 5396, WaitTime: 4737, JCT: 8.56
  Name: L, AT: 32, Work: 320, Tickets: 84, Resource: 5, ExecStartTime: 5396, FinishTime: 5716, WaitTime: 5364, JCT: 17.76
  Name: M, AT: 35, Work: 494, Tickets: 58, Resource: 6, ExecStartTime: 5716, FinishTime: 6210, WaitTime: 5681, JCT: 12.50
  Name: N, AT: 35, Work: 310, Tickets: 82, Resource: 4, ExecStartTime: 6210, FinishTime: 6520, WaitTime: 6175, JCT: 20.92
  Name: O, AT: 38, Work: 193, Tickets: 36, Resource: 1, ExecStartTime: 6520, FinishTime: 6713, WaitTime: 6482, JCT: 34.59
  Name: P, AT: 39, Work: 577, Tickets: 84, Resource: 3, ExecStartTime: 6713, FinishTime: 7290, WaitTime: 6674, JCT: 12.57
  Name: Q, AT: 42, Work: 715, Tickets: 49, Resource: 3, ExecStartTime: 7290, FinishTime: 8005, WaitTime: 7248, JCT: 11.14
  Name: R, AT: 42, Work: 530, Tickets: 38, Resource: 4, ExecStartTime: 8005, FinishTime: 8535, WaitTime: 7963, JCT: 16.02
  Name: S, AT: 47, Work: 314, Tickets: 66, Resource: 5, ExecStartTime: 8535, FinishTime: 8849, WaitTime: 8488, JCT: 28.03
  Name: T, AT: 48, Work: 795, Tickets: 91, Resource: 2, ExecStartTime: 8849, FinishTime: 9644, WaitTime: 8801, JCT: 12.07
  Name: U, AT: 51, Work: 962, Tickets: 82, Resource: 5, ExecStartTime: 9644, FinishTime: 10606, WaitTime: 9593, JCT: 10.97
  Name: V, AT: 55, Work: 369, Tickets: 41, Resource: 3, ExecStartTime: 10606, FinishTime: 10975, WaitTime: 10551, JCT: 29.59
  Name: W, AT: 58, Work: 848, Tickets: 96, Resource: 3, ExecStartTime: 10975, FinishTime: 11823, WaitTime: 10917, JCT: 13.87
  Name: X, AT: 63, Work: 457, Tickets: 37, Resource: 3, ExecStartTime: 11823, FinishTime: 12280, WaitTime: 11760, JCT: 26.73
  Name: Y, AT: 65, Work: 375, Tickets: 50, Resource: 7, ExecStartTime: 12280, FinishTime: 12655, WaitTime: 12215, JCT: 33.57
  Name: Z, AT: 68, Work: 347, Tickets: 53, Resource: 8, ExecStartTime: 12655, FinishTime: 13002, WaitTime: 12587, JCT: 37.27
  Scheduler: FCFS, Average JCT: 14.82
```

- SRTF Trace and Result

```SRTF
  currentTime: 5, procName: A, timeInPrevState: 0, from: State.CREATED to: READY
  currentTime: 5, procName: A, timeInPrevState: 0, from: State.READY to: RUN
  currentTime: 9, procName: B, timeInPrevState: 0, from: State.CREATED to: READY
  currentTime: 10, procName: C, timeInPrevState: 0, from: State.CREATED to: READY
  currentTime: 11, procName: D, timeInPrevState: 0, from: State.CREATED to: READY
  currentTime: 11, procName: E, timeInPrevState: 0, from: State.CREATED to: READY
  currentTime: 15, procName: F, timeInPrevState: 0, from: State.CREATED to: READY
  currentTime: 20, procName: G, timeInPrevState: 0, from: State.CREATED to: READY
  currentTime: 21, procName: H, timeInPrevState: 0, from: State.CREATED to: READY
  currentTime: 25, procName: I, timeInPrevState: 0, from: State.CREATED to: READY
  currentTime: 27, procName: J, timeInPrevState: 0, from: State.CREATED to: READY
  currentTime: 32, procName: K, timeInPrevState: 0, from: State.CREATED to: READY
  currentTime: 32, procName: L, timeInPrevState: 0, from: State.CREATED to: READY
  currentTime: 35, procName: M, timeInPrevState: 0, from: State.CREATED to: READY
  currentTime: 35, procName: N, timeInPrevState: 0, from: State.CREATED to: READY
  currentTime: 38, procName: O, timeInPrevState: 0, from: State.CREATED to: READY
  currentTime: 39, procName: P, timeInPrevState: 0, from: State.CREATED to: READY
  currentTime: 42, procName: Q, timeInPrevState: 0, from: State.CREATED to: READY
  currentTime: 42, procName: R, timeInPrevState: 0, from: State.CREATED to: READY
  currentTime: 47, procName: S, timeInPrevState: 0, from: State.CREATED to: READY
  currentTime: 48, procName: T, timeInPrevState: 0, from: State.CREATED to: READY
  currentTime: 51, procName: U, timeInPrevState: 0, from: State.CREATED to: READY
  currentTime: 55, procName: V, timeInPrevState: 0, from: State.CREATED to: READY
  currentTime: 58, procName: W, timeInPrevState: 0, from: State.CREATED to: READY
  currentTime: 63, procName: X, timeInPrevState: 0, from: State.CREATED to: READY
  currentTime: 65, procName: Y, timeInPrevState: 0, from: State.CREATED to: READY
  currentTime: 68, procName: Z, timeInPrevState: 0, from: State.CREATED to: READY
  currentTime: 197, procName: A, timeInPrevState: 192, from: State.RUN to: DONE
  currentTime: 197, procName: C, timeInPrevState: 187, from: State.READY to: RUN
  currentTime: 356, procName: C, timeInPrevState: 159, from: State.RUN to: DONE
  currentTime: 356, procName: O, timeInPrevState: 318, from: State.READY to: RUN
  currentTime: 549, procName: O, timeInPrevState: 193, from: State.RUN to: DONE
  currentTime: 549, procName: H, timeInPrevState: 528, from: State.READY to: RUN
  currentTime: 828, procName: H, timeInPrevState: 279, from: State.RUN to: DONE
  currentTime: 828, procName: J, timeInPrevState: 801, from: State.READY to: RUN
  currentTime: 1129, procName: J, timeInPrevState: 301, from: State.RUN to: DONE
  currentTime: 1129, procName: F, timeInPrevState: 1114, from: State.READY to: RUN
  currentTime: 1437, procName: F, timeInPrevState: 308, from: State.RUN to: DONE
  currentTime: 1437, procName: N, timeInPrevState: 1402, from: State.READY to: RUN
  currentTime: 1747, procName: N, timeInPrevState: 310, from: State.RUN to: DONE
  currentTime: 1747, procName: S, timeInPrevState: 1700, from: State.READY to: RUN
  currentTime: 2061, procName: S, timeInPrevState: 314, from: State.RUN to: DONE
  currentTime: 2061, procName: L, timeInPrevState: 2029, from: State.READY to: RUN
  currentTime: 2381, procName: L, timeInPrevState: 320, from: State.RUN to: DONE
  currentTime: 2381, procName: B, timeInPrevState: 2372, from: State.READY to: RUN
  currentTime: 2719, procName: B, timeInPrevState: 338, from: State.RUN to: DONE
  currentTime: 2719, procName: Z, timeInPrevState: 2651, from: State.READY to: RUN
  currentTime: 3066, procName: Z, timeInPrevState: 347, from: State.RUN to: DONE
  currentTime: 3066, procName: V, timeInPrevState: 3011, from: State.READY to: RUN
  currentTime: 3435, procName: V, timeInPrevState: 369, from: State.RUN to: DONE
  currentTime: 3435, procName: Y, timeInPrevState: 3370, from: State.READY to: RUN
  currentTime: 3810, procName: Y, timeInPrevState: 375, from: State.RUN to: DONE
  currentTime: 3810, procName: X, timeInPrevState: 3747, from: State.READY to: RUN
  currentTime: 4267, procName: X, timeInPrevState: 457, from: State.RUN to: DONE
  currentTime: 4267, procName: M, timeInPrevState: 4232, from: State.READY to: RUN
  currentTime: 4761, procName: M, timeInPrevState: 494, from: State.RUN to: DONE
  currentTime: 4761, procName: R, timeInPrevState: 4719, from: State.READY to: RUN
  currentTime: 5291, procName: R, timeInPrevState: 530, from: State.RUN to: DONE
  currentTime: 5291, procName: G, timeInPrevState: 5271, from: State.READY to: RUN
  currentTime: 5826, procName: G, timeInPrevState: 535, from: State.RUN to: DONE
  currentTime: 5826, procName: P, timeInPrevState: 5787, from: State.READY to: RUN
  currentTime: 6403, procName: P, timeInPrevState: 577, from: State.RUN to: DONE
  currentTime: 6403, procName: K, timeInPrevState: 6371, from: State.READY to: RUN
  currentTime: 7030, procName: K, timeInPrevState: 627, from: State.RUN to: DONE
  currentTime: 7030, procName: Q, timeInPrevState: 6988, from: State.READY to: RUN
  currentTime: 7745, procName: Q, timeInPrevState: 715, from: State.RUN to: DONE
  currentTime: 7745, procName: D, timeInPrevState: 7734, from: State.READY to: RUN
  currentTime: 8518, procName: D, timeInPrevState: 773, from: State.RUN to: DONE
  currentTime: 8518, procName: T, timeInPrevState: 8470, from: State.READY to: RUN
  currentTime: 9313, procName: T, timeInPrevState: 795, from: State.RUN to: DONE
  currentTime: 9313, procName: W, timeInPrevState: 9255, from: State.READY to: RUN
  currentTime: 10161, procName: W, timeInPrevState: 848, from: State.RUN to: DONE
  currentTime: 10161, procName: I, timeInPrevState: 10136, from: State.READY to: RUN
  currentTime: 11092, procName: I, timeInPrevState: 931, from: State.RUN to: DONE
  currentTime: 11092, procName: E, timeInPrevState: 11081, from: State.READY to: RUN
  currentTime: 12040, procName: E, timeInPrevState: 948, from: State.RUN to: DONE
  currentTime: 12040, procName: U, timeInPrevState: 11989, from: State.READY to: RUN
  currentTime: 13002, procName: U, timeInPrevState: 962, from: State.RUN to: DONE
  Results
  Name: A, AT: 5, Work: 192, Tickets: 95, Resource: 1, ExecStartTime: 5, FinishTime: 197, WaitTime: 0, JCT: 1.00
  Name: B, AT: 9, Work: 338, Tickets: 78, Resource: 5, ExecStartTime: 2381, FinishTime: 2719, WaitTime: 2372, JCT: 8.02
  Name: C, AT: 10, Work: 159, Tickets: 31, Resource: 8, ExecStartTime: 197, FinishTime: 356, WaitTime: 187, JCT: 2.18
  Name: D, AT: 11, Work: 773, Tickets: 29, Resource: 7, ExecStartTime: 7745, FinishTime: 8518, WaitTime: 7734, JCT: 11.01
  Name: E, AT: 11, Work: 948, Tickets: 93, Resource: 2, ExecStartTime: 11092, FinishTime: 12040, WaitTime: 11081, JCT: 12.69
  Name: F, AT: 15, Work: 308, Tickets: 37, Resource: 3, ExecStartTime: 1129, FinishTime: 1437, WaitTime: 1114, JCT: 4.62
  Name: G, AT: 20, Work: 535, Tickets: 86, Resource: 6, ExecStartTime: 5291, FinishTime: 5826, WaitTime: 5271, JCT: 10.85
  Name: H, AT: 21, Work: 279, Tickets: 95, Resource: 1, ExecStartTime: 549, FinishTime: 828, WaitTime: 528, JCT: 2.89
  Name: I, AT: 25, Work: 931, Tickets: 28, Resource: 6, ExecStartTime: 10161, FinishTime: 11092, WaitTime: 10136, JCT: 11.89
  Name: J, AT: 27, Work: 301, Tickets: 44, Resource: 2, ExecStartTime: 828, FinishTime: 1129, WaitTime: 801, JCT: 3.66
  Name: K, AT: 32, Work: 627, Tickets: 67, Resource: 1, ExecStartTime: 6403, FinishTime: 7030, WaitTime: 6371, JCT: 11.16
  Name: L, AT: 32, Work: 320, Tickets: 84, Resource: 5, ExecStartTime: 2061, FinishTime: 2381, WaitTime: 2029, JCT: 7.34
  Name: M, AT: 35, Work: 494, Tickets: 58, Resource: 6, ExecStartTime: 4267, FinishTime: 4761, WaitTime: 4232, JCT: 9.57
  Name: N, AT: 35, Work: 310, Tickets: 82, Resource: 4, ExecStartTime: 1437, FinishTime: 1747, WaitTime: 1402, JCT: 5.52
  Name: O, AT: 38, Work: 193, Tickets: 36, Resource: 1, ExecStartTime: 356, FinishTime: 549, WaitTime: 318, JCT: 2.65
  Name: P, AT: 39, Work: 577, Tickets: 84, Resource: 3, ExecStartTime: 5826, FinishTime: 6403, WaitTime: 5787, JCT: 11.03
  Name: Q, AT: 42, Work: 715, Tickets: 49, Resource: 3, ExecStartTime: 7030, FinishTime: 7745, WaitTime: 6988, JCT: 10.77
  Name: R, AT: 42, Work: 530, Tickets: 38, Resource: 4, ExecStartTime: 4761, FinishTime: 5291, WaitTime: 4719, JCT: 9.90
  Name: S, AT: 47, Work: 314, Tickets: 66, Resource: 5, ExecStartTime: 1747, FinishTime: 2061, WaitTime: 1700, JCT: 6.41
  Name: T, AT: 48, Work: 795, Tickets: 91, Resource: 2, ExecStartTime: 8518, FinishTime: 9313, WaitTime: 8470, JCT: 11.65
  Name: U, AT: 51, Work: 962, Tickets: 82, Resource: 5, ExecStartTime: 12040, FinishTime: 13002, WaitTime: 11989, JCT: 13.46
  Name: V, AT: 55, Work: 369, Tickets: 41, Resource: 3, ExecStartTime: 3066, FinishTime: 3435, WaitTime: 3011, JCT: 9.16
  Name: W, AT: 58, Work: 848, Tickets: 96, Resource: 3, ExecStartTime: 9313, FinishTime: 10161, WaitTime: 9255, JCT: 11.91
  Name: X, AT: 63, Work: 457, Tickets: 37, Resource: 3, ExecStartTime: 3810, FinishTime: 4267, WaitTime: 3747, JCT: 9.20
  Name: Y, AT: 65, Work: 375, Tickets: 50, Resource: 7, ExecStartTime: 3435, FinishTime: 3810, WaitTime: 3370, JCT: 9.99
  Name: Z, AT: 68, Work: 347, Tickets: 53, Resource: 8, ExecStartTime: 2719, FinishTime: 3066, WaitTime: 2651, JCT: 8.64
  Scheduler: SRTF, Average JCT: 8.35
```

- SRF Trace and Result
  
```SRF
  currentTime: 5, procName: A, timeInPrevState: 0, from: State.CREATED to: READY
  currentTime: 5, procName: A, timeInPrevState: 0, from: State.READY to: RUN
  currentTime: 9, procName: B, timeInPrevState: 0, from: State.CREATED to: READY
  currentTime: 10, procName: C, timeInPrevState: 0, from: State.CREATED to: READY
  currentTime: 11, procName: D, timeInPrevState: 0, from: State.CREATED to: READY
  currentTime: 11, procName: E, timeInPrevState: 0, from: State.CREATED to: READY
  currentTime: 15, procName: F, timeInPrevState: 0, from: State.CREATED to: READY
  currentTime: 20, procName: G, timeInPrevState: 0, from: State.CREATED to: READY
  currentTime: 21, procName: H, timeInPrevState: 0, from: State.CREATED to: READY
  currentTime: 25, procName: I, timeInPrevState: 0, from: State.CREATED to: READY
  currentTime: 27, procName: J, timeInPrevState: 0, from: State.CREATED to: READY
  currentTime: 32, procName: K, timeInPrevState: 0, from: State.CREATED to: READY
  currentTime: 32, procName: L, timeInPrevState: 0, from: State.CREATED to: READY
  currentTime: 35, procName: M, timeInPrevState: 0, from: State.CREATED to: READY
  currentTime: 35, procName: N, timeInPrevState: 0, from: State.CREATED to: READY
  currentTime: 38, procName: O, timeInPrevState: 0, from: State.CREATED to: READY
  currentTime: 39, procName: P, timeInPrevState: 0, from: State.CREATED to: READY
  currentTime: 42, procName: Q, timeInPrevState: 0, from: State.CREATED to: READY
  currentTime: 42, procName: R, timeInPrevState: 0, from: State.CREATED to: READY
  currentTime: 47, procName: S, timeInPrevState: 0, from: State.CREATED to: READY
  currentTime: 48, procName: T, timeInPrevState: 0, from: State.CREATED to: READY
  currentTime: 51, procName: U, timeInPrevState: 0, from: State.CREATED to: READY
  currentTime: 55, procName: V, timeInPrevState: 0, from: State.CREATED to: READY
  currentTime: 58, procName: W, timeInPrevState: 0, from: State.CREATED to: READY
  currentTime: 63, procName: X, timeInPrevState: 0, from: State.CREATED to: READY
  currentTime: 65, procName: Y, timeInPrevState: 0, from: State.CREATED to: READY
  currentTime: 68, procName: Z, timeInPrevState: 0, from: State.CREATED to: READY
  currentTime: 197, procName: A, timeInPrevState: 192, from: State.RUN to: DONE
  currentTime: 197, procName: H, timeInPrevState: 176, from: State.READY to: RUN
  currentTime: 476, procName: H, timeInPrevState: 279, from: State.RUN to: DONE
  currentTime: 476, procName: K, timeInPrevState: 444, from: State.READY to: RUN
  currentTime: 1103, procName: K, timeInPrevState: 627, from: State.RUN to: DONE
  currentTime: 1103, procName: O, timeInPrevState: 1065, from: State.READY to: RUN
  currentTime: 1296, procName: O, timeInPrevState: 193, from: State.RUN to: DONE
  currentTime: 1296, procName: E, timeInPrevState: 1285, from: State.READY to: RUN
  currentTime: 2244, procName: E, timeInPrevState: 948, from: State.RUN to: DONE
  currentTime: 2244, procName: J, timeInPrevState: 2217, from: State.READY to: RUN
  currentTime: 2545, procName: J, timeInPrevState: 301, from: State.RUN to: DONE
  currentTime: 2545, procName: T, timeInPrevState: 2497, from: State.READY to: RUN
  currentTime: 3340, procName: T, timeInPrevState: 795, from: State.RUN to: DONE
  currentTime: 3340, procName: F, timeInPrevState: 3325, from: State.READY to: RUN
  currentTime: 3648, procName: F, timeInPrevState: 308, from: State.RUN to: DONE
  currentTime: 3648, procName: P, timeInPrevState: 3609, from: State.READY to: RUN
  currentTime: 4225, procName: P, timeInPrevState: 577, from: State.RUN to: DONE
  currentTime: 4225, procName: Q, timeInPrevState: 4183, from: State.READY to: RUN
  currentTime: 4940, procName: Q, timeInPrevState: 715, from: State.RUN to: DONE
  currentTime: 4940, procName: V, timeInPrevState: 4885, from: State.READY to: RUN
  currentTime: 5309, procName: V, timeInPrevState: 369, from: State.RUN to: DONE
  currentTime: 5309, procName: W, timeInPrevState: 5251, from: State.READY to: RUN
  currentTime: 6157, procName: W, timeInPrevState: 848, from: State.RUN to: DONE
  currentTime: 6157, procName: X, timeInPrevState: 6094, from: State.READY to: RUN
  currentTime: 6614, procName: X, timeInPrevState: 457, from: State.RUN to: DONE
  currentTime: 6614, procName: N, timeInPrevState: 6579, from: State.READY to: RUN
  currentTime: 6924, procName: N, timeInPrevState: 310, from: State.RUN to: DONE
  currentTime: 6924, procName: R, timeInPrevState: 6882, from: State.READY to: RUN
  currentTime: 7454, procName: R, timeInPrevState: 530, from: State.RUN to: DONE
  currentTime: 7454, procName: B, timeInPrevState: 7445, from: State.READY to: RUN
  currentTime: 7792, procName: B, timeInPrevState: 338, from: State.RUN to: DONE
  currentTime: 7792, procName: L, timeInPrevState: 7760, from: State.READY to: RUN
  currentTime: 8112, procName: L, timeInPrevState: 320, from: State.RUN to: DONE
  currentTime: 8112, procName: S, timeInPrevState: 8065, from: State.READY to: RUN
  currentTime: 8426, procName: S, timeInPrevState: 314, from: State.RUN to: DONE
  currentTime: 8426, procName: U, timeInPrevState: 8375, from: State.READY to: RUN
  currentTime: 9388, procName: U, timeInPrevState: 962, from: State.RUN to: DONE
  currentTime: 9388, procName: G, timeInPrevState: 9368, from: State.READY to: RUN
  currentTime: 9923, procName: G, timeInPrevState: 535, from: State.RUN to: DONE
  currentTime: 9923, procName: I, timeInPrevState: 9898, from: State.READY to: RUN
  currentTime: 10854, procName: I, timeInPrevState: 931, from: State.RUN to: DONE
  currentTime: 10854, procName: M, timeInPrevState: 10819, from: State.READY to: RUN
  currentTime: 11348, procName: M, timeInPrevState: 494, from: State.RUN to: DONE
  currentTime: 11348, procName: D, timeInPrevState: 11337, from: State.READY to: RUN
  currentTime: 12121, procName: D, timeInPrevState: 773, from: State.RUN to: DONE
  currentTime: 12121, procName: Y, timeInPrevState: 12056, from: State.READY to: RUN
  currentTime: 12496, procName: Y, timeInPrevState: 375, from: State.RUN to: DONE
  currentTime: 12496, procName: C, timeInPrevState: 12486, from: State.READY to: RUN
  currentTime: 12655, procName: C, timeInPrevState: 159, from: State.RUN to: DONE
  currentTime: 12655, procName: Z, timeInPrevState: 12587, from: State.READY to: RUN
  currentTime: 13002, procName: Z, timeInPrevState: 347, from: State.RUN to: DONE
  Results
  Name: A, AT: 5, Work: 192, Tickets: 95, Resource: 1, ExecStartTime: 5, FinishTime: 197, WaitTime: 0, JCT: 1.00
  Name: B, AT: 9, Work: 338, Tickets: 78, Resource: 5, ExecStartTime: 7454, FinishTime: 7792, WaitTime: 7445, JCT: 23.03
  Name: C, AT: 10, Work: 159, Tickets: 31, Resource: 8, ExecStartTime: 12496, FinishTime: 12655, WaitTime: 12486, JCT: 79.53
  Name: D, AT: 11, Work: 773, Tickets: 29, Resource: 7, ExecStartTime: 11348, FinishTime: 12121, WaitTime: 11337, JCT: 15.67
  Name: E, AT: 11, Work: 948, Tickets: 93, Resource: 2, ExecStartTime: 1296, FinishTime: 2244, WaitTime: 1285, JCT: 2.36
  Name: F, AT: 15, Work: 308, Tickets: 37, Resource: 3, ExecStartTime: 3340, FinishTime: 3648, WaitTime: 3325, JCT: 11.80
  Name: G, AT: 20, Work: 535, Tickets: 86, Resource: 6, ExecStartTime: 9388, FinishTime: 9923, WaitTime: 9368, JCT: 18.51
  Name: H, AT: 21, Work: 279, Tickets: 95, Resource: 1, ExecStartTime: 197, FinishTime: 476, WaitTime: 176, JCT: 1.63
  Name: I, AT: 25, Work: 931, Tickets: 28, Resource: 6, ExecStartTime: 9923, FinishTime: 10854, WaitTime: 9898, JCT: 11.63
  Name: J, AT: 27, Work: 301, Tickets: 44, Resource: 2, ExecStartTime: 2244, FinishTime: 2545, WaitTime: 2217, JCT: 8.37
  Name: K, AT: 32, Work: 627, Tickets: 67, Resource: 1, ExecStartTime: 476, FinishTime: 1103, WaitTime: 444, JCT: 1.71
  Name: L, AT: 32, Work: 320, Tickets: 84, Resource: 5, ExecStartTime: 7792, FinishTime: 8112, WaitTime: 7760, JCT: 25.25
  Name: M, AT: 35, Work: 494, Tickets: 58, Resource: 6, ExecStartTime: 10854, FinishTime: 11348, WaitTime: 10819, JCT: 22.90
  Name: N, AT: 35, Work: 310, Tickets: 82, Resource: 4, ExecStartTime: 6614, FinishTime: 6924, WaitTime: 6579, JCT: 22.22
  Name: O, AT: 38, Work: 193, Tickets: 36, Resource: 1, ExecStartTime: 1103, FinishTime: 1296, WaitTime: 1065, JCT: 6.52
  Name: P, AT: 39, Work: 577, Tickets: 84, Resource: 3, ExecStartTime: 3648, FinishTime: 4225, WaitTime: 3609, JCT: 7.25
  Name: Q, AT: 42, Work: 715, Tickets: 49, Resource: 3, ExecStartTime: 4225, FinishTime: 4940, WaitTime: 4183, JCT: 6.85
  Name: R, AT: 42, Work: 530, Tickets: 38, Resource: 4, ExecStartTime: 6924, FinishTime: 7454, WaitTime: 6882, JCT: 13.98
  Name: S, AT: 47, Work: 314, Tickets: 66, Resource: 5, ExecStartTime: 8112, FinishTime: 8426, WaitTime: 8065, JCT: 26.68
  Name: T, AT: 48, Work: 795, Tickets: 91, Resource: 2, ExecStartTime: 2545, FinishTime: 3340, WaitTime: 2497, JCT: 4.14
  Name: U, AT: 51, Work: 962, Tickets: 82, Resource: 5, ExecStartTime: 8426, FinishTime: 9388, WaitTime: 8375, JCT: 9.71
  Name: V, AT: 55, Work: 369, Tickets: 41, Resource: 3, ExecStartTime: 4940, FinishTime: 5309, WaitTime: 4885, JCT: 14.24
  Name: W, AT: 58, Work: 848, Tickets: 96, Resource: 3, ExecStartTime: 5309, FinishTime: 6157, WaitTime: 5251, JCT: 7.19
  Name: X, AT: 63, Work: 457, Tickets: 37, Resource: 3, ExecStartTime: 6157, FinishTime: 6614, WaitTime: 6094, JCT: 14.33
  Name: Y, AT: 65, Work: 375, Tickets: 50, Resource: 7, ExecStartTime: 12121, FinishTime: 12496, WaitTime: 12056, JCT: 33.15
  Name: Z, AT: 68, Work: 347, Tickets: 53, Resource: 8, ExecStartTime: 12655, FinishTime: 13002, WaitTime: 12587, JCT: 37.27
  Scheduler: SRF, Average JCT: 16.42
```

- Lottery Trace and Result
  
```Lottery
  currentTime: 5, procName: A, timeInPrevState: 0, from: State.CREATED to: READY
  Winner: A
  currentTime: 5, procName: A, timeInPrevState: 0, from: State.READY to: RUN
  currentTime: 9, procName: B, timeInPrevState: 0, from: State.CREATED to: READY
  currentTime: 10, procName: C, timeInPrevState: 0, from: State.CREATED to: READY
  currentTime: 11, procName: D, timeInPrevState: 0, from: State.CREATED to: READY
  currentTime: 11, procName: E, timeInPrevState: 0, from: State.CREATED to: READY
  currentTime: 15, procName: F, timeInPrevState: 0, from: State.CREATED to: READY
  currentTime: 20, procName: G, timeInPrevState: 0, from: State.CREATED to: READY
  currentTime: 21, procName: H, timeInPrevState: 0, from: State.CREATED to: READY
  currentTime: 25, procName: I, timeInPrevState: 0, from: State.CREATED to: READY
  currentTime: 27, procName: J, timeInPrevState: 0, from: State.CREATED to: READY
  currentTime: 32, procName: K, timeInPrevState: 0, from: State.CREATED to: READY
  currentTime: 32, procName: L, timeInPrevState: 0, from: State.CREATED to: READY
  currentTime: 35, procName: M, timeInPrevState: 0, from: State.CREATED to: READY
  currentTime: 35, procName: N, timeInPrevState: 0, from: State.CREATED to: READY
  currentTime: 38, procName: O, timeInPrevState: 0, from: State.CREATED to: READY
  currentTime: 39, procName: P, timeInPrevState: 0, from: State.CREATED to: READY
  currentTime: 42, procName: Q, timeInPrevState: 0, from: State.CREATED to: READY
  currentTime: 42, procName: R, timeInPrevState: 0, from: State.CREATED to: READY
  currentTime: 47, procName: S, timeInPrevState: 0, from: State.CREATED to: READY
  currentTime: 48, procName: T, timeInPrevState: 0, from: State.CREATED to: READY
  currentTime: 51, procName: U, timeInPrevState: 0, from: State.CREATED to: READY
  currentTime: 55, procName: V, timeInPrevState: 0, from: State.CREATED to: READY
  currentTime: 58, procName: W, timeInPrevState: 0, from: State.CREATED to: READY
  currentTime: 63, procName: X, timeInPrevState: 0, from: State.CREATED to: READY
  currentTime: 65, procName: Y, timeInPrevState: 0, from: State.CREATED to: READY
  currentTime: 68, procName: Z, timeInPrevState: 0, from: State.CREATED to: READY
  currentTime: 197, procName: A, timeInPrevState: 192, from: State.RUN to: DONE
  Winner: N
  currentTime: 197, procName: N, timeInPrevState: 162, from: State.READY to: RUN
  currentTime: 507, procName: N, timeInPrevState: 310, from: State.RUN to: DONE
  Winner: U
  currentTime: 507, procName: U, timeInPrevState: 456, from: State.READY to: RUN
  currentTime: 1469, procName: U, timeInPrevState: 962, from: State.RUN to: DONE
  Winner: G
  currentTime: 1469, procName: G, timeInPrevState: 1449, from: State.READY to: RUN
  currentTime: 2004, procName: G, timeInPrevState: 535, from: State.RUN to: DONE
  Winner: Y
  currentTime: 2004, procName: Y, timeInPrevState: 1939, from: State.READY to: RUN
  currentTime: 2379, procName: Y, timeInPrevState: 375, from: State.RUN to: DONE
  Winner: H
  currentTime: 2379, procName: H, timeInPrevState: 2358, from: State.READY to: RUN
  currentTime: 2658, procName: H, timeInPrevState: 279, from: State.RUN to: DONE
  Winner: L
  currentTime: 2658, procName: L, timeInPrevState: 2626, from: State.READY to: RUN
  currentTime: 2978, procName: L, timeInPrevState: 320, from: State.RUN to: DONE
  Winner: R
  currentTime: 2978, procName: R, timeInPrevState: 2936, from: State.READY to: RUN
  currentTime: 3508, procName: R, timeInPrevState: 530, from: State.RUN to: DONE
  Winner: B
  currentTime: 3508, procName: B, timeInPrevState: 3499, from: State.READY to: RUN
  currentTime: 3846, procName: B, timeInPrevState: 338, from: State.RUN to: DONE
  Winner: I
  currentTime: 3846, procName: I, timeInPrevState: 3821, from: State.READY to: RUN
  currentTime: 4777, procName: I, timeInPrevState: 931, from: State.RUN to: DONE
  Winner: S
  currentTime: 4777, procName: S, timeInPrevState: 4730, from: State.READY to: RUN
  currentTime: 5091, procName: S, timeInPrevState: 314, from: State.RUN to: DONE
  Winner: K
  currentTime: 5091, procName: K, timeInPrevState: 5059, from: State.READY to: RUN
  currentTime: 5718, procName: K, timeInPrevState: 627, from: State.RUN to: DONE
  Winner: J
  currentTime: 5718, procName: J, timeInPrevState: 5691, from: State.READY to: RUN
  currentTime: 6019, procName: J, timeInPrevState: 301, from: State.RUN to: DONE
  Winner: M
  currentTime: 6019, procName: M, timeInPrevState: 5984, from: State.READY to: RUN
  currentTime: 6513, procName: M, timeInPrevState: 494, from: State.RUN to: DONE
  Winner: X
  currentTime: 6513, procName: X, timeInPrevState: 6450, from: State.READY to: RUN
  currentTime: 6970, procName: X, timeInPrevState: 457, from: State.RUN to: DONE
  Winner: C
  currentTime: 6970, procName: C, timeInPrevState: 6960, from: State.READY to: RUN
  currentTime: 7129, procName: C, timeInPrevState: 159, from: State.RUN to: DONE
  Winner: P
  currentTime: 7129, procName: P, timeInPrevState: 7090, from: State.READY to: RUN
  currentTime: 7706, procName: P, timeInPrevState: 577, from: State.RUN to: DONE
  Winner: Q
  currentTime: 7706, procName: Q, timeInPrevState: 7664, from: State.READY to: RUN
  currentTime: 8421, procName: Q, timeInPrevState: 715, from: State.RUN to: DONE
  Winner: E
  currentTime: 8421, procName: E, timeInPrevState: 8410, from: State.READY to: RUN
  currentTime: 9369, procName: E, timeInPrevState: 948, from: State.RUN to: DONE
  Winner: T
  currentTime: 9369, procName: T, timeInPrevState: 9321, from: State.READY to: RUN
  currentTime: 10164, procName: T, timeInPrevState: 795, from: State.RUN to: DONE
  Winner: O
  currentTime: 10164, procName: O, timeInPrevState: 10126, from: State.READY to: RUN
  currentTime: 10357, procName: O, timeInPrevState: 193, from: State.RUN to: DONE
  Winner: F
  currentTime: 10357, procName: F, timeInPrevState: 10342, from: State.READY to: RUN
  currentTime: 10665, procName: F, timeInPrevState: 308, from: State.RUN to: DONE
  Winner: Z
  currentTime: 10665, procName: Z, timeInPrevState: 10597, from: State.READY to: RUN
  currentTime: 11012, procName: Z, timeInPrevState: 347, from: State.RUN to: DONE
  Winner: D
  currentTime: 11012, procName: D, timeInPrevState: 11001, from: State.READY to: RUN
  currentTime: 11785, procName: D, timeInPrevState: 773, from: State.RUN to: DONE
  Winner: W
  currentTime: 11785, procName: W, timeInPrevState: 11727, from: State.READY to: RUN
  currentTime: 12633, procName: W, timeInPrevState: 848, from: State.RUN to: DONE
  Winner: V
  currentTime: 12633, procName: V, timeInPrevState: 12578, from: State.READY to: RUN
  currentTime: 13002, procName: V, timeInPrevState: 369, from: State.RUN to: DONE
  Results
  Name: A, AT: 5, Work: 192, Tickets: 95, Resource: 1, ExecStartTime: 5, FinishTime: 197, WaitTime: 0, JCT: 1.00
  Name: B, AT: 9, Work: 338, Tickets: 78, Resource: 5, ExecStartTime: 3508, FinishTime: 3846, WaitTime: 3499, JCT: 11.35
  Name: C, AT: 10, Work: 159, Tickets: 31, Resource: 8, ExecStartTime: 6970, FinishTime: 7129, WaitTime: 6960, JCT: 44.77
  Name: D, AT: 11, Work: 773, Tickets: 29, Resource: 7, ExecStartTime: 11012, FinishTime: 11785, WaitTime: 11001, JCT: 15.23
  Name: E, AT: 11, Work: 948, Tickets: 93, Resource: 2, ExecStartTime: 8421, FinishTime: 9369, WaitTime: 8410, JCT: 9.87
  Name: F, AT: 15, Work: 308, Tickets: 37, Resource: 3, ExecStartTime: 10357, FinishTime: 10665, WaitTime: 10342, JCT: 34.58
  Name: G, AT: 20, Work: 535, Tickets: 86, Resource: 6, ExecStartTime: 1469, FinishTime: 2004, WaitTime: 1449, JCT: 3.71
  Name: H, AT: 21, Work: 279, Tickets: 95, Resource: 1, ExecStartTime: 2379, FinishTime: 2658, WaitTime: 2358, JCT: 9.45
  Name: I, AT: 25, Work: 931, Tickets: 28, Resource: 6, ExecStartTime: 3846, FinishTime: 4777, WaitTime: 3821, JCT: 5.10
  Name: J, AT: 27, Work: 301, Tickets: 44, Resource: 2, ExecStartTime: 5718, FinishTime: 6019, WaitTime: 5691, JCT: 19.91
  Name: K, AT: 32, Work: 627, Tickets: 67, Resource: 1, ExecStartTime: 5091, FinishTime: 5718, WaitTime: 5059, JCT: 9.07
  Name: L, AT: 32, Work: 320, Tickets: 84, Resource: 5, ExecStartTime: 2658, FinishTime: 2978, WaitTime: 2626, JCT: 9.21
  Name: M, AT: 35, Work: 494, Tickets: 58, Resource: 6, ExecStartTime: 6019, FinishTime: 6513, WaitTime: 5984, JCT: 13.11
  Name: N, AT: 35, Work: 310, Tickets: 82, Resource: 4, ExecStartTime: 197, FinishTime: 507, WaitTime: 162, JCT: 1.52
  Name: O, AT: 38, Work: 193, Tickets: 36, Resource: 1, ExecStartTime: 10164, FinishTime: 10357, WaitTime: 10126, JCT: 53.47
  Name: P, AT: 39, Work: 577, Tickets: 84, Resource: 3, ExecStartTime: 7129, FinishTime: 7706, WaitTime: 7090, JCT: 13.29
  Name: Q, AT: 42, Work: 715, Tickets: 49, Resource: 3, ExecStartTime: 7706, FinishTime: 8421, WaitTime: 7664, JCT: 11.72
  Name: R, AT: 42, Work: 530, Tickets: 38, Resource: 4, ExecStartTime: 2978, FinishTime: 3508, WaitTime: 2936, JCT: 6.54
  Name: S, AT: 47, Work: 314, Tickets: 66, Resource: 5, ExecStartTime: 4777, FinishTime: 5091, WaitTime: 4730, JCT: 16.06
  Name: T, AT: 48, Work: 795, Tickets: 91, Resource: 2, ExecStartTime: 9369, FinishTime: 10164, WaitTime: 9321, JCT: 12.72
  Name: U, AT: 51, Work: 962, Tickets: 82, Resource: 5, ExecStartTime: 507, FinishTime: 1469, WaitTime: 456, JCT: 1.47
  Name: V, AT: 55, Work: 369, Tickets: 41, Resource: 3, ExecStartTime: 12633, FinishTime: 13002, WaitTime: 12578, JCT: 35.09
  Name: W, AT: 58, Work: 848, Tickets: 96, Resource: 3, ExecStartTime: 11785, FinishTime: 12633, WaitTime: 11727, JCT: 14.83
  Name: X, AT: 63, Work: 457, Tickets: 37, Resource: 3, ExecStartTime: 6513, FinishTime: 6970, WaitTime: 6450, JCT: 15.11
  Name: Y, AT: 65, Work: 375, Tickets: 50, Resource: 7, ExecStartTime: 2004, FinishTime: 2379, WaitTime: 1939, JCT: 6.17
  Name: Z, AT: 68, Work: 347, Tickets: 53, Resource: 8, ExecStartTime: 10665, FinishTime: 11012, WaitTime: 10597, JCT: 31.54
  Scheduler: Lottery, Average JCT: 15.61
```