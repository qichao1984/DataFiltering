
###The second method fills missing values using a nearest neighbor algorithm.

library(DMwR2)
method_2 <- function(data){
  data[data=="0"] <- NA   
  data <- data.frame(data)
  dataknn <- knnImputation(data, k = 10, scale = T, meth = "weighAvg",distData = NULL)
  method_2_spearman <- cor(t(dataknn),method = "spearman")
}

method_2_spearman <- method_2(DATA)
