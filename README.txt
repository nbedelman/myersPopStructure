This is a project begun and led by Andis Arietta. He collected eggs from different ponds in Yale Myers and sequenced them with RAD-seq.

## Generate rad clusters and assess quality ##
There's still no ref genome, so the first thing is to generate de novo RAD loci. Andis did this with ipyrad. The first thing to do is to look at those loci and assess their quality.

Metrics to evaluate:
number of loci
number of samples per locus
mean heterozygosity
shape of heterozygosity per locus

Parameters to adjust:
7 datatype: I think this should actually be ddrad bc 2 enzymes used?
13 maxdepth [maximum depth per ind per locus; def. 10000]: 20,50,100,100000
14 clust_threshold [similarity for clustering reads; def. 0.9]: 0.85, 0.9, 0.95
24 max_shared_Hs_locus [max prop sites heterozygous in loci; def. 0.5 ]: .2, .35, .5
28 pop_assign_file popfile.txt
