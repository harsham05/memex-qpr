

```

pip install tldextract

tar -xzvf CP3_GT.tar.gz

find CP3_Ground_Truth/ -type f > ground_truth_ids

chmod u+x iterate.sh

./iterate.sh ground_truth_ids <your_team's_concatenated_URLs_file>

```

your_team's_concatenated_URLs_file is a simple txt file demarcated by "\n"
