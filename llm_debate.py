import argparse

from util import GSMDebate


def main(args):
    pass
    if args.task == "GSM":
        GSMDebate(args)
        

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="LLM debating with confidence")
    parser.add_argument('--task', type=str, default="GSM", help='This argument assigns the task to be performed by')
    parser.add_argument('--debate_turns', type=int, default=2, help='This argument assigns the debating turns')
    parser.add_argument('--debate_agents', type=int, default=3, help='This argument assigns the number of debating agents')
    parser.add_argument('--assistant_1', type=str, default="claude-3-haiku-20240307", help='This argument assigns the num ')
    parser.add_argument('--assistant_2', type=str, default="gpt-3.5-turbo", help='This argument assigns the num ')
    parser.add_argument('--attempt_times', type=int, default=5, help='This argument assigns the num ')
    
    args = parser.parse_args()
    
    main(args)