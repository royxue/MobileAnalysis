library(cluster);
library(fpc);

data <- read.csv("/Users/royxue/Code/CMU_Projects/code/kmeans/final_merge.csv");
l_data = data[,3:47];

k <- kmeans(l_data, 4);
stats = cluster.stats(dist(l_data), k$cluster)
if (stats$avg.silwidth > 0.38){
heatmap(as.matrix(l_data)[order(k$cluster),],Rowv=NA,Colv=NA,scale="none",labRow=NA)
}

# k <- pam(l_data, 4);
# DBScan Method
# k <- dbscan(l_data,eps=0.655,MinPts=7)
# dbscan Pts=138 MinPts=7 eps=0.655
#        0   1   2  3
#border 60  29   2  0
#seed    0  31   9  7
#total  60  60  11  7