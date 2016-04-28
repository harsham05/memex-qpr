

```
tar -xzvf CP3_GT.tar.gz

find CP3_Ground_Truth/ -type f > ground_truth

chmod u+x iterate.sh

./iterate.sh ground_truth <concatenated_URLs_file>

```

