#!/usr/bin/env python


import os
import sys
import ipyrad

inFile=sys.argv[1]

#stats with each row as a sample:
# [assembly].stats_dfs.s7_samples
# #Final Sample stats summary

#other stats
#[assembly].stats_dfs.s7_filters
# [assembly].stats_dfs.s7_loci
#[assembly].stats_dfs.s7_snps
# Alignment matrix statistics

def createCSVs(inFile):
