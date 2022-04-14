
###The third method is to fill the missing values with 0.01.

method_3 <- function(data){
  data <- data.frame(data)
  data[data=="0"] <- NA      
  data <- impute(data,0.01)
  method_3_spearman <- cor(t(data),method = "spearman")
}


method_3_spearman <- method_3(DATA)