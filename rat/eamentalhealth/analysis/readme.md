# Data Analysis

## Index:

1. Is the population which answered the survey representative of EA overall?  
- 1.1. According to age.
- 1.2. According to country.
- 1.3. According to gender.
- Bonus: [A practical exercise in p-hacking (or not)](https://nunosempere.github.io/rat/eamentalhealth/analysis/p-hacking.html)
- 1.4. Bottom line.
2. Does EA have a mental health problem?
3. Is more involvement with EA correlated with mental ilness?  
4. Is being mentally ill predictive of answering yes to: "Do you think you could personally benefit from EA community mental health resources?"
5. Is having a mental disorder, or thinking you could potentially benefit from mental health ressources correlated with thinking that providing them is likely to be one of the most effective interventions available?
6. Striving for Consistency. When is effective use of the EA Community's resources != the most effective interventions?

## 1. Is the population which answered the survey representative of EA overall?

### 1.1. According to age
![]([nunosempere.github.com/eamentalhealth/analysis/A1.png)

### 1.2. According to country.
![]([nunosempere.github.com/eamentalhealth/analysis/A2.png)

### 1.3. According to gender.
EA Survey 2018: 
> The majority of people who took the survey reported being male (67%), while 29% of respondents reported that they were female, and approximately 4% described themselves as other or declined to self-identify. This is closely aligned with the 2017 survey, which had the following gender breakdown: “70.1% identified as male, 26.01% identified as female, 1.9% respondents identified as “other”, and another 21 respondents preferred not to answer.”

However, in this survey, 54.46% of respondents reported being male, 33.33% of respondents reported being female, and 12.21% described themselves as other (7.59%) or declined to self-identify (4.62%).

### 1.4. Bottom line:
Editorial bottom line: With respect to age, country, and gender, there seem to be significant but not overwhelming differences. The differences in gender identification might be indicative of selection effects affecting this survey. This is because perhaps people in this third category have higher rates of mental ilness. I have explored this hypothesis at length here: [A practical exercise in p-hacking (or not)](https://nunosempere.github.io/rat/eamentalhealth/analysis/p-hacking.html).

## 2. Does EA have a mental health problem?
Initially, I was intending to find out the different mental disorder rates in the different countries, and combine that with the distribution in the data. The webpage [Our World in Data](https://ourworldindata.org/mental-health) provides the necessary data:

![share-with-mental-and-substance-disorders.png]

We see that the distribution is broadly similar across the countries among which EA has a presence. Most importantly, it doesn't surpass ~25% in any country, whereas among survey respondents:
- 45% have been diagnosed with one or more mental disorders.
- 71% either have been diagnosed with one or more mental disorders, or intuit they have one.
- The average number of mental ilnesses respondents have been diagnosed with is 0.82
- The average number of mental ilnesses respondents have either been diagnosed with or intuit they have is 1.68. This number is higher than one because some (many respondents) have more than one disorder.

Thus, we can conclude with certainty that there are selection effects going on. Whether this is at the level of the EA community or at the survey level is not deducible from the data. That is, it could either be that EA attracts people with mental disorders, or that the survey attracts respondents with mental disorders. Thus, we suggest adding a mental health section to the yearly EA Survey by Rethink Charity.

## 3. Is more involvement with EA correlated with mental ilness?

The first four questions in our survey relate to involvement with EA: 
1. How involved are you in the Effective Altruism Community?	
2. Do you attend EA meetings?	
3. How much impact do EA ideas have on your life?	
4. Do you donate part of your income to GiveWell recommended charities? 	

And two measures of mental ilness:
- A. A binary variable indicating whether a person was diagnosed with any mental ilness or not.
- B. A binary variable indicating whether a person was diagnosed with any mental ilness / think they have a mental ilness, or not
- C. An integer variable with the number of mental ilnesses a person has.
- D. An integer variable with the number of mental ilnesses a person has or thinks they have.

We have run 20 linear models, regressing each of our measures of mental ilness with the answers to each of the four questions, and their sum (where verbal scales are converted to numerical ones when required. For example, a {"No", "Yes"} is converted to {0,1}. As a technical note, whether it's converted to {0,1} or to {1,2} doesn't affect the regression coefficient, just the intercept)

In 17/20 cases, we get a positive but insignificant effect. One case is ambiguous and instill insignificant, and the remaining 2/20 cases are negative but still insignificant. That is, further involvement with EA across all but one model makes one less likely to have mental ilnesses, and to have fewer mental ilnesses, but at no point does this reach significance thresholds.

For example, consider whether attending EA meeting has a positive effect on the binary variable: has been diagnosed with a mental health ilness.

```
> summary(lm(A$m_ill_or_not ~ A$Do.you.attend.EA.meetings.))

Call:
lm(formula = A$m_ill_or_not ~ A$Do.you.attend.EA.meetings.)

Residuals:
    Min      1Q  Median      3Q     Max 
-0.5238 -0.4375 -0.4359  0.5625  0.6667 

Coefficients:
                                                                                  Estimate Std. Error t value Pr(>|t|)
(Intercept)                                                                         0.3333     0.2893   1.152    0.250
A$Do.you.attend.EA.meetings.No                                                      0.1905     0.2961   0.643    0.520
A$Do.you.attend.EA.meetings.No, but I regularly participate in an EA online group   0.1505     0.3029   0.497    0.620
A$Do.you.attend.EA.meetings.Yes, occasionally                                       0.1026     0.2948   0.348    0.728
A$Do.you.attend.EA.meetings.Yes, often                                              0.1042     0.2926   0.356    0.722

Residual standard error: 0.501 on 298 degrees of freedom
Multiple R-squared:  0.005741,	Adjusted R-squared:  -0.007604 
F-statistic: 0.4302 on 4 and 298 DF,  p-value: 0.7868

```
The key column is "Estimate". Smaller numbers are better, and we see that the more often one goes, the less likely is one to have been diagnosed with a mental ilness. No > No, but I regularly participate in an EA online group  > Yes, occasionally > Yes often. 

In the interest of total disclosure, here is a link with the 20 regressions carried out, and the code used to generate them: ![]([nunosempere.github.com/eamentalhealth/regressions_EA_mental_health.html) 

The bottomline seems to be that EA is correlated with better mental health, across almost all measures. However, the error bars are humongous, and no significance thresholds are reached. Note that this is only valid for people who are already involved enough with EA to answer this survey. Curiously, I was kind of expecting the opposite result. It would just have been so much more interesting / contrarian.

### 4. Is being mentally ill predictive of answering yes to: "Do you think you could personally benefit from EA community mental health resources?"

Yes, with p<0.001. In fact, p=6.93e-09. The obvious result is indeed obvious, and it serves as a proof of concept: we have enough power to find out *some* things. 

## 5. Is having a mental disorder, or thinking you could potentially benefit from mental health ressources correlated with thinking that providing them is likely to be one of the most effective interventions available?

Take a moment to make your predictions before you read ahead.

```
> colnames(A)[c(23,24,26,27)]
[1] "X.I.believe.that.offering.mental.health.resources.to.its.members.is.an.effective.use.of.the.EA.Community.s.resources.."                           
[2] "X.I.believe.that.offering.mental.health.resources.to.effective.altruists.is.NOT.likely.to.be.one.of.the.most.effective.interventions.available..."
[3] "Do.you.think.you.could.personally.benefit.from.EA.community.mental.health.resources."                                                             
[4] "Which..if.any..of.the.following.resources.do.you.think.you.could.potentially.benefit.from."                                                       

> summary(lm((A[,23]=="Agree" | A[,23]=="Strongly agree")  ~ A[,26] == "Yes"))

Call:
lm(formula = (A[, 23] == "Agree" | A[, 23] == "Strongly agree") ~ 
    A[, 26] == "Yes")

Residuals:
    Min      1Q  Median      3Q     Max 
-0.7188 -0.4286  0.2812  0.2812  0.5714 

Coefficients:
                     Estimate Std. Error t value Pr(>|t|)    
(Intercept)           0.42857    0.03612  11.864  < 2e-16 ***
A[, 26] == "Yes"TRUE  0.29018    0.05558   5.221 3.32e-07 ***
---
Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1

Residual standard error: 0.4779 on 301 degrees of freedom
Multiple R-squared:  0.08305,	Adjusted R-squared:   0.08 
F-statistic: 27.26 on 1 and 301 DF,  p-value: 3.321e-07
```

I had forgotten how high the heaven is and how deep the earth is! If people think they can benefit from mental health ressources, the probability that they agree or strongly agree with the statement "I believe that offering mental health resources to its members is an effective use of the EA Community's resources" goes up from 42.857% to 29.018% + 42.857% = 71.875%, with a p-value of 3.321e-07!

Similarly, the probability that they agree with the statement "I believe that offering mental health resources to effective altruists is NOT likely to be one of the most effective interventions available" goes down from 32.571% to 32.571%-16.165% = 16.406%, with a p-value of 0.001409!

```
> summary(lm((A[,24]=="Agree" | A[,24]=="Strongly agree")  ~ A[,26] == "Yes"))

Call:
lm(formula = (A[, 24] == "Agree" | A[, 24] == "Strongly agree") ~ 
    A[, 26] == "Yes")

Residuals:
    Min      1Q  Median      3Q     Max 
-0.3257 -0.3257 -0.1641  0.6743  0.8359 

Coefficients:
                     Estimate Std. Error t value Pr(>|t|)    
(Intercept)           0.32571    0.03260   9.991  < 2e-16 ***
A[, 26] == "Yes"TRUE -0.16165    0.05016  -3.223  0.00141 ** 
---
Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1

Residual standard error: 0.4313 on 301 degrees of freedom
Multiple R-squared:  0.03335,	Adjusted R-squared:  0.03014 
F-statistic: 10.39 on 1 and 301 DF,  p-value: 0.001409
```

Two narratives present themselves: 
1: This is a bias, a component of self-interest.
2: People who feel mental pain have *grokked* negative utilitarianism, or similarly have different intuitions about the matter.

For various factors, some of which are opaque to me, my system 1 is more sympathetic with the first framing. Thus, I'd propose that this topic is more conducive to research analysis of the sort in which QALYs are estimated, and that asking the broad public for opinions is not that valuable.

The effect is very robust to different modelizations: regressing instead on empty answers to question 25:  "Which if any of the following resources do you think you could potentially benefit from?", regressing on whether the respondents have a mental disorder instead of whether they say they'd benefit from mental health ressources, including "Not sure" answers in the regression, etc.

Here is the above, presented visually

![]([nunosempere.github.com/eamentalhealth/analysis/A3.png)

The following table is the cold, raw, hard data for the graphic. 
```
> # Distribution of answers to "Q22: I believe that offering mental health resources to effective altruists\nis NOT likely to be one of the most effective interventions available?"
               group      freq                                                type
1   Neutral/Not sure 47.656250                          Thinks they could benefit.
2           Disagree 28.125000                          Thinks they could benefit.
3  Strongly disagree  7.031250                          Thinks they could benefit.
4              Agree 13.281250                          Thinks they could benefit.
5     Strongly agree  3.125000                          Thinks they could benefit.
6          No answer  0.781250                          Thinks they could benefit.
7   Neutral/Not sure 44.571429  Does not think they could benefit, or is not sure.
8           Disagree 19.428571  Does not think they could benefit, or is not sure.
9              Agree 24.000000  Does not think they could benefit, or is not sure.
10         No answer  1.714286  Does not think they could benefit, or is not sure.
11    Strongly agree  8.571429  Does not think they could benefit, or is not sure.
12 Strongly disagree  1.714286  Does not think they could benefit, or is not sure.
```

Much could be said about how the above is why we take care of cultivating rationality.

## 6. Striving for Consistency. When is effective use of the EA Community's resources != the most effective interventions?
According to my understanding of "effective" and "effective altruism", the following two questions are equivalent:
- "I believe that offering mental health resources to its members is an effective use of the EA Community's resources."	
- "I believe that offering mental health resources to effective altruists is NOT likely to be one of the most effective interventions available." 	

However, I insisted in adding the second question because the connotations are slightly different, and the bias that they'll produce will go in opposite directions. For an intuition pump:
> A Latinobarometro poll in 2004 showed that while a clear majority (63 percent) in Latin America would never support a military government, 55 percent would not mind a nondemocratic government if it solved economic problems.
> - Source: The Power of Survey Design.

As it turns out, only 30% of respondents gave the same answer to the two questions. This is not correlated with mental disorders, age, sex, gender, impact of EA ideas in one's life or involvement in the EA community. It is, however, weakly correlated with donating to GiveWell recommended charities.
