library(cluster);

# Start from 2 to 20
begin <- 2; 
count <- 100;
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
        kcluster = kmeans(data[, 3:47], i);
		dissE <- daisy(data[,3:47]);
		dE2 <- dissE^2;
		sk2 <- silhouette(kcluster$cl, dE2);
    }
    result[i] = mean(sk2);
}
 
plot(result, type="o", xlab="Number of Cluster", ylab="Silhouette Score");


