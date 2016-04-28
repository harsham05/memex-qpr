import sys


def main(groundF, jplF):
    print groundF

    with open(groundF, "r") as groundF:

        ground_truth = set([line.strip().rstrip('/').split("://")[-1] for line in groundF])
        # remove http or https

        with open(jplF, "r") as jplF:

            jpl = set([line.strip().strip('"').rstrip('/').split("://")[-1] for line in jplF])

            results = ground_truth & jpl

            print "Ground truth Sample Size:\t", len(ground_truth)

            print "Overlap:\t", len(results)

            print "Recall:\t", (len(results) * 100)/float(len(ground_truth))




if __name__ == "__main__":
    # ground truth file
    main(sys.argv[1], sys.argv[2])



def weighted():

    """
    weighted Sum, Recall of those 4 questions, in CP1-1, for each question

    of the overall Eval, 4 question

    By host site

    if you move logos, tell Wayne

    """



