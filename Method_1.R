
###The first method is to fill in the missing values with 0.

method_1 <- function(data){
  data <- impute(data,0)   #If the missing values of your data are already filled with 0 by default, skip this step.  
  method_1_spearman <- cor(t(data),method = "spearman")
}

method_1_spearman <- method_1(DATA)

