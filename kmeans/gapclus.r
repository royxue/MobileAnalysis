gskmn <- clusGap(data[,3:47], FUN = pam, K.max = 20, B = 60)
plot(gskmn)
