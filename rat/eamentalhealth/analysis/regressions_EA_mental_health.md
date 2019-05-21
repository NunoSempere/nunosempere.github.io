```
> colnames(A)[c(7,8)]
[1] "Which.of.these.conditions.have.you.been.formally.diagnosed.with."                                 
[2] "Which.of.these.conditions.do.you.think.you.may.have..but.have.never.been.formally.diagnosed.with."

List_of_Mental_Illnesses = c("Depression","Anxiety", "Obsessive Compulsive Disorder", "Disordered Eating", "Alcoholism", "Drug Addiction", "Borderline Personality Disorder", "Bipolar Disorder", "Autism", "ADHD", "Schizophrenia")
(A[,i])
A$num_mental_ilnesses = integer(l) ## This produces a list of 0s.
i=7
l = 303
for(j in c(1:l)){
  for(k in List_of_Mental_Illnesses){
    if(grepl(k,A[,i][j])){
      A$num_mental_ilnesses[j] = A$num_mental_ilnesses[j]+1
    }
  }
}
i=8
A$num_mental_ilnesses2 = A$num_mental_ilnesses
for(j in c(1:l)){
  for(k in List_of_Mental_Illnesses){
    if(grepl(k,A[,i][j])){
      A$num_mental_ilnesses2[j] = A$num_mental_ilnesses2[j]+1
    }
  }
}

A$m_ill_or_not = integer(l)

i=7
for(j in c(1:l)){
  for(k in List_of_Mental_Illnesses){
    if(grepl(k,A[,i][j])){
      A$m_ill_or_not[j] = 1
    }
  }
}
i=8
A$m_ill_or_not2=A$m_ill_or_not
for(j in c(1:l)){
  for(k in List_of_Mental_Illnesses){
    if(grepl(k,A[,i][j])){
      A$m_ill_or_not2[j] = 1
    }
  }
}


> sink("readme.txt")
> colnames(A)[c(3:6)]
> summary(lm(A$m_ill_or_not ~ A[,3]))
> summary(lm(A$m_ill_or_not ~ A[,4]))
> summary(lm(A$m_ill_or_not ~ A[,5]))
> summary(lm(A$m_ill_or_not ~ A[,6]))

> A[,3]+((A[,4]=="No")*0 + (A[,4]=="No, but I regularly participate in an EA online group")*1 + (A[,4]=="Yes, occasionally")*2 + (A[,4]=="Yes")*3) +A[,5]+((A[,6]=="No")*0 + A[,6]=="Yes")*1 -> t

> summary(lm(A$m_ill_or_not ~ t))

> summary(lm(A$num_mental_ilnesses ~A[,3]))
> summary(lm(A$num_mental_ilnesses ~A[,4]))
> summary(lm(A$num_mental_ilnesses ~A[,5]))
> summary(lm(A$num_mental_ilnesses ~A[,6]))

> summary(lm(A$num_mental_ilnesses ~t))
> sink()

[1] "How.involved.are.you.in.the.Effective.Altruism.Community."           
[2] "Do.you.attend.EA.meetings."                                          
[3] "How.much.impact.do.EA.ideas.have.on.your.life."                      
[4] "Do.you.donate.part.of.your.income.to.GiveWell.recommended.charities."

Call:
lm(formula = A$m_ill_or_not ~ A[, 3])

Residuals:
    Min      1Q  Median      3Q     Max 
-0.4659 -0.4585 -0.4536  0.5415  0.5464 

Coefficients:
             Estimate Std. Error t value Pr(>|t|)    
(Intercept)  0.468410   0.078905   5.936 8.12e-09 ***
A[, 3]      -0.002477   0.017804  -0.139    0.889    
---
Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1

Residual standard error: 0.4999 on 297 degrees of freedom
  (4 observations deleted due to missingness)
Multiple R-squared:  6.519e-05,	Adjusted R-squared:  -0.003302 
F-statistic: 0.01936 on 1 and 297 DF,  p-value: 0.8894


Call:
lm(formula = A$m_ill_or_not ~ A[, 4])

Residuals:
    Min      1Q  Median      3Q     Max 
-0.5238 -0.4375 -0.4359  0.5625  0.6667 

Coefficients:
                                                            Estimate Std. Error t value Pr(>|t|)
(Intercept)                                                   0.3333     0.2893   1.152    0.250
A[, 4]No                                                      0.1905     0.2961   0.643    0.520
A[, 4]No, but I regularly participate in an EA online group   0.1505     0.3029   0.497    0.620
A[, 4]Yes, occasionally                                       0.1026     0.2948   0.348    0.728
A[, 4]Yes, often                                              0.1042     0.2926   0.356    0.722

Residual standard error: 0.501 on 298 degrees of freedom
Multiple R-squared:  0.005741,	Adjusted R-squared:  -0.007604 
F-statistic: 0.4302 on 4 and 298 DF,  p-value: 0.7868


Call:
lm(formula = A$m_ill_or_not ~ A[, 5])

Residuals:
    Min      1Q  Median      3Q     Max 
-0.4756 -0.4608 -0.4571  0.5392  0.5429 

Coefficients:
             Estimate Std. Error t value Pr(>|t|)    
(Intercept)  0.479256   0.114810   4.174 3.92e-05 ***
A[, 5]      -0.003696   0.023524  -0.157    0.875    
---
Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1

Residual standard error: 0.5002 on 299 degrees of freedom
  (2 observations deleted due to missingness)
Multiple R-squared:  8.256e-05,	Adjusted R-squared:  -0.003262 
F-statistic: 0.02469 on 1 and 299 DF,  p-value: 0.8753


Call:
lm(formula = A$m_ill_or_not ~ A[, 6])

Residuals:
    Min      1Q  Median      3Q     Max 
-0.4758 -0.4520 -0.4520  0.5480  0.5480 

Coefficients:
             Estimate Std. Error t value Pr(>|t|)
(Intercept) 8.317e-15  3.530e-01   0.000    1.000
A[, 6]No    4.758e-01  3.558e-01   1.337    0.182
A[, 6]Yes   4.520e-01  3.550e-01   1.273    0.204

Residual standard error: 0.4992 on 300 degrees of freedom
Multiple R-squared:  0.006182,	Adjusted R-squared:  -0.0004435 
F-statistic: 0.9331 on 2 and 300 DF,  p-value: 0.3945


Call:
lm(formula = A$m_ill_or_not ~ t)

Residuals:
    Min      1Q  Median      3Q     Max 
-0.4891 -0.4565 -0.4469  0.5416  0.5608 

Coefficients:
             Estimate Std. Error t value Pr(>|t|)    
(Intercept)  0.496827   0.108987   4.559 7.53e-06 ***
t           -0.003841   0.010449  -0.368    0.713    
---
Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1

Residual standard error: 0.4998 on 297 degrees of freedom
  (4 observations deleted due to missingness)
Multiple R-squared:  0.0004549,	Adjusted R-squared:  -0.002911 
F-statistic: 0.1352 on 1 and 297 DF,  p-value: 0.7134


Call:
lm(formula = A$num_mental_ilnesses ~ A[, 3])

Residuals:
    Min      1Q  Median      3Q     Max 
-0.8559 -0.8305 -0.8135  1.1441  5.1695 

Coefficients:
             Estimate Std. Error t value Pr(>|t|)    
(Intercept)  0.864417   0.173834   4.973 1.12e-06 ***
A[, 3]      -0.008484   0.039223  -0.216    0.829    
---
Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1

Residual standard error: 1.101 on 297 degrees of freedom
  (4 observations deleted due to missingness)
Multiple R-squared:  0.0001575,	Adjusted R-squared:  -0.003209 
F-statistic: 0.04679 on 1 and 297 DF,  p-value: 0.8289


Call:
lm(formula = A$num_mental_ilnesses ~ A[, 4])

Residuals:
    Min      1Q  Median      3Q     Max 
-1.0476 -0.7692 -0.7422  0.9524  4.9524 

Coefficients:
                                                            Estimate Std. Error t value Pr(>|t|)
(Intercept)                                                   0.3333     0.6315   0.528    0.598
A[, 4]No                                                      0.7143     0.6464   1.105    0.270
A[, 4]No, but I regularly participate in an EA online group   0.5699     0.6614   0.862    0.390
A[, 4]Yes, occasionally                                       0.4359     0.6436   0.677    0.499
A[, 4]Yes, often                                              0.4089     0.6389   0.640    0.523

Residual standard error: 1.094 on 298 degrees of freedom
Multiple R-squared:  0.01426,	Adjusted R-squared:  0.001027 
F-statistic: 1.078 on 4 and 298 DF,  p-value: 0.3677


Call:
lm(formula = A$num_mental_ilnesses ~ A[, 5])

Residuals:
    Min      1Q  Median      3Q     Max 
-0.8445 -0.8336 -0.8117  1.1555  5.1664 

Coefficients:
            Estimate Std. Error t value Pr(>|t|)   
(Intercept)  0.77898    0.25197   3.092  0.00218 **
A[, 5]       0.01092    0.05163   0.212  0.83263   
---
Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1

Residual standard error: 1.098 on 299 degrees of freedom
  (2 observations deleted due to missingness)
Multiple R-squared:  0.0001496,	Adjusted R-squared:  -0.003194 
F-statistic: 0.04474 on 1 and 299 DF,  p-value: 0.8326


Call:
lm(formula = A$num_mental_ilnesses ~ A[, 6])

Residuals:
    Min      1Q  Median      3Q     Max 
-0.8790 -0.7966 -0.7966  1.1210  5.1210 

Coefficients:
             Estimate Std. Error t value Pr(>|t|)
(Intercept) 1.097e-14  7.744e-01   0.000    1.000
A[, 6]No    8.790e-01  7.807e-01   1.126    0.261
A[, 6]Yes   7.966e-01  7.788e-01   1.023    0.307

Residual standard error: 1.095 on 300 degrees of freedom
Multiple R-squared:  0.005158,	Adjusted R-squared:  -0.001474 
F-statistic: 0.7778 on 2 and 300 DF,  p-value: 0.4604


Call:
lm(formula = A$num_mental_ilnesses ~ t)

Residuals:
    Min      1Q  Median      3Q     Max 
-0.8826 -0.8265 -0.8100  1.1306  5.1636 

Coefficients:
            Estimate Std. Error t value Pr(>|t|)    
(Intercept)  0.89580    0.24014   3.730 0.000229 ***
t           -0.00660    0.02302  -0.287 0.774576    
---
Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1

Residual standard error: 1.101 on 297 degrees of freedom
  (4 observations deleted due to missingness)
Multiple R-squared:  0.0002766,	Adjusted R-squared:  -0.003089 
F-statistic: 0.08217 on 1 and 297 DF,  p-value: 0.7746

> sink("readme.txt", append=TRUE)
> summary(lm(A$num_mental_ilnesses2 ~A[,3]))
> summary(lm(A$num_mental_ilnesses2 ~A[,4]))
> summary(lm(A$num_mental_ilnesses2 ~A[,5]))
> summary(lm(A$num_mental_ilnesses2 ~A[,6]))
> summary(lm(A$num_mental_ilnesses2 ~t))
> summary(lm(A$m_ill_or_not2 ~A[,3]))
> summary(lm(A$m_ill_or_not2 ~A[,4]))
> summary(lm(A$m_ill_or_not2 ~A[,5]))
> summary(lm(A$m_ill_or_not2 ~A[,6]))
> summary(lm(A$m_ill_or_not2 ~t))
> sink()


Call:
lm(formula = A$num_mental_ilnesses2 ~ A[, 3])

Residuals:
    Min      1Q  Median      3Q     Max 
-1.9681 -1.5266  0.1202  1.1202  9.2968 

Coefficients:
            Estimate Std. Error t value Pr(>|t|)    
(Intercept)  2.05642    0.23945   8.588 5.07e-16 ***
A[, 3]      -0.08830    0.05403  -1.634    0.103    
---
Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1

Residual standard error: 1.517 on 297 degrees of freedom
  (4 observations deleted due to missingness)
Multiple R-squared:  0.008912,	Adjusted R-squared:  0.005575 
F-statistic: 2.671 on 1 and 297 DF,  p-value: 0.1033


Call:
lm(formula = A$num_mental_ilnesses2 ~ A[, 4])

Residuals:
    Min      1Q  Median      3Q     Max 
-2.0159 -1.4766 -0.0159  0.9841  8.9841 

Coefficients:
                                                            Estimate Std. Error t value Pr(>|t|)  
(Intercept)                                                   0.3333     0.8693   0.383   0.7016  
A[, 4]No                                                      1.6825     0.8897   1.891   0.0596 .
A[, 4]No, but I regularly participate in an EA online group   1.6344     0.9104   1.795   0.0736 .
A[, 4]Yes, occasionally                                       1.3462     0.8858   1.520   0.1297  
A[, 4]Yes, often                                              1.1432     0.8794   1.300   0.1946  
---
Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1

Residual standard error: 1.506 on 298 degrees of freedom
Multiple R-squared:  0.02933,	Adjusted R-squared:  0.0163 
F-statistic: 2.251 on 4 and 298 DF,  p-value: 0.06363


Call:
lm(formula = A$num_mental_ilnesses2 ~ A[, 5])

Residuals:
    Min      1Q  Median      3Q     Max 
-2.0011 -1.5848  0.1654  1.1654  9.3319 

Coefficients:
            Estimate Std. Error t value Pr(>|t|)    
(Intercept)  2.08439    0.34797   5.990 6.01e-09 ***
A[, 5]      -0.08326    0.07130  -1.168    0.244    
---
Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1

Residual standard error: 1.516 on 299 degrees of freedom
  (2 observations deleted due to missingness)
Multiple R-squared:  0.004541,	Adjusted R-squared:  0.001212 
F-statistic: 1.364 on 1 and 299 DF,  p-value: 0.2438


Call:
lm(formula = A$num_mental_ilnesses2 ~ A[, 6])

Residuals:
    Min      1Q  Median      3Q     Max 
-1.7984 -1.6158  0.2016  1.2016  9.2016 

Coefficients:
              Estimate Std. Error t value Pr(>|t|)  
(Intercept) -3.878e-15  1.071e+00   0.000   1.0000  
A[, 6]No     1.798e+00  1.079e+00   1.666   0.0967 .
A[, 6]Yes    1.616e+00  1.077e+00   1.501   0.1345  
---
Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1

Residual standard error: 1.514 on 300 degrees of freedom
Multiple R-squared:  0.01166,	Adjusted R-squared:  0.005067 
F-statistic: 1.769 on 2 and 300 DF,  p-value: 0.1723


Call:
lm(formula = A$num_mental_ilnesses2 ~ t)

Residuals:
    Min      1Q  Median      3Q     Max 
-2.0964 -1.5447  0.1544  1.1544  9.2547 

Coefficients:
            Estimate Std. Error t value Pr(>|t|)    
(Intercept)  2.19677    0.33090   6.639  1.5e-10 ***
t           -0.05016    0.03172  -1.581    0.115    
---
Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1

Residual standard error: 1.518 on 297 degrees of freedom
  (4 observations deleted due to missingness)
Multiple R-squared:  0.008347,	Adjusted R-squared:  0.005008 
F-statistic:   2.5 on 1 and 297 DF,  p-value: 0.1149


Call:
lm(formula = A$m_ill_or_not2 ~ A[, 3])

Residuals:
    Min      1Q  Median      3Q     Max 
-0.7611 -0.6938  0.2658  0.2927  0.3062 

Coefficients:
            Estimate Std. Error t value Pr(>|t|)    
(Intercept)  0.77453    0.07110  10.894   <2e-16 ***
A[, 3]      -0.01345    0.01604  -0.839    0.402    
---
Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1

Residual standard error: 0.4504 on 297 degrees of freedom
  (4 observations deleted due to missingness)
Multiple R-squared:  0.002362,	Adjusted R-squared:  -0.0009972 
F-statistic: 0.7031 on 1 and 297 DF,  p-value: 0.4024


Call:
lm(formula = A$m_ill_or_not2 ~ A[, 4])

Residuals:
    Min      1Q  Median      3Q     Max 
-0.8710 -0.6875  0.2540  0.3125  0.6667 

Coefficients:
                                                            Estimate Std. Error t value Pr(>|t|)  
(Intercept)                                                   0.3333     0.2595   1.285   0.2000  
A[, 4]No                                                      0.4127     0.2656   1.554   0.1213  
A[, 4]No, but I regularly participate in an EA online group   0.5376     0.2718   1.978   0.0488 *
A[, 4]Yes, occasionally                                       0.3590     0.2644   1.357   0.1757  
A[, 4]Yes, often                                              0.3542     0.2625   1.349   0.1783  
---
Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1

Residual standard error: 0.4495 on 298 degrees of freedom
Multiple R-squared:  0.02254,	Adjusted R-squared:  0.009421 
F-statistic: 1.718 on 4 and 298 DF,  p-value: 0.1459


Call:
lm(formula = A$m_ill_or_not2 ~ A[, 5])

Residuals:
    Min      1Q  Median      3Q     Max 
-0.7305 -0.7177  0.2772  0.2798  0.2823 

Coefficients:
             Estimate Std. Error t value Pr(>|t|)    
(Intercept)  0.733081   0.103298   7.097 9.31e-12 ***
A[, 5]      -0.002572   0.021165  -0.122    0.903    
---
Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1

Residual standard error: 0.45 on 299 degrees of freedom
  (2 observations deleted due to missingness)
Multiple R-squared:  4.938e-05,	Adjusted R-squared:  -0.003295 
F-statistic: 0.01477 on 1 and 299 DF,  p-value: 0.9034


Call:
lm(formula = A$m_ill_or_not2 ~ A[, 6])

Residuals:
    Min      1Q  Median      3Q     Max 
-0.7345 -0.7016  0.2655  0.2984  0.2984 

Coefficients:
              Estimate Std. Error t value Pr(>|t|)  
(Intercept) -6.837e-15  3.175e-01   0.000   1.0000  
A[, 6]No     7.016e-01  3.200e-01   2.192   0.0291 *
A[, 6]Yes    7.345e-01  3.193e-01   2.300   0.0221 *
---
Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1

Residual standard error: 0.449 on 300 degrees of freedom
Multiple R-squared:  0.01804,	Adjusted R-squared:  0.0115 
F-statistic: 2.756 on 2 and 300 DF,  p-value: 0.06514


Call:
lm(formula = A$m_ill_or_not2 ~ t)

Residuals:
    Min      1Q  Median      3Q     Max 
-0.7515 -0.7072  0.2767  0.2868  0.3009 

Coefficients:
             Estimate Std. Error t value Pr(>|t|)    
(Intercept)  0.759607   0.098306   7.727 1.71e-13 ***
t           -0.004031   0.009425  -0.428    0.669    
---
Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1

Residual standard error: 0.4508 on 297 degrees of freedom
  (4 observations deleted due to missingness)
Multiple R-squared:  0.0006157,	Adjusted R-squared:  -0.002749 
F-statistic: 0.183 on 1 and 297 DF,  p-value: 0.6691

```
