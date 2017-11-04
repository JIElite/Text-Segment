import argparse 
import segment
import dictionary

parser = argparse.ArgumentParser()
parser.add_argument("-f", "--file", help="using input context file to segment")
parser.add_argument("-s", "--simple", help="just add simple context to end of CLI to segment")
args = parser.parse_args()

dictionary = dictionary.Dictionary()
dictionary.load()

segments_agent = segment.SegmentSystem()
segments_agent.use_dictionary(dictionary)

if args.file:
    with open(args.file, 'r') as fd:
        for context in fd.readlines():
            print(segments_agent.segments(context))
elif args.simple:
    context = args.simple
    print(segments_agent.segments(context))
else:
    print("No Input Context")
    print("If you need any help, please try: python main.py -h")