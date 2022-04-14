# DataFiltering
Data Filtering For Microbial Association Network Construction

Microorganisms are not alone in the environment, forming complex assemblages that perform essential ecosystem functions and maintain ecosystem stability. Besides the diversity and compositions of microbial communities, deciphering their potential interactions in the form of association networks has attracted many microbiologists and ecologists. Much effort has been made towards the methodological development for constructing microbial association networks. However, microbial profiles suffer dramatically from missing values, which hamper accurate association network construction. In this study, we investigated the effects of missing value issues associated with microbial association network construction. Using the TARA Oceans microbial profile as an example, different missing-value-treatment approaches were comparatively investigated using different correlation methods. The results suggested dramatic variations of correlation coefficient values for differently treated microbial profiles. Consequently, microbial association networks were dramatically differed. As microbial association network analyses have become a widely used technique in the field of microbial ecology and environmental science, we urge cautions be made to critically consider the missing value issues in microbial data.

Here, different missing-value-treatment approaches were comparatively investigated using Spearman’s rank order correlation correlation as an example. Since the missing values of data of microbial abundance we usually get are filled with 0 by default, for your convenience, all of our code is based on that.  

Six files are generated for data filtering:
1.	Method_1.R: The first method is to fill in the missing values with 0.
2.	Method_2.R: The second method fills missing values using a nearest neighbor algorithm.
3.	Method_3.R: The third method is to fill the missing values with 0.01.
4.	Method_4.py: The fourth method is to exclude the samples from correlation calculation in which pairwise missing values are detected and fill the unpaired missing values with 0.01.
5.	Method_5.py: The fifth method is similar to the fourth method but fills unpaired missing values with 0.
6.	Method_6.py: The sixth method is to exclude all samples from correlation calculation as long as paired or unpaired missing values are observed. 
Detailed explanations:
Input data: 2D array of counts. Columns are samples, rows are components.
Output data: 2D array of counts. Correlation matrix, columns are components, rows are components.
