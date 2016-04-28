import sys, tldextract

def main(groundF, jplF):
    print groundF

    with open(groundF, "r") as groundF:

        urls = [line.strip().rstrip('/') for line in groundF]

        ground_truth_domains = set([tldextract.extract(url).registered_domain for url in urls])

        ground_truth = set([url.split("://")[-1] for url in urls])  # remove http or https


        with open(jplF, "r") as jplF:


            jpl_urls = [ line.strip().strip('"').rstrip('/') for line in jplF]

            jpl_domains =  set([tldextract.extract(url).registered_domain for url in jpl_urls])

            jpl_truth = set([url.split("://")[-1] for url in jpl_urls])



            results = ground_truth & jpl_truth

            print "URLs"
            print "Ground truth Sample Size:\t", len(ground_truth)

            print "Overlap:\t", len(results)

            print "Recall:\t", (len(results) * 100)/float(len(ground_truth))


            domains = ground_truth_domains & jpl_domains

            print "\nHost Names"

            print "Ground truth Host Names:\t", len(ground_truth_domains)

            print "HostName Overlap:\t", len(domains)

            print "Recall:\t", (len(domains) * 100)/float(len(ground_truth_domains))


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



