library(cluster);

# Start from 2 to 20
begin <- 2; 
count <- 50;
end <- 20;
 
# Store result
result = c();
result[begin:end] = -1;
 
data <- read.csv("/Users/royxue/Code/CMU_Projects/code/kmeans/final_merge.csv");

for(i in begin:end) {
    # Silhouette coefficient
    tmp = c();
    tmp[1:count] = 0;
    for(j in 1:count) {
        kcluster = pam(data[, 3:47], i);
        tmp[j] = kcluster$silinfo$avg.width;
    }
    result[i] = mean(tmp);
}
 
plot(result, type="o", xlab="Number of Cluster", ylab="Silhouette Score");

