# Start from 2 to 20
begin = 2; 
count = 50;
end = 20;
 
# Store result
result = c();
result[begin:end] = -1;
 
library(cluster);
qc = read.table("/Users/royxue/Code/CMU_Projects/code/cluster/input_data.txt");
for(i in begin:end) {
    # Silhouette coefficient
    tmp = c();
    tmp[1:count] = 0;
    for(j in 1:count) {
        kcluster = pam(qc, i);
        tmp[j] = kcluster$silinfo$avg.width;
    }
    #result[i] = mean(tmp);
	result[i] = sd(tmp, na.rm=FALSE);
}
 

plot(result, type="o", xlab="Number of Cluster", ylab="Silhouette Coefficient");
