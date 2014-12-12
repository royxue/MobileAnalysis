library(cluster);
library(fpc)

# Start from 2 to 20
begin <- 2; 
count <- 50;
end <- 20;

# Store result
result = c();
result[begin:end] = -1;
sd_result = c();
sd_result[begin:end] = -1;

data <- read.csv("/Users/royxue/Code/CMU_Projects/code/kmeans/final_merge.csv");
l_data = data[,3:47];

for(i in begin:end) {
  # Silhouette coefficient
  tmp = c();
  tmp[1:count]=0;
  for(j in 1:count){
    kcluster = kmeans(l_data, i);
    stats = cluster.stats(dist(l_data), kcluster$cluster)
    tmp[j] = stats$avg.silwidth
  }
  result[i] = mean(tmp);
  sd_result[i] = sd(tmp);
}

plot(result, type="o", xlab="Number of Cluster", ylab="Silhouette Score", main="Mean");
plot(sd_result, type="o", xlab="Number of Cluster", main="Standard Deviation");