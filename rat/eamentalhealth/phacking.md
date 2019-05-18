# A practical exercise in p-hacking (or not)

## Introduction

Among the respondents of the 2019 EA Mental Health Survey, 54.45% identified as male, 33.33% identified as female, and 12.21% described themselves in various other terms or declined to answer. This gives us an interesting oportunity to test the hypothesis: do people who neither identify as male or female have higher rates of mental ilnesses?

The data at our disposal comprises:

- Answers to the question "Which of these conditions have you been formally diagnosed with?". Answers are character strings, For example: "[304] "Depression, Anxiety, Bipolar Disorder"
- Answers to the question "Which of these conditions do you think you may have, but have never been formally diagnosed with?". Answers are character strings, for example: "[304] "Depression, Anxiety, Bipolar Disorder"
- Answers to the question "What is your gender?".

We can thus create the following six variables:
- A: Number of mental ilnesses the person has been diagnosed with.
- B: Number of mental ilnesses the person has either been diagnosed with or think they have.
- C: A binary variable: 0 if the person has not been diagnosed with any mental ilnesses, 1 otherwise
- D: A binary variable: 0 if the person has neither been diagnosed with a mental ilness, nor do they think they have one, and 1 otherwise.
- X: A binary variable: 1 if the person belongs to the 12.21% of respondents who don't describe themselves as male or female, or decline to provide their gender, 0 otherwise
- Y: A binary variable. 1 if tthe person belongs to the 7.59% of respondents who don't describe themselves as male or female, 0 otherwise. It represents X excluding the 4.62% of respondents who decline to reveal their gender.

Thus, we can regress the first four variables on the fourth and fifth.

## Results

If we choose only one among the 8 comparisons, the results are *not* whatever we want them to be, because the data is extremely suggestive of one interpretation. But we can massage them, concluding either:
a) If we only report B ~ X (the only regression which did not reach significance), we find no significant effect, smallish effect which could be due to chance, because p>0.1.
b) If we only report A ~ Y, we find a huge effect; whereas male or female EAs have a mean of 0.76 mental ilnesses, gender nonconforming EAs have a mean of 1.6 mental ilnesses, p < 0.001. If we bother to [calculate the exact p-value](https://www.wolframalpha.com/input/?i=N(mean%3D0,+standard+deviation+%3D+0.23271)+>+0.84798), it's [~0.0003649317](https://www.wolframalpha.com/input/?i=((2476491678888003+e)%2F18446744073709551616)). Additionally, "the most conservative method, which is free of dependence and distributional assumptions, is the Bonferroni correction" [Wikipedia](https://en.wikipedia.org/wiki/Multiple_comparisons_problem). If we harshly apply it to correct for having tested 8 hypothesis, we get p = 0.0003649317*8 = 0.002919452 ~ 0.003, which is still ridiculously low.

## A note on regressions and frequentist probability.
If you have 303 values for the variable A: {A1, A2, A3, ..., A303} and 303 values for the variable B. {B1, B2, B3, ..., B303}, you consider lines of the form A = I + C*B, and look at their associated points {(I+C*B1,B1),(I+C*B2,B2), (I+C*B3,B3), ..., (I+C*B303,B303)}. They are separated from the points {(A1,B1),(A2,B2),(A3,B3),..., (A303,B303)} by whatever distance.

For example, with I and C set, the point (I+C*B1, B1) is separated from (A1,B1) by a distance of sqrt((I+C*B1 - A1)^2 - (B1-B1)^2) = sqrt(((I+C*B1 - A1)^2)) = abs(I+C*B1 - A1). In the mathematical concept of distance, which is always greater than 0, but we do want the sign, so d1 = (I+C*B1 - A1). All in all, you have 303 such distances: {d1, d2, d3, ..., d4}

You then find the values I and C which minimize the sum of the distances from the point (Ai, Bi) to the point (I+C*Bi, Bi). That is, you find the line A = I + C*B which best fits your data. We'll want to distinguish between I and C as variables and (II,CC) as the point which solves their minimization problem.

Now, you can consider the distances which you calculated before: {d1, d2, d3, ..., d4}, treat them like rightful variables, and calculate it's mean and its standard deviation. Intuitively, the mean is going to be 0, because otherwise, you would have another better line (just change the intercept). Keep the standard deviation of the distances = SD in mind, though.

If you're a frequentist, you can then assign a p-value to that. Once you've found out the value (II,CC), you pretend that you were a virtuous Bayesian all along, and it just happened that you had the following prior for C:
- You had previously assigned p=0.5 to being a gaussian distribution centered at 0, with standard deviation SD (the standard deviation of the mean of the distances)
- And the remaining p=0.5 to C being a gaussian distribution centered at CC and with a standard deviation of SD.

The frequentist then carries a process which is similar to, but not quite same process which bayesians would if they had that prior and encountered the observations: frequentist update on C>CC, not on C=CC and then they multiply their probabilities by ~2 [1]. Bayesian rationalists are astonished at this method, and don't contemplate it with frustration, utter contempt and disregard, because they have better things to do. Nonetheless, sometimes they don't have enough computational power, or find libraries written with frequentist assumptions to be very convenient, and go along.

### As for the cold hard facts, have a look at the data yourself:
### A ~ X
n=303
Line of best fit: A = 1.62030 +  0.48781*X
Frequentist confidence that the term which multiplies the X is different from 0: p < 0.1 


#### Code and output
```
> summary(
+   lm(
+     A ~ X
+     )
+   )


Call:
lm(formula = A ~ X)

Residuals:
    Min      1Q  Median      3Q     Max 
-2.1081 -1.6203 -0.1081  0.8919  9.3797 

Coefficients:
            Estimate Std. Error t value Pr(>|t|)    
(Intercept)  1.62030    0.09271  17.477   <2e-16 ***
X            0.48781    0.26531   1.839    0.067 .  
---
Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1

Residual standard error: 1.512 on 301 degrees of freedom
Multiple R-squared:  0.01111,	Adjusted R-squared:  0.007821 
F-statistic:  3.38 on 1 and 301 DF,  p-value: 0.06696

```

## A ~ Y
n=303
Line of best fit: A = 0.76071 +  0.84798*Y
Frequentist confidence that the term which multiplies the Y is different from 0: p < 0.001.
```
> summary(
+   lm(
+     A ~ Y
+     )
+   )

Call:
lm(formula = A ~ Y)

Residuals:
    Min      1Q  Median      3Q     Max 
-1.6087 -0.7607 -0.7607  0.3913  5.2393 

Coefficients:
             Estimate Std. Error t value Pr(>|t|)    
(Intercept)   0.76071    0.06411  11.865  < 2e-16 ***
Y             0.84798    0.23271   3.644 0.000316 ***
---
Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1

Residual standard error: 1.073 on 301 degrees of freedom
Multiple R-squared:  0.04225,	Adjusted R-squared:  0.03907 
F-statistic: 13.28 on 1 and 301 DF,  p-value: 0.0003161
```

## B ~ X
n=303
Line of best fit: B = 2.4662 + 0.5609*X
Frequentist confidence that the term which multiplies the X is different from 0: p > 0.1

```
> summary(
+   lm(
+     B ~ X
+     )
+   )


Call:
lm(formula = B ~ X)

Residuals:
    Min      1Q  Median      3Q     Max 
-3.0270 -2.4662 -0.4662  1.5338 13.5338 

Coefficients:
            Estimate Std. Error t value Pr(>|t|)    
(Intercept)   2.4662     0.1443  17.091   <2e-16 ***
X             0.5609     0.4129   1.358    0.175    
---
Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1

Residual standard error: 2.353 on 301 degrees of freedom
Multiple R-squared:  0.006091,	Adjusted R-squared:  0.002789 
F-statistic: 1.845 on 1 and 301 DF,  p-value: 0.1754
```

## B ~ Y
n=303
Line of best fit: B = 1.60714 + 0.95807*Y
Frequentist confidence that the term which multiplies the Y is different from 0: p<0.01

```
> summary(
+   lm(
+     B ~ Y
+     )
+   )

Call:
lm(formula = B ~ Y)

Residuals:
    Min      1Q  Median      3Q     Max 
-2.5652 -1.6071  0.3929  1.3929  9.3929 

Coefficients:
             Estimate Std. Error t value Pr(>|t|)    
(Intercept)   1.60714    0.08959  17.939  < 2e-16 ***
Y             0.95807    0.32517   2.946  0.00347 ** 
---
Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1

Residual standard error: 1.499 on 301 degrees of freedom
Multiple R-squared:  0.02803,	Adjusted R-squared:  0.0248 
F-statistic: 8.681 on 1 and 301 DF,  p-value: 0.003466
```

## C ~ X
n=303
Line of best fit: C = 0.43985 + 0.15474*X
Frequentist confidence that the term which multiplies the X is different from 0: p<0.1

```
> summary(lm(C ~ X))

Call:
lm(formula = C ~ X)

Residuals:
    Min      1Q  Median      3Q     Max 
-0.5946 -0.4399 -0.4399  0.5602  0.5602 

Coefficients:
            Estimate Std. Error t value Pr(>|t|)    
(Intercept)  0.43985    0.03049  14.424   <2e-16 ***
X            0.15474    0.08727   1.773   0.0772 .  
---
Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1

Residual standard error: 0.4974 on 301 degrees of freedom
Multiple R-squared:  0.01034,	Adjusted R-squared:  0.007051 
F-statistic: 3.144 on 1 and 301 DF,  p-value: 0.0772
```

## C ~ Y
n=303
Line of best fit: C= 0.43214+ 0.35047*Y
Frequentist confidence that the term which multiplies the Y is different from 0: p<0.01
```
> summary(lm(C ~ Y))

Call:
lm(formula = C ~ Y)

Residuals:
    Min      1Q  Median      3Q     Max 
-0.7826 -0.4321 -0.4321  0.5679  0.5679 

Coefficients:
             Estimate Std. Error t value Pr(>|t|)    
(Intercept)   0.43214    0.02935  14.721  < 2e-16 ***
Y             0.35047    0.10655   3.289  0.00112 ** 
---
Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1

Residual standard error: 0.4912 on 301 degrees of freedom
Multiple R-squared:  0.0347,	Adjusted R-squared:  0.03149 
F-statistic: 10.82 on 1 and 301 DF,  p-value: 0.001123

```

## D ~ X
n=303
Line of best fit: = 0.70000 + 0.21304*X
Frequentist confidence that the term which multiplies the X is different from 0: p<0.05

```
> summary(lm(D ~ X))

Call:
lm(formula = D ~ X)

Residuals:
   Min     1Q Median     3Q    Max 
-0.913 -0.700  0.300  0.300  0.300 

Coefficients:
             Estimate Std. Error t value Pr(>|t|)    
(Intercept)   0.70000    0.02682  26.099   <2e-16 ***
X             0.21304    0.09735   2.188   0.0294 *  
---
Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1

Residual standard error: 0.4488 on 301 degrees of freedom
Multiple R-squared:  0.01566,	Adjusted R-squared:  0.01239 
F-statistic: 4.789 on 1 and 301 DF,  p-value: 0.0294

```


## D ~ Y
n=303
Line of best fit: = 0.69925 + 0.07897*Y
Frequentist confidence that the term which multiplies the Y is different from 0: p<0.05

```
> summary(lm(D ~ Y))

Call:
lm(formula = D~ Y)

Residuals:
    Min      1Q  Median      3Q     Max 
-0.8378 -0.6993  0.3008  0.3008  0.3008 

Coefficients:
            Estimate Std. Error t value Pr(>|t|)    
(Intercept)  0.69925    0.02759  25.340   <2e-16 ***
y            0.13859    0.07897   1.755   0.0803 .  
---
Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1

Residual standard error: 0.4501 on 301 degrees of freedom
Multiple R-squared:  0.01013,	Adjusted R-squared:  0.006841 
F-statistic:  3.08 on 1 and 301 DF,  p-value: 0.08027
```

[1]: In particular, their p-value is the probability that, if the null hypothesis were true, a value greater or equal than CC would be observed.
The probability that a gaussian centered at CC produces an output greater than CC is 0.5, so a Bayesian with the fake frequentist prior would normalize the p-value: p-value / (p-value + 0.5), which, if the p-value is close to 0, as in out case, amounts to dividing by 0.5, i.e., multiplying by 2.
