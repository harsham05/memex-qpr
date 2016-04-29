#!/usr/bin/env bash

while read p; do
  python evaluation-CP3.py $p $2
done <$1

#CP3_Ground_Truth/CP3_4-4_Sheet1.csv