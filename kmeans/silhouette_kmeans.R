library(cluster);
library(fpc)

# Start from 2 to 20
begin <- 2; 
count <- 50;
end <- 20;

# Store result
result = c();
result[begin:end] = -1;

data <- read.csv("/Users/royxue/Code/CMU_Projects/code/kmeans/final_merge.csv");
l_data = data[,3:47];

for(i in begin:end) {
  # Silhouette coefficient
  kcluster = kmeans(l_data, i);
  stats = cluster.stats(dist(l_data), kcluster$cluster)
  result[i] = stats$avg.silwidth
}

plot(result, type="o", xlab="Number of Cluster", ylab="Silhouette Score");

