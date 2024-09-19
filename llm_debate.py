import argparse

from util import GSMDebateOneByOne


def main(args):
    pass
    if args.task == "GSM":
        if args.debate_mode == "onebyone":
            GSMDebateOneByOne(args)
    if args.task == "StrategyQA":
        pass

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="LLM debating with confidence")
    parser.add_argument('--task', type=str, default="GSM", choices=["GSM", "StrategyQA"], help='This argument assigns the task to be performed by')
    parser.add_argument('--debate_turns', type=int, default=2, help='This argument assigns the debating turns')
    parser.add_argument('--debate_agents', type=int, default=3, help='This argument assigns the number of debating agents')
    parser.add_argument('--debate_mode', type=str, default="onebyone", choices=["onebyone", "simultaneous"], help='This argument assigns the debating mode, using only assistant_1 in this mode')
    parser.add_argument('--attempt_times', type=int, default=5, help='This argument assigns the number of attempts times if failed to output in requested format')
    
    
    parser.add_argument('--self_elicit', type=str, default="Self-Probing", help='This argument assigns the prompting scheme for self-elicitation')
    
    parser.add_argument('--output_dir', type=str, default="./result", help='This argument assigns the output directory')
    
    args = parser.parse_args()
    
    main(args)