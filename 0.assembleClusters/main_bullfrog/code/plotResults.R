#code to plot results of clustering

library(ggplot2)
library(dplyr)

setwd("/home/nbe4/scratch60/0.assembleClusters/")

resultDir="overallStats"

allFinalStats=data.frame(c())
for (i in list.files(resultDir)){
  thisOut=read.csv(paste0(resultDir,"/",i))
  thisOut$clust_threshold=factor(thisOut$clust_threshold, levels=c(85,9,95))
  allFinalStats=bind_rows(allFinalStats,thisOut)
}

plotResults = ggplot(data=allFinalStats)+
  geom_density(aes(fill=clust_threshold,x=clusters_hidepth))+
  facet_wrap(~max_shared_Hs_locus + as.factor(maxDepth))

highCov <- as.character(allFinalStats[which(allFinalStats$clusters_hidepth > 50000 & allFinalStats$clust_threshold==95),]$X)

unique(highCov)