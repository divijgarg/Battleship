# coded by Divij Garg

from Simulation import Simulation

def main():
    sim1=Simulation(100000)
    sim1.createSims()
    sim1.runTrials()
    sim1.doStatsAnalysis()

main()
