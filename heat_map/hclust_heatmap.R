data <- read.csv("/Users/royxue/Code/CMU_Projects/code/kmeans/final_merge.csv");
l_data = data[,3:47];

dist <- dist(l_data,method="euclidean");
hclust <- hclust(dist,method="complete");
plot(hclust);
heatmap(as.matrix(dist),labRow = F, labCol = F)