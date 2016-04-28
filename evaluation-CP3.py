import sys


def main(groundF):
    print groundF

    with open(groundF, "r") as groundF:

        ground_truth = set([line.strip().rstrip('/').split("://")[-1] for line in groundF])

        # remove http

        # remove https:

        split on it


        with open("JPL_AprilQPR_CP3.txt", "r") as jplF:

            jpl = set([line.strip().strip('"').rstrip('/').split("://")[-1] for line in jplF])

            results = ground_truth & jpl


            print "Ground truth Sample", len(ground_truth)

            print "Overlap", len(results)

            print "Recall", len(results) / float(len(ground_truth))




if __name__ == "__main__":
    # ground truth file
    main(sys.argv[1])