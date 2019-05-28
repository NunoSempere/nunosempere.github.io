# EA Mental Health Survey: Results and Analysis.

## Index:

#### A. Questions asked by the survey

#### B. Exploratory plots.

#### C. Data Analysis

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
6. When is an effective use of the EA Community's resources != the most effective intervention?
7. How does further involment in EA correlate with opinions on the value of mental health resources?
8. How does productivity lost because of mental health problems correlate with opinions on the value of mental health resources (and viceversa)?
9. How does mental health affect productivity, and how is this mediated by access to healthcare?
- 9.1. How does mental health affect productivity?
- 9.2. How is lost productivity mediated by treatment and access to treatment?
10. How does access to mental health ressources vary with a variety of factors?
- 10.1. By countries or continent.
- 10.2. By race/ethnicity.
- 10.3. By mental health
- 10.4. By age
- 10.5. By involvement in EA.

#### D. Implications for mental health in EA overall, guided by some insightful comments made by the respondents.
- 1.1. Selection effects in EA. 
- 1.2. Do mental health problems stem from EA-specific beliefs?
- 1.3. EA may not have a comparative advantage in providing mental health ressources.
- 1.4. EA France has something going on 
- 1.5. Visceral comparison with global poverty
- 1.6. Moral hazard.
- 1.7. Layers of indirectness and pathways to impact.
- 1.8. A support group for EAs with ADHD
- 1.9. Cheap ressources.
- 1.10. Providing mental health ressources is creepy

#### E. Summary.

## A. Questions asked by the survey.

1. How involved are you in the Effective Altruism Community?	
2. Do you attend EA meetings?	
3. How much impact do EA ideas have on your life?	
4. Do you donate part of your income to GiveWell recommended charities? 	
5. Which of these conditions have you been formally diagnosed with? 
6. Which of these conditions do you think you may have, but have never been formally diagnosed with?	
7. During the past 14 days, how many hours did you miss from work because of mental health problems?	
8. During the past 14 days, how many hours did you miss from work because of any other reason, such as vacation, other commitments, etc.?	
9. During the past 14 days, about how many hours did you actually work?	
10. During the past 14 days, how much did mental health problems affect your productivity while you were working?	
11. During the past 14 days, how much did mental health problems affect your ability to do your regular daily activities, other than work at a job?  	
12. Are the past 14 days representative of your average mental health?  	
13. If you answered "No" to the previous question, how has your mental health differed over the past 14 days?	
14. How challenging was it to receive the mental healthcare services you needed within the past 12 months?	
15. How challenging is it to find useful information on mental healthcare services? 	
16. Do you experience financial difficulties as a result of mental healthcare?	
17. "I am currently receiving the mental healthcare I need." 	
18. How satisfied are you with the mental healthcare you've received?	
19. Which of the following treatments have you tried? 	
20. Any other thoughts you'd like to share on mental healthcare access?	
21. "I believe that offering mental health resources to its members is an effective use of the EA Community's resources."	
22. "I believe that offering mental health resources to effective altruists is NOT likely to be one of the most effective interventions available." 	
23. Please explain your answers to the questions above. 	
24. Do you think you could personally benefit from EA community mental health resources?	
25. Which (if any) of the following resources do you think you could potentially benefit from? 	
26. Any other thoughts you'd like to share on EA-sponsored mental health resources? 	
27. Which country do you live in? 	
28. What is your age?
29. What is your gender?	
30. What is your race/ethnicity?

## B. Exploratory plots.

![](https://nunosempere.github.io/rat/eamentalhealth/Q1.png)  
![](https://nunosempere.github.io/rat/eamentalhealth/Q2.png)  
![](https://nunosempere.github.io/rat/eamentalhealth/Q3.png)  
![](https://nunosempere.github.io/rat/eamentalhealth/Q4.png)  
![](https://nunosempere.github.io/rat/eamentalhealth/Q5.png)  
![](https://nunosempere.github.io/rat/eamentalhealth/Q5and6.png)  
![](https://nunosempere.github.io/rat/eamentalhealth/Q6.png)  
![](https://nunosempere.github.io/rat/eamentalhealth/Q7-9b.png)  
![](https://nunosempere.github.io/rat/eamentalhealth/Q10.png)  
![](https://nunosempere.github.io/rat/eamentalhealth/Q11.png)  
![](https://nunosempere.github.io/rat/eamentalhealth/Q12.png)  
![](https://nunosempere.github.io/rat/eamentalhealth/Q13.png)  
![](https://nunosempere.github.io/rat/eamentalhealth/Q14.png)  
![](https://nunosempere.github.io/rat/eamentalhealth/Q14-b.png)  
![](https://nunosempere.github.io/rat/eamentalhealth/Q15.png)  
![](https://nunosempere.github.io/rat/eamentalhealth/Q15-b.png)  
![](https://nunosempere.github.io/rat/eamentalhealth/Q16.png)  
![](https://nunosempere.github.io/rat/eamentalhealth/Q17.png)  
![](https://nunosempere.github.io/rat/eamentalhealth/Q17-2.png)  
![](https://nunosempere.github.io/rat/eamentalhealth/Q18.png)  
![](https://nunosempere.github.io/rat/eamentalhealth/Q19.png)  
![](https://nunosempere.github.io/rat/eamentalhealth/Q21.png)  
![](https://nunosempere.github.io/rat/eamentalhealth/Q22.png)  
![](https://nunosempere.github.io/rat/eamentalhealth/Q24.png)  
![](https://nunosempere.github.io/rat/eamentalhealth/Q25.png)  
![](https://nunosempere.github.io/rat/eamentalhealth/Q28.png)  

The code to produce them can be found [here](https://nunosempere.github.io/rat/eamentalhealth/)

## C. Data Analysis

### 1. Is the population which answered the survey representative of EA overall?

#### 1.1. According to age
![](https://nunosempere.github.io/rat/eamentalhealth/analysis/A1.png)
![]()

#### 1.2. According to country.
![](https://nunosempere.github.io/rat/eamentalhealth/analysis/A2.png)

#### 1.3. According to gender.
EA Survey 2018: 
> The majority of people who took the survey reported being male (67%), while 29% of respondents reported that they were female, and approximately 4% described themselves as other or declined to self-identify. This is closely aligned with the 2017 survey, which had the following gender breakdown: “70.1% identified as male, 26.01% identified as female, 1.9% respondents identified as “other”, and another 21 respondents preferred not to answer.”

However, in this survey, 54.46% of respondents reported being male, 33.33% of respondents reported being female, and 12.21% described themselves as other (7.59%) or declined to self-identify (4.62%).

#### 1.4. Bottom line:
Editorial bottom line: With respect to age, country, and gender, there seem to be significant but not overwhelming differences. The differences in gender identification might be indicative of selection effects affecting this survey. This is because perhaps people in this third category have higher rates of mental ilness. I have explored this hypothesis at length here: [A practical exercise in p-hacking (or not)](https://nunosempere.github.io/rat/eamentalhealth/analysis/p-hacking.html).

### 2. Does EA have a mental health problem?
Initially, I was intending to find out the different mental disorder rates in the different countries, and combine that with the distribution in the data. The webpage [Our World in Data](https://ourworldindata.org/mental-health) provides the necessary data:

![](https://nunosempere.github.io/rat/eamentalhealth/analysis/share-with-mental-and-substance-disorders.png)

We see that the distribution is broadly similar across the countries among which EA has a presence. Most importantly, it doesn't surpass ~25% in any country, whereas among survey respondents:
- 45% have been diagnosed with one or more mental disorders (from our list).
- 71% either have been diagnosed with one or more mental disorders, or intuit they have one.
- The average number of mental ilnesses respondents have been diagnosed with is 0.82
- The average number of mental ilnesses respondents have either been diagnosed with or intuit they have is 1.68. This number is higher than one because some (many respondents) have more than one disorder. This is not particularly surprising: see [Understanding Comorbid Depression and Anxiety](https://www.psychiatrictimes.com/articles/understanding-comorbid-depression-and-anxiety). 

Thus, we can conclude with certainty that there are selection effects going on. Whether this is at the level of the EA community or at the survey level is not deducible from the data. That is, it could either be that EA attracts people with mental disorders, or that the survey attracts respondents with mental disorders. Thus, we suggest adding a mental health section to the yearly EA Survey by Rethink Charity.

### 3. Is more involvement with EA correlated with mental ilness?

The first four questions in our survey relate to involvement with EA: 
- How involved are you in the Effective Altruism Community?	
- Do you attend EA meetings?	
- How much impact do EA ideas have on your life?	
- Do you donate part of your income to GiveWell recommended charities? 	

And two measures of mental ilness:
- A. A binary variable indicating whether a person was diagnosed with any mental ilness (from our list) or not.
- B. A binary variable indicating whether a person was diagnosed with any mental ilness / think they have a mental ilness, or not
- C. An integer variable with the number of mental ilnesses a person has been diagnosed with.
- D. An integer variable with the number of mental ilnesses a person has been diagnosed with, or thinks they have.

We have run 20 linear models, regressing each of our measures of mental ilness with the answers to each of the four questions, and their sum (where verbal scales are converted to numerical ones when required. For example, a {"No", "Yes"} is converted to {0,1}. As a technical note, whether it's converted to {0,1} or to {1,2} doesn't affect the regression coefficient, just the intercept)

In 17/20 cases, we get a positive but insignificant effect. One case is ambiguous and instill insignificant, and the remaining 2/20 cases are negative but still insignificant. That is, further involvement with EA across all but one model makes one less likely to have mental ilnesses, and to have fewer mental ilnesses, but at no point does this reach significance thresholds.

For example, consider whether attending EA meeting has a positive effect on the binary variable: has been diagnosed with a mental health ilness.

```
> summary(lm(A$m_ill_or_not ~ A$Do.you.attend.EA.meetings.))

Coefficients:
                                                                                  Estimate Std. Error t value Pr(>|t|)
(Intercept)                                                                         0.3333     0.2893   1.152    0.250
A$Do.you.attend.EA.meetings.No                                                      0.1905     0.2961   0.643    0.520
A$Do.you.attend.EA.meetings.No, but I regularly participate in an EA online group   0.1505     0.3029   0.497    0.620
A$Do.you.attend.EA.meetings.Yes, occasionally                                       0.1026     0.2948   0.348    0.728
A$Do.you.attend.EA.meetings.Yes, often                                              0.1042     0.2926   0.356    0.722

```
The key column is "Estimate". Smaller numbers are better, and we see that the more often one goes, the less likely is one to have been diagnosed with a mental ilness. No > No, but I regularly participate in an EA online group  > Yes, occasionally ~ Yes often. 

In the interest of total disclosure, [here](https://nunosempere.github.io/rat/eamentalhealth/analysis/regressions_EA_mental_health.html)  is a link with the 20 regressions carried out, and the code used to generate them.

The bottomline seems to be that EA is correlated with better mental health, across almost all measures. However, the error bars are humongous, and no significance thresholds are reached. Note that this is only valid for people who are already involved enough with EA to answer this survey. 

Curiously, I was kind of expecting the opposite result. It would just have been so much more interesting / contrarian. See also: [Efffective Altruists, not as mentally ill as you think](https://slatestarcodex.com/2015/03/06/effective-altruists-not-as-mentally-ill-as-you-think/)

#### 4. Is being mentally ill predictive of answering yes to: "Do you think you could personally benefit from EA community mental health resources?"

The two questions which directly ask about mental ilness are:
- Which of these conditions have you been formally diagnosed with? 
- Which of these conditions do you think you may have, but have never been formally diagnosed with?	

And the questions which ask about benefiting from mental health ressources are:
- Do you think you could personally benefit from EA community mental health resources?
- Which if any of the following resources do you think you could potentially benefit from?

I model having a mental ilness as before. Independent on the modelization, the answer our question is yes, people with mental ilnesses are more likely to think they can benefit from mental health ressources, with p-values ranging from 0.0004736 to
7.612e-12. The obvious result is indeed obvious, and it serves as a proof of concept: we have enough power to find out *some* things. 

### 5. Is having a mental disorder, or thinking you could potentially benefit from mental health ressources, correlated with thinking that providing them is likely to be one of the most effective interventions available?

Take a moment to make your predictions before you read ahead.

```
> colnames(A)[c(23,24,26,27)]
[1] "X.I.believe.that.offering.mental.health.resources.to.its.members.is.an.effective.use.of.the.EA.Community.s.resources.."                           
[2] "X.I.believe.that.offering.mental.health.resources.to.effective.altruists.is.NOT.likely.to.be.one.of.the.most.effective.interventions.available..."
[3] "Do.you.think.you.could.personally.benefit.from.EA.community.mental.health.resources."                                                             
[4] "Which..if.any..of.the.following.resources.do.you.think.you.could.potentially.benefit.from."                                                       

> summary(lm((A[,23]=="Agree" | A[,23]=="Strongly agree")  ~ A[,26] == "Yes"))

Coefficients:
                     Estimate Std. Error t value Pr(>|t|)    
(Intercept)           0.42857    0.03612  11.864  < 2e-16 ***
A[, 26] == "Yes"TRUE  0.29018    0.05558   5.221 3.32e-07 ***
---
Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1
```

I had forgotten how deep the waters are. If people think they can benefit from mental health ressources, the probability that they agree or strongly agree with the statement "I believe that offering mental health resources to its members is an effective use of the EA Community's resources" goes up from 42.857% to 29.018% + 42.857% = 71.875%, with a p-value of 3.321e-07!

Similarly, the probability that they agree with the statement "I believe that offering mental health resources to effective altruists is NOT likely to be one of the most effective interventions available" goes down from 32.571% to 32.571%-16.165% = 16.406%, with a p-value of 0.001409!

```
> summary(lm((A[,24]=="Agree" | A[,24]=="Strongly agree")  ~ A[,26] == "Yes"))

Coefficients:
                     Estimate Std. Error t value Pr(>|t|)    
(Intercept)           0.32571    0.03260   9.991  < 2e-16 ***
A[, 26] == "Yes"TRUE -0.16165    0.05016  -3.223  0.00141 ** 
---
Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1

```

Two narratives present themselves: 
1: This is a bias, a component of self-interest.
2: People who feel mental pain have *grokked* negative utilitarianism, or similarly have different intuitions about the matter.

For various factors, some of which are opaque to me, my system 1 is more sympathetic with the first framing. Thus, I'd propose that this topic is more conducive to research analysis of the sort in which QALYs are estimated, and that asking the broad public for opinions is not that valuable.

The effect is very robust to different modelizations: regressing instead on empty answers to question 25:  "Which if any of the following resources do you think you could potentially benefit from?", regressing on whether the respondents have a mental disorder instead of whether they say they'd benefit from mental health ressources, including "Not sure" answers in the regression, etc.

Here is the above, presented visually

![](https://nunosempere.github.io/rat/eamentalhealth/analysis/A3.png)

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

### 6. Striving for Consistency. When is effective use of the EA Community's resources != the most effective interventions?
According to my understanding of "effective" and "effective altruism", the following two questions have equivalent meanings:
- "I believe that offering mental health resources to its members is an effective use of the EA Community's resources."	
- "I believe that offering mental health resources to effective altruists is NOT likely to be one of the most effective interventions available." 	

However, I insisted in adding the second question because the connotations are slightly different, and the bias that they'll produce will go in opposite directions. For an intuition pump:
> A Latinobarometro poll in 2004 showed that while a clear majority (63 percent) in Latin America would never support a military government, 55 percent would not mind a nondemocratic government if it solved economic problems.
> - Source: The Power of Survey Design.

As it turns out, only 30% of respondents gave the same answer to the two questions. This is not correlated with mental disorders, age, sex, gender, impact of EA ideas in one's life or involvement in the EA community. It is, however, weakly correlated with donating to GiveWell recommended charities.

### 7. How does further involment in EA correlate with opinions on the value of mental health resources?
The correlation between involvement in EA and having a positive opinion of providing mental health ressources is positive, but small and not significant at all. I wouldn't read anything into this.

The above is true both if we create a dummy for each possible answer (which are: "Strongly disagree", "Disagree", "", "Neutral/Not sure", "Agree", "Strongly agree") and if we instead convert the answers into a number ("Strongly disagree" = -2, "Disagree" = -1, ""=0, "Neutral/Not sure"=0, "Agree"=1, "Strongly agree"=2) and run a regression on that. For that matter, the switch function in R proved usatisfactory for working on strings; I wrote one more suited to my purposes and sufficient for n=303.

```
switch2 <- function(Elements, Compare_With, Output_if_found, Output_if_Else){
  Lista = vector() 
  for(element in Elements){
    i=1 
    found=FALSE
    for(comparator in Compare_With){
       if(element == comparator){
         found = TRUE
         Lista = c(Lista, Output_if_found[i])
       }
      i =i +1
    }
    if(found == FALSE){
      Lista = c(Lista,Output_if_Else)
    }
  }
  return(Lista)
}

## This function can then be used as follows:
> colnames(A)[c(23,24)]
[1] "X.I.believe.that.offering.mental.health.resources.to.its.members.is.an.effective.use.of.the.EA.Community.s.resources.."                           
[2] "X.I.believe.that.offering.mental.health.resources.to.effective.altruists.is.NOT.likely.to.be.one.of.the.most.effective.interventions.available..."

switch2(A[,23], c("Strongly disagree", "Disagree", "Agree","Strongly agree"), c(-2,-1,1,2),0) -> Numerical_23
switch2(A[,23], c("Strongly disagree", "Disagree", "Agree","Strongly agree"), c(-2,-1,1,2),0) -> Numerical_24

```

### 8. How does productivity lost because of mental health problems correlate with opinions on the value of mental health resources (and viceversa)?

The two questions which ask about productivity lost because of mental health problems are:
- During the past 14 days, how many hours did you miss from work because of mental health problems?	(numerical answer)
- During the past 14 days, how much did mental health problems affect your productivity while you were working?	(numerical answer)

And the two questions which ask about effectiveness of providing mental health ressources are:
- "I believe that offering mental health resources to its members is an effective use of the EA Community's resources."	
- "I believe that offering mental health resources to effective altruists is NOT likely to be one of the most effective interventions available." 	

Under a wide range of modelizations / operationalizations, there is ~0 correlation between the two sets of answers. The one exception is if we consider a dummy variable for "hours lost due to mental ilness > 0". In that case, respondents who did lose >0 hours are somewhat more likely to support offering mental health resources, but this does not reach significant levels.

This is surprising, because a positive opinion of offering mental health resources is strongly correlated with thinking you could benefit from them, thinking you could benefit from them is strongly correlated with having a mental condition, and having a mental condition is strongly correlated with losing hours because of mental health.

Of course the relation "(significantly) correlated to" is not transitive in theory, and coming up with a nifty example is not difficult. But it is most curious that the relation is not transitive *in practice*.

```
> colnames(A)[c(23,24,26)]
[1] "X.I.believe.that.offering.mental.health.resources.to.its.members.is.an.effective.use.of.the.EA.Community.s.resources.."                           
[2] "X.I.believe.that.offering.mental.health.resources.to.effective.altruists.is.NOT.likely.to.be.one.of.the.most.effective.interventions.available..."
[3] "Do.you.think.you.could.personally.benefit.from.EA.community.mental.health.resources."

> summary(lm(Numerical_23 ~ A[,26]=="No"))
    ## Significantly correlated, with p-value = 6.068e-07
> summary(lm(A[,26] == "No" ~ A$m_ill_or_not))
    ## Significantly correlated, with p-value = 0.0004736
> summary(lm(A$m_ill_or_not ~ hours_lost))
    ## Significantly correlated, with p-value = 5.479e-07
> summary(lm(Numerical_23 ~ hours_lost))
    ## Not significantly correlated!
```

### 9. How does mental health affect productivity, and how is this mediated by access to healthcare?
What is the effect of mental health on productivity, and how does access to healthcare mediate it? 

#### 9.1. How does mental health affect productivity?
We can correlate our four markers of mental ilness on our two measures of lost productivity lost. However, the correlation runs both ways: from the data we cannot deduce whether people with mental conditions lose productivity, or whether losing productivity (i.e., losing a job) makes people more likely to be mentally ill. 

If we assume that the effect is purely unidirectional (mental ilness -> lost productivity), three highlights are:
- Being diagnosed with one or more mental conditions would cause a loss of ~9 hours per 2 weeks.
- Each additional diagnosed mental ilness would cause a loss of ~5 hours per 2 weeks.
- On a subjective 10 point scale, answers to the question ("During the past 14 days, how much did mental health problems affect your productivity while you were working?") increase by ~2 points if the respondent perceives they have at least 1 mental condition.

In total, we run 12 regressions, which are fully documented below. The casual reader is welcome to skip them, and continue to the next section.

```

# Call: lm(formula = A$m_ill_or_not ~ hours_lost)

Coefficients:
            Estimate Std. Error t value Pr(>|t|)    
(Intercept) 0.403430   0.030657  13.159  < 2e-16 ***
hours_lost  0.009909   0.001886   5.254 2.94e-07 ***
---
Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1


# Call: lm(formula = hours_lost ~ A$m_ill_or_not)

Coefficients:
               Estimate Std. Error t value Pr(>|t|)    
(Intercept)       2.010      1.168   1.721   0.0863 .  
A$m_ill_or_not    8.998      1.713   5.254 2.94e-07 ***
---
Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1

# Call: lm(formula = hours_lost ~ A$m_ill_or_not2)

Coefficients:
                Estimate Std. Error t value Pr(>|t|)    
(Intercept)       0.3951     1.6253   0.243    0.808    
A$m_ill_or_not2   8.1099     1.9224   4.219 3.32e-05 ***
---
Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1

# Call: lm(formula = hours_lost ~ A$m_ill_or_not + (A$m_ill_or_not2 & 
    !A$m_ill_or_not))

    Coefficients:
                                      Estimate Std. Error t value Pr(>|t|)    
(Intercept)                             0.3951     1.5960   0.248    0.805    
A$m_ill_or_not                         10.6125     2.0274   5.235 3.24e-07 ***
A$m_ill_or_not2 & !A$m_ill_or_notTRUE   3.4571     2.3352   1.480    0.140    
---
Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1

# Call: lm(formula = hours_lost ~ A$num_mental_ilnesses)

Coefficients:
                      Estimate Std. Error t value Pr(>|t|)    
(Intercept)              2.174      1.051   2.069   0.0395 *  
A$num_mental_ilnesses    4.856      0.767   6.331 9.58e-10 ***
---
Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1

# Call: lm(formula = hours_lost ~ A$num_mental_ilnesses2)

Coefficients:
                       Estimate Std. Error t value Pr(>|t|)    
(Intercept)             -0.6053     1.2060  -0.502    0.616    
A$num_mental_ilnesses2   4.0640     0.5317   7.643 3.33e-13 ***
---
Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1

# Call: lm(formula = hours_lost ~ A$num_mental_ilnesses + A$num_mental_ilnesses2)

Coefficients:
                       Estimate Std. Error t value Pr(>|t|)    
(Intercept)             -0.5355     1.2055  -0.444    0.657    
A$num_mental_ilnesses    1.4484     1.0981   1.319    0.188    
A$num_mental_ilnesses2   3.3057     0.7826   4.224 3.25e-05 ***
---
Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1

# Call: lm(formula = A$m_ill_or_not ~ effect_while_working)

Coefficients:
                     Estimate Std. Error t value Pr(>|t|)    
(Intercept)           0.10805    0.04885   2.212   0.0278 *  
effect_while_working  0.08744    0.01020   8.577 5.56e-16 ***
---
Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1

# Call: lm(formula = effect_while_working ~ A$m_ill_or_not)

Coefficients:
               Estimate Std. Error t value Pr(>|t|)    
(Intercept)      3.0062     0.1806  16.644  < 2e-16 ***
A$m_ill_or_not   2.2764     0.2654   8.577 5.56e-16 ***
---
Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1

# Call: lm(formula = effect_while_working ~ A$m_ill_or_not2)

Coefficients:
                Estimate Std. Error t value Pr(>|t|)    
(Intercept)       1.9518     0.2402   8.126 1.22e-14 ***
A$m_ill_or_not2   2.9226     0.2828  10.335  < 2e-16 ***
---
Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1

# Call: lm(formula = effect_while_working ~ A$num_mental_ilnesses)

Coefficients:
                      Estimate Std. Error t value Pr(>|t|)    
(Intercept)             3.1341     0.1630  19.228   <2e-16 ***
A$num_mental_ilnesses   1.1130     0.1185   9.394   <2e-16 ***
---
Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1

#  Call: lm(formula = effect_while_working ~ A$num_mental_ilnesses2)

Coefficients:
                       Estimate Std. Error t value Pr(>|t|)    
(Intercept)             2.43830    0.18171   13.42   <2e-16 ***
A$num_mental_ilnesses2  0.95910    0.07998   11.99   <2e-16 ***
---
Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1
```

#### 9.2. How is this mediated by treatment and access to treatment?
So unsurprisingly, having a mental ilness decreases both work hours, and self-reported productivity when working. Thus, a pressing question is whether therapy has an effect on that. 

Four questions ask about treatment or access to treatment:
- How challenging was it to receive the mental healthcare services you needed within the past 12 months?	
- How challenging is it to find useful information on mental healthcare services? 	
- "I am currently receiving the mental healthcare I need."
- How satisfied are you with the mental healthcare you've received?	

And we can correlate their answers with our measures for lost productivity.
- During the past 14 days, how many hours did you miss from work because of mental health problems?	(numerical answer)
- During the past 14 days, how much did mental health problems affect your productivity while you were working?	(numerical answer)

##### 9.2.1. Mediated by answers to "I am currently receiving the mental healthcare I need".

Respondents could choose one of the following options, after being prompted by the sentence "I am currently receiving the mental healthcare I need":
```
[1] "Strongly agree"                            
[2] "Agree"                                     
[3] "Strongly disagree"                         
[4] "Disagree"                                  
[5] "I do not currently need mental healthcare."
[6] ""                                          
```

We can thus define two dummy variables and regress on them.
```
> Receiving_positive = A[,19]%in%c("Agree", "Strongly agree")*1         ## 1/TRUE if the respondent thinks they're receiving the mental healthcare they need, 0/FALSE otherwise.
> Receiving_negative= A[,19]%in%c("Disagree", "Strongly disagree")*1    ## 1/TRUE if the respondent thinks they're not receiving the mental healthcare they need, 0/FALSE otherwise.
```

The results seem to indicate that when respondents receive the mental health care they think they need, they improve. Note that both of the coefficients are positive because the intercept refers to respondents who did not feel they needed mental healthcare. 

```
> summary(lm(hours_lost ~ Receiving_positive + Receiving_negative))

Call:
lm(formula = hours_lost ~ Receiving_positive + Receiving_negative)

Coefficients:
                       Estimate Std. Error t value Pr(>|t|)    
(Intercept)              0.6435     1.3885   0.463 0.643388    
Receiving_positiveTRUE   7.7986     2.0297   3.842 0.000151 ***
Receiving_negativeTRUE  10.3071     2.1209   4.860 1.96e-06 ***
---
Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1

> summary(lm(effect_while_working ~ Receiving_positive + Receiving_negative))

Call:
lm(formula = effect_while_working ~ Receiving_positive + Receiving_negative)

Coefficients:
                       Estimate Std. Error t value Pr(>|t|)    
(Intercept)              2.4818     0.2123  11.689  < 2e-16 ***
Receiving_positiveTRUE   2.1182     0.3077   6.884  3.5e-11 ***
Receiving_negativeTRUE   2.9386     0.3185   9.227  < 2e-16 ***
---
Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1

```

If this was fully rigorous, giving people "the mental healthcare they need" would reduce hours lost per two weeks from 10.3071 to 7.7986, that is, a difference of 2.5 hours per two weeks, or 1.25 hours per week. Results are similar if we:
- ask instead "How satisfied are you with the mental healthcare you've received?"
- exclude people who did not feel they needed mental healthcare (n=191).
- and further restrict the regression to respondents thought they had a mental condition from our list, or who had been diagnosed with one (n=175).
- or restrict it to people (who claim to have been) diagnosed with a mental condition (n=129).

In this last case, the implied effect doubles, to 2.2 hours saved per week, as seen below.

```
> m_ill3= (Receiving_positive | Receiving_negative) & A$m_ill_or_not
> sum(m_ill3)
[1] 124
> summary(lm(hours_lost[m_ill3] ~ Receiving_positive[m_ill3]))

Call:
lm(formula = hours_lost[m_ill3] ~ Receiving_positive[m_ill3])

Coefficients:
                               Estimate Std. Error t value Pr(>|t|)    
(Intercept)                      14.833      3.086   4.807 4.67e-06 ***
Receiving_positive[m_ill3]TRUE   -4.428      4.018  -1.102    0.273    
---
Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1
```

Note that, in none of the above cases we've gotten a significant effect. This is because outliers, for example, respondents who lost a job because of mental ilness, and thus ~40 hours per week, make the error bars huge. In this case, excluding outliers doesn't make sense at all; instead, knowing where the error comes from, I think it makes sense to not get hung up on p-values. As a proof of concept, here is the same regression as above, but considering the logarithm of hours lost (which gives less weigh to outliers); we "suddenly" reach significance (p-value of 0.00698). On the flipside, the logarithm of hours lost is not an intuitive unit in which to report results. 

```
> summary(lm(log(hours_lost[m_ill3]+1) ~ Receiving_positive[m_ill3]))
Coefficients:
                               Estimate Std. Error t value Pr(>|t|)    
(Intercept)                      2.0578     0.1994  10.322  < 2e-16 ***
Receiving_positive[m_ill3]TRUE  -0.7131     0.2596  -2.747  0.00698 ** 
---
Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1
```

Alas, we cannot take the above crosssections at face value. Imagine, for example, that people with lighter mental conditions find it easier to deal with the hassle of finding good treatment, which seems plausible. In that case, the causal arrow would go both ways: (getting good mental healthcare -> healing occurs -> people lose less hours each week), but also (having a lighter mental ilness -> easier to find good mental healthcare) + (having a lighter mental ilness -> loose less work hours). It could also be that, as people regress to the mean with respect to their mental ilness, and become happier, they attribute their improvement to whatever therapy they were receiving, and become more satisfied with it. If we assume that the bias goes in the direction of amplifying the effect of good mental healthcare, the above figures become an upper estimate of its effect.

In the ideal case, what I'd like to have is a randomized trial in which:
- Productivity and severity of mental ilness are measured across a population
- Mental healthcare is provided to a randomly selected part of the population; the treatment group.
- Part of the treatment group takes up that freely provided mental heathcare, and part of the control group pays for the treatment out of pocket.
- Some time passes.
- Productivity and severity of mental ilness are measured again, both in the control and treatment group.

### 10. How does access to mental health ressources vary with a wide variety of factors?

Acess is asked about in the following two questions:
14. How challenging was it to receive the mental healthcare services you needed within the past 12 months?	
15. How challenging is it to find useful information on mental healthcare services? 	

The main limitation of these questions is that the answers will depend on the subjective experience and capabilities of the respondents.

#### 10.1. By countries or continent.
With 52 countries and 303 respondents, we don't have the power to say anything. We still don't have anything to say if we aggregate by continent instead, except that unsuprisingly, respondents find it more difficult to access mental healthcare in Africa than in any other continent. However, the effect was not significant, given that very few respondents were from Africa.

#### 10.2. By race/ethnicity.
Perhaps unsurprisingly, white people find it less challenging to receive mental healthcare, and to find information about it. The effect is magnified when considering only respondents with a mental condition.
```
> summary(lm(switch2(A[,16][M_ILL2], c("Very easy", "Fairly easy", "Moderate", "Fairly hard", "Very hard"), c(3,1,-1,-3),0) ~ A$Race.ethnicity[M_ILL2]))

Coefficients:
                                                Estimate Std. Error t value Pr(>|t|)
(Intercept)                                      -1.6667     1.1053  -1.508    0.134
A$Race.ethnicity[M_ILL2]Asian                     0.9167     1.2960   0.707    0.481
A$Race.ethnicity[M_ILL2]Hispanic or Latino/a/x    0.6667     2.2105   0.302    0.763
A$Race.ethnicity[M_ILL2]Mixed race/Multi-racial   1.1667     1.4621   0.798    0.426
A$Race.ethnicity[M_ILL2]White                     1.7576     1.1178   1.572    0.118


> summary(lm(switch2(A[,16], c("Very easy", "Fairly easy", "Moderate", "Fairly hard", "Very hard"), c(3,1,-1,-3),0) ~ A$Race.ethnicity))

Coefficients:
                                        Estimate Std. Error t value Pr(>|t|)
(Intercept)                             -0.41667    0.39899  -1.044    0.297
A$Race.ethnicityAsian                    0.15580    0.49218   0.317    0.752
A$Race.ethnicityBlack                    0.41667    1.05562   0.395    0.693
A$Race.ethnicityHispanic or Latino/a/x   0.21667    0.73569   0.295    0.769
A$Race.ethnicityMiddle Eastern           0.41667    1.05562   0.395    0.693
A$Race.ethnicityMixed race/Multi-racial  0.08333    0.69106   0.121    0.904
A$Race.ethnicityWhite                    0.46730    0.40896   1.143    0.254
```

#### 10.3. By mental health
Among all our markers, having worse mental health is correlated with finding it more challenging to receive mental healthcare, and to find information about it. Sometimes the effect is significant, p<0.05, but it it is never large (the largest is a change of -0.16 in a -3 to +3 scale)

#### 10.4. By age
No effect. 

#### 10.5. By involvement in EA.
No effect. 

### 11. Implications for mental health in EA overall, guided by some insightful comments made by the respondents. 

Some of the questions asked their respondents for their thoughts, and I really appreciated some of the long and insightful answers. Here, I paraphrase and expand on some of the key ideas and leave a technical comment for the footnotes [1]. I have found these comments very useful as way to think about the problem of mental health in EA overall.

#### 11.1. Selection effects in EA. 
Some respondents suggested that EA attracts people with mental ilnesses. Perhaps there is a snowball effect going on, perhaps it selects from demographic which have higher rates of mental ilness. Thus, a particularly cost effective way to fight mental health in EA might be to do outreach amongst people who do not have mental health issues.

This model is consistent with finding out that, among effective altrists, more effective altruism is not correlated (or correlated weakly) with better mental health (see section 3.)

#### 11.2. Do mental health problems stem from EA-specific beliefs?
A respondent asked about how to deal with work-aholism when your work actually matters. Some people have talked with me about how, if ideas related to existential risk are internalized, Angst might occur. Thus, for EA specific problems, therapists familiar with EA ideas might help more than regular therapists. 

What follows are my own thoughts.

This model is not is not consistent with finding out that, among effective altrists, more effective altruism is not correlated (or correlated weakly) with better mental health (see section 3). That is, if effective altruism caused mental ilness, we have lost part of the probability mass which comes from (more effective altruism -> more mental ilness). Instead, only the probability mass corresponding to (if a certain level of effective altruism is reached -> more mental ilness). 

For a toy model, consider for example whether mental ilness is caused by involvement in effective altruism and mediated by understanding x-risk, that is, suppose that understanding x-risk led to (a chance of developing) depression/anxiety, and that higher levels of effective altruism led to higher chances of understanding x-risk. For example, suppose that numerical answers to "How involved are you in the EA community?", from 1 to 6 were such that: Answering 1 (not very involved) leads to a 10% probability of understanding x-risk, 2->20%, ..., 6-> 60%. Imagine then that our survey has serious selection effects (such that people with more mental ilness and people more familiar with effective altruism are more likely to participate). Then the effect would be amplified by these selection effects, and we *would* see a correlation between effective altruism and worse mental health. 

The fact that we *don't* is indicative of other models, like models with selection effects. For example, maybe obsessive thoughts relating to EA are exactly [like any other obsessive thoughts](https://slatestarcodex.com/2018/10/15/the-chamber-of-guf/). Maybe minds with mental conditions look for things to be depressed or anxious about, and effective altruism happens to provide some. Crucially, the counterfactual would not be not freaking out about stuff, it would be having fixated on something else to freak out about, like american politics, climate change, sexual assault, not being lovable, etc. *The content and origin of the idea being fixated on might be besides the point*. Under this model, EA therapists might be counterproductive.

#### 11.3. EA may not have a comparative advantage in providing mental health ressources.
Either the market or other organizations, like universities or other NGOs specifically dedicated to mental health (CAMH, Zendo are mentioned, but I am not familiar with them). 

#### 11.4. EA France has something going on 
EA France has a group in which they read *Feeling Good*, by David Burns.  I personally have benefitted from the book, and know that it's available on libgen (or a mirror, like b-ok.org).

Here is a formal invitation to EA France to talk about how the group is organized.

#### 11.5. Visceral comparison with global poverty
A respondent notes that they think someone who has nothing to eat in a developing country still has it worse than someone living with depression, and that they'd rather donate a 100 euros to cure two blind people from blindness than spend it on an hour of therapy for themselves. I empathize with this, and I also like second order effects. That is, going to therapy might allow someone to earn and donate more money, and thus cure more blind people, but this depends on the specifics of how much time is saved, how much money the person makes, how much therapy costs, and how much effort it takes to organize the whole thing.

#### 11.6. Moral hazard.
Some people may join EA just to use these resources. Or some EAs who were paying for their therapy might choose to get it for free instead. 

#### 11.7. Layers of indirectness and pathways to impact.
A respondent mentions that providing mental health ressources goes through two layers of indirectness: therapy may not help mental health, which may not help productivity. the comment stops here; what follows are my own thoughts.

Additionally, offering therapy does not mean that therapy is taken up, and an increase in productivity might not mean that the world will be made better. 

Thinking about this further, the case for providing EAs with mental healthcare seems to rest on several distinct pathways to impact:
1. Providing mental healthcare to anyone with a mental condition makes them happier, and this in itself makes the world better.
2. Providing mental healthcare to effective altruists earning to give makes them work more and thus earn more money, which they then donate to effective charities, and this makes the world better.
3. Providing mental heathcare to effective altruists working in really effective projects makes them more likely to succeed in their undertakings. If these undertakings succeed, this makes the world better.
4. Others, like "flourishing of the community". Although its specific impact might be difficult to measure, providing mental health, together with other measures, makes the community flourish, and this leads to a better world.

With regards to pathway 1, [perhaps effective altruism are not the best demographic to worry about](https://forum.effectivealtruism.org/posts/XWSTBBH8gSjiaNiy7/cause-profile-mental-health). 

With regards to pathway 2, we have a rough upwards crosssectional estimate of 2 hours of work saved per week if satisfactory mentalh healthcare is provided (with a more realistic estimate being 1 hour/week). If therapy lasts one hour per week, and the therapist has to be paid for one hour, and 10% of the counterfactual gain is donated, the math doesn't check out. However, this is only indicative, and one could argue that:
- The distribution is more important than the mean. That is, the average person does not exist; we may have a small number of people who could be a lot more effective if they had mental health, and a lot of people who wouldn't benefit that much (see image below)
    - This requires to argue that filtering and organizational costs are not likely to be significant. I am skeptical of this if organized centrally, and less skeptical if local EA groups organize it themselves.
- Gains because of therapy continue after therapy has ended
    - As opposed to regression to the mean? That is, the gains of therapy might not be people getting better, but people getting better sooner.
- People who recover from a mental ilness because of help from the EA community might not donate 10% of the counterfactual gain, but more. 

![](https://nunosempere.github.io/rat/eamentalhealth/analysis/Q7-9b.png)

With regards to pathway 3, it is my impression that people in top charities and EA organizations already get good mental healthcare, though about rogue effective altruists I cannot say much. 

With regards to other fuzzier pathways, they would have to be outlined first. 

In each of the first three cases, there are many different steps in the process of providing mental healthcare, until impact is reached. I do not think this is a case of the conjunctive fallacy, but more of a case of attrition.
- Mental healthcare is offered to EAs.
- Some, but not all the EAs who need it apply for it.
- Some non EAs also apply. They are somehow filtered.
- Some EAs who would have paid for healthcare out of their own pocket get it for free instead.
    - Note that people with mental conditions, the limiting factor may not be money, but spoons/energy/not procrastinating.
- Mental healthcare works, and improves the patient's mental health somehow.
- In pathway 1, the process ends here. 
- In pathway 2, better mental health leads to a degree of higher work efficiency / more work hours -> More donations to effective charities, f.ex., GiveDirectly -> Impact pathway of GiveDirectly.
- In pathway 3, better mental health -> higher likelihood of success -> pathway to impact of the effective project. The project presumably has to be at some point asessed.

All in all, althought the questions in our survey only ask about "offering mental health resources to effective altruists" in the abstract, the specific pathway to impact matters, because the several outlined here are different. In particular, if none of them work, being fuzzy about which one is in effect wouldn't help.

#### 11.8. A support group for EAs with ADHD
A commenter talked about forming a support group for EAs with ADHD. Here is a formal invitation to create one.

#### 11.9. Cheap ressources.
Whereas therapists are relatively expensive, it's relatively cheap to make [Nate Soares' writing on guilt] (http://mindingourway.com/guilt/) more widely known. I personally have also recently gotten some value out of Kaj Sotala's blogposts on psychological frameworks (https://kajsotala.fi/blog/blog_english/); there is a certain power in hearing other people talk about their struggles with mental conditions. 

SlateStarCodex's list of [mental health professionals](https://slatestarcodex.com/psychiat-list/), [ressources](https://www.reddit.com/r/raisedbynarcissists/comments/6cdmn2/new_here_helpful_posts_comments_from_rbnbestof/) by [r/raisedbynarcissists](https://www.reddit.com/r/raisedbynarcissists/wiki/helpfullinks), and in particular [this list of books for building your life](https://www.reddit.com/r/raisedbynarcissists/comments/1axuzu/book_list_for_building_your_life/), are free. I've personally gotten some value out of these [Strategies and tools for getting through a break up, from LessWrong](https://www.lesswrong.com/posts/opLKzAFQWCco8wQiH/strategies-and-tools-for-getting-through-a-break-up). Julia Wise seems to have [some](https://forum.effectivealtruism.org/posts/CJZGFxzHfdPuu2X76/a-mental-health-resource-for-ea-community) useful [things](https://forum.effectivealtruism.org/posts/ZGW8Tmc6mDWZTnqyo/burnout-and-self-care). The aforementioned *Feeling Good*, by David Burns is also free if found online (b-ok.org). 

The point being that there are a lot of mental health ressources and information online, if only one knew where to find them, and >10% of survey respondents answered that finding information on mental health ressources was hard or very hard.

![](https://nunosempere.github.io/rat/eamentalhealth/Q15-b.png)

Thus, it is a high tractability, high neglectedness, small to medium impact task to create such a list of mental ressources for the EA community, even if collated and scavenged from other sources. If such a ressource already exist, some respondents do not seem to know about it.

#### 11.10. Providing mental health ressources is creepy
In personal converations, a person in the outer orbit of the EA community has pointed out to me that providing mental health is creepy, and that they feel cringe when thinking about the idea. The word "cult" is mentioned. I am uncertain about their epistemic level, but it is not implausible that providing mental health may put prospective EAs off.


[1] [Technical note](https://concepts.effectivealtruism.org/concepts/information-hazards/): Let a be a variable which stands for an individual eas, and consider a mapping of O: A-> |N, such that O(a) falls in {1,...,n}, and consider a function like f(x) = c\*x^(-j)\*(1 + 1/sqrt(2\*pi\*9)\*exp(-x^2 / 2\*9}\*sin(x)/BB(6)), where BB is the busy beaver function. It may be that the counterfactual impact of eas follows such a distribution; j and c would be arbitrary constants, with j preferably greater than 3, because otherwise the variance is not well defined, and consider the relationship which the integral from 1 to k of f(x)dx and the integral from k+1 to n of f(x) dx have. It wouldn't  be unsurprising if O(a) were not inversely correlated with conscientiousnes and initiative, and correlated, perhaps causally, with more mental health problems, as these variables often are. Now consider the first k such that the integral from 1 to k of f(x)dx > the integral from k+1 to n of f(x) dx. The question is now whether for high O(a), offering mental health is worth it, given that O(a) is a priori unknown, and that computing the exact value of f(O(a)) is arduous / subject to Goodhart's law or to moral hazards. 

## E. Summary

We first provided some shiny plots which summarized our results. 

Then, we proceeded to analyze these results. We have seen that demographically, respondents varied somewhat compared with the 2018 EA Survey, but didn't worry too much about that. The rates of mental ilnesses were astoundingly high: 45% of respondents had been diagnosed with at least one mental condition, which shoots up to 71% if we include respondents who think they have a mental condition, but have not formally been diagnosed with one.

This makes us suspect selection effects, but from the data, we cannot know whether these play out at the level of our survey, or at the level of the EA community. For this reason, we'd **strongly suggest to add a mental health section to the annual EA survey**. Nonetheless, some conclusions can be reached despite a potential bias, because sometimes the bias either doesn't matter, or we know its direction. 

We also have the issue of p-hacking, or in general picking and choosing regressions to push a conclusion. Because computing power is cheap, we choose to instead run all the regressions, that is, we choose to operationalize our questions and to model our data in many different ways, and report the aggregate results. Additionally, most of our conclusions carry the caveat of coming from a crossectional analysis, a method which not only can be unreliable, but also doesn't tell us the direction of our effect. For example, if we run a regression GDP ~ education, we see that richer countries are more educated, but we can't say whether that is because they like to spend their money on education, or because being more educated makes them richer.

Nonetheless, our first conclusion is that, among the respondents of this survey, more involvement in the EA community is positively correlated with better mental health. The correlation does not reach any significance threshold whatsoever, and, we're relieved to find out that it doesn't go in the opposite direction. This is evidence against EA causing mental health problems, and a toy model is presented in which EA causes mental health through the idea of x-risk; we find that such a model is not consistent with our data. 

As a proof of concept, we run a correlation on whether having mental health problems is correlated with thinking one could benefit from mental health ressources; we find the expected correlation, and get an absurdly low p-value. We also run a correlation on potential self-interested, that is, we ask whether thinking one could benefit from mental health ressources is correlated with answering that providing these ressources would be an effective thing to do. Again, we get a positive correlation with absurdly low p-values.

We then ask what the effect of mental health on productivity is, and how access to treatment mediates it. We see that people lose a lot of hours because of mental ilness: an additional diagnosed mental ilness is correlated with a loss of ~5 hours per 2 weeks. But  conditions are highly comorbid, so being mentally ill is correlated with losing ~9 hours per 2 weeks. This is not homogeneusly distributed, but instead like a power law: a small proportion of respondents (~10%-20%) loose a lot of hours. Limiting our regression to that 10-20% takes our statistical power away, but nonetheless, knowing the shape of the distribution helps indicate what sort of interventions might be valuable.

Dividing respondents by whether they have received satisfactory healthcare, we find that those who have loose ~1-2 hours of work less than those who have not, and we think that this is probably and upwards estimate. In total, among our respondents 1 758 hours of work were lost because of mental ilness in the two weeks previous to our survey, compared to 16 737 hours worked, and 1 899 hours missed because of other reasons. We also ask whether productivity is lost because of mental ilness, but our scale is inadequate to estimate effects, because we do not know to quantify the amount of productivity lost which a "6" represents.

Several questions in our survey ask respondents for their personal opinions and insights, and some of the observations which they make are quite sharp. I present the ones which are likely to be useful, expand on some of them, and see whether the data gathered supports the hypothesis they propose. That section is likely to be accessible to the casual reader, nonetheless, here are some brief highlights: Many respondents seem to think that there are selection effects going on in EA. Others propose that EA itself causally leads to mental conditions, and I give some nondefinitive arguments to why that might not be the case, supported by the data at hand.  I sketch several layers which providing mental health would have to go through before the world is positively changed, consider three different possible pathways to impact which providing mental health to effective altruists may have, and warn that if none of them work, being fuzzy about which ones are in effect wouldn't help. Many respondents suggest creating or scavenging mental health ressources, and I mention some which have been of use to me. EA France seems to have something going on with a book club for reading *Feeling Good*, by David Burns, and I extend them an invitation to talk about it. 
