import argparse

from util import GSMDebateCompare, GSMDebateSingle


def main(args):
    pass
    if args.task == "GSM":
        if args.debate_mode == "single":
            GSMDebateSingle(args)
        elif args.debate_mode == "dual":
            GSMDebateCompare(args)
        

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="LLM debating with confidence")
    parser.add_argument('--task', type=str, default="GSM", help='This argument assigns the task to be performed by')
    parser.add_argument('--debate_turns', type=int, default=2, help='This argument assigns the debating turns')
    parser.add_argument('--debate_agents', type=int, default=3, help='This argument assigns the number of debating agents')
    parser.add_argument('--debate_mode', type=str, default="single", choices=["single", "dual"], help='This argument assigns the debating mode, using only assistant_1 in this mode')
    parser.add_argument('--assistant_1', type=str, default="gpt-4o-mini", help='This argument assigns model for assistant 1')
    parser.add_argument('--assistant_2', type=str, default="claude-3-haiku-20240307", help='This argument assigns model for assistant 2 ')
    parser.add_argument('--attempt_times', type=int, default=5, help='This argument assigns the number of attempts times if failed to output in requested format')
    
    
    parser.add_argument('--self_elicit', type=str, default="Self-Probing-Single", help='This argument assigns the prompting scheme for self-elicitation')
    
    parser.add_argument('--output_dir', type=str, default="./result", help='This argument assigns the output directory')
    
    args = parser.parse_args()
    
    main(args)