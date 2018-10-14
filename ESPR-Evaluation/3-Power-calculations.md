# Power calculations  
  
Using R we will do some power calculations  
Necessary library pwr, loads with library(pwr)  
Necessary function: pwr.t2n.test  
See: https://www.statmethods.net/stats/power.html  
  
Optimistic: We reach everyone  
Pessimistic: We reach 66% of treatment and control group.
  
## Year 1, pessimistic projections  
 ith n-treatment=20, n-control = 20, power = 0.9,sig.level= 0.05, power = 0.9, minimal detectable effect in standard deviations (d) = ?  
  
t test power calculation   
  
n1 = 20  
n2 = 20  
d = 1.051997  
sig.level = 0.05  
power = 0.9  
alternative = two.sided  
  
## Year 1, optimistic projections  
 With n_treatment=30, n_control = 60, power = 0.9,sig.level= 0.05, minimal detectable effect = ?  
  
t test power calculation   
  
n1 = 30  
n2 = 60  
d = 0.7328756  
sig.level = 0.05  
power = 0.9  
alternative = two.sided  
  
With n = ?, power = 0.9,sig.level= 0.05, power = 0.9, minimal detectable effect = 0.5  
  
Two-sample t test power calculation   
  
n = 85.03128  
d = 0.5  
sig.level = 0.05  
power = 0.9  
alternative = two.sided  
  
NOTE: n is number in *each* group  
  
  
## Year 2, pessimistic projections  
With n_treatment=40, n_control = 40, power = 0.9,sig.level= 0.05, minimal detectable effect = ?  
  
t test power calculation   
  
n1 = 40  
n2 = 40  
d = 0.7339255  
sig.level = 0.05  
power = 0.9  
alternative = two.sided  
  
## Year 2, optimistic projections  
With n_treatment=60, n_control = 120, power = 0.9,sig.level= 0.05, minimal detectable effect = ?  
  
t test power calculation   
  
n1 = 60  
n2 = 120  
d = 0.5153056  
sig.level = 0.05  
power = 0.9  
alternative = two.sided  
  
  
## Year 3, pessimistic projections  
 With n_treatment=60, n_control = 60, power = 0.9,sig.level= 0.05, minimal detectable effect = ?  
  
t test power calculation   
  
n1 = 60  
n2 = 60  
d = 0.5967207  
sig.level = 0.05  
power = 0.9  
alternative = two.sided  
  
## Year 3, optimistic projections  
 With n_treatment=90, n_control = 180, power = 0.9,sig.level= 0.05, minimal detectable effect = ?  
  
t test power calculation   
  
n1 = 90  
n2 = 180  
d = 0.4200132  
sig.level = 0.05  
power = 0.9  
alternative = two.sided  
  
## Year 4, pessimistic projections  
 With n_treatment=80, n_control = 80, power = 0.9,sig.level= 0.05, minimal detectable effect = ?  
  
t test power calculation   
  
n1 = 80  
n2 = 80  
d = 0.5156619  
sig.level = 0.05  
power = 0.9  
alternative = two.sided  
  
## Year 4, optimistic projections  
 With n_treatment=120, n_control = 240, power = 0.9,sig.level= 0.05, minimal detectable effect = ?  
  
t test power calculation   
  
n1 = 120  
n2 = 240  
d = 0.3633959  
sig.level = 0.05  
power = 0.9  
alternative = two.sided  
  
## Population necessary to detect an effect size of 0.2 with significance level = 0.05 and power = 0.9  
  
Here the free variable was d= minimal detectable effect  
With n = ?, power = 0.9,sig.level= 0.05, power = 0.9, minimal detectable effect = 0.2  
  
Two-sample t test power calculation   
  
n = 526.3332  
d = 0.2  
sig.level = 0.05  
power = 0.9  
alternative = two.sided  
  
NOTE: n is number in *each* group  
  
here the free variable was n, the population of the treatment group  
son = population of the treatmente group = population of the control group  
necessary to detect an effect of 0.2  
  
## Population necessary to detect an effect size of 0.5 with significance level = 0.05 and power = 0.9  
  
Two-sample t test power calculation   
  
n = 85.03128  
d = 0.5  
sig.level = 0.05  
power = 0.9  
alternative = two.sided  
  
NOTE: n is number in *each* group  
  
## Population necessary to detect an effect size of 0.2 with significance level = 0.10 and power = 0.9  
  
Two-sample t test power calculation   
  
n = 428.8664  
d = 0.2  
sig.level = 0.1  
power = 0.9  
alternative = two.sided  
  
NOTE: n is number in *each* group  
  
  
## Population necessary to detect an effect size of 0.5 with significance level = 0.10 and power = 0.9  
  
Two-sample t test power calculation   
  
n = 69.19719  
d = 0.5  
sig.level = 0.1  
power = 0.9  
alternative = two.sided  
  
NOTE: n is number in *each* group  
  
  
## Conclusions.  
Even after 4 years, under the most optimistic population projections (i.e., every participant answers our surveys every year, and 60 students who didn't get selected also do), we wouldn't have enough power to detect an effect size of 0.2 standard deviations with significance level = 0.05.  However, it seems feasible to detect the kinds of effects which would justify the upward of $150.000 / year costs of ESPR within 3 years. The minimum effect which justifies the costs of ESPR should be determined beforehand, as should the axis along which we measure. I would also suggest to expand the RCT to SPARC once its feasibility has been tested at ESPR.  
  
