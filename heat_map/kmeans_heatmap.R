library(cluster);
library(fpc);

data <- read.csv("/Users/royxue/Code/CMU_Projects/code/kmeans/final_merge.csv");
l_data = data[,3:47];

k <- kmeans(l_data, 4);
stats = cluster.stats(dist(l_data), k$cluster)
if (stats$avg.silwidth > 0.38){
heatmap(as.matrix(l_data)[order(k$cluster),],Rowv=NA,Colv=NA,scale="none",labRow=NA)
}