library(cluster);

count <- 50;

data <- read.csv("/Users/royxue/Code/CMU_Projects/code/kmeans/final_merge.csv");
l_data = data[,3:47];

tmp = 0;

for(j in 1:count){
  kcluster = kmeans(l_data, 4);
  stats = cluster.stats(dist(l_data), kcluster$cluster)
  comp <- stats$avg.silwidth
  if (comp > tmp){
    tmp <- comp;
    result <- kcluster$centers;
  }
}