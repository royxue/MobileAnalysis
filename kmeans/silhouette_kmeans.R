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
#a = matrix(0.25,nrow=50, ncol=20)
a = c();
init <- rep(0.40,50);
a = c(a, init);

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
  #a[1:50, i] = tmp
  #result[i] = mean(tmp);
  #sd_result[i] = sd(tmp);
  a = c(a, tmp)
}

min.mean.sd.max <- function(x) {
  r <- c(min(x), mean(x) - sd(x), mean(x), mean(x) + sd(x), max(x))
  names(r) <- c("ymin", "lower", "middle", "upper", "ymax")
  r
}

#plot(sd_result, type="o", xlab="Number of Cluster", ylab="Silhouette Score");#lines(sd_result, type="o");
#boxplot(a)
p  <- factor(rep(1:20, rep(50,20)))
o <- data.frame(a, p)
names(o) <- c('value', 'k')
p1 <- ggplot(aes(y = value, x = factor(k)), data = o)
p1 <- p1 + stat_summary(fun.data = min.mean.sd.max, geom = "boxplot")
plot(p1)

# Hierarchical clustering
z1 = dist(l_data, method = 'euclidean')
x <- hclust(z1, method='complete')
plot(x)