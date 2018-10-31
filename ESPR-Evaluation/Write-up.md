# ESPR-Evaluation Writeup

(Epistemic status: Cognitive dissonance. On the one hand )

## Introduction
I have spent the last 2-4 months thinking about how to evaluate the impact of the European Summer Camp on Rationality (ESPR) [1], a selective program affiliated with CFAR (Center for Applied Rationality) which takes brilliant highschoolers and teach thems a variety of rationality techniques. Here are the highlights of what I have found, as well as some remarks on what CFAR could do if it was interested in measuring impact with a randomized controlled trial (an RCT).

## Note to potential donors.
The question I am answering here is not "Should I donate to CFAR?" but "Which plan could be set in motion to better estimate ESPR's impact?".

## Current evidence

There isn't much evidence on how effective ESPR is, besides it's logical model. In the words of a student which came back this year as a Junior Counselor:

>... ESPR (teaches) smart people not to make stupid mistakes. Examples: betting, prediction markets decrease overconfidence. Units of exchange class decreases likelihood of spending time, money, other currency in counterproductive ways. The whole asking for examples thing prevents people from hiding behind abstract terms and to pretend to understand something when they don't. Some of this is learned in classes. A lot of good techniques from just interacting with people at espr.
>
>I've had conversations with otherwise really smart people and thought “you wouldn't be stuck with those beliefs if you'd gone though two weeks of espr”
>
>ESPR also increases self-awareness. A lot of espr classes / techniques / culture involves noticing things that happen in your head. This is good for avoiding stupid mistakes and also for getting better at accomplishing things.
>
>It is nice to be surrounded by very smart. ambitious people. This might be less relevant for people who do competitions like IMO or go to very selective universities. Personally, it is a fucking awesome and rare experience every time I meet someone really smart with a bearable personality in the real world. Being around lots of those people at espr was awesome. Espr might have made a lot of participants consider options they wouldn't seriously have before talking to the instructors like founding a startup, working on ai alignment, everything that galit talked about etc
>
>espr also increased positive impact participants will have on the world in the future by introducing them to effective altruism ideas. I think last year’s batch would have been affected more by this because I remember there being more on x-risk and prioritizing causes and stuff [3].

Thus, because CFAR has a similar logical model, the current evidence on ESPR, i.e, a literature review, would simply be the evidence CFAR has on itself. I've mainly studied [CFAR's 2015 Longitudinal Study](http://www.rationality.org/studies/2015-longitudinal-study) together with the more recent [Case Studies](http://rationality.org/studies/2016-case-studies) and the [2017 CFAR Impact report](http://www.rationality.org/resources/updates/2017/cfar-2017-impact-report).

I find myself confused, in the sense that I don't find it satisfactory, and I wouldn't go about collecting evidence in the same way. On the other hand, I respect these people, and I may be under the effects of tunnel vision after having been reading about RCTs for a couple of months. Alternatively, it could be that their Data Analyst is mostly a normal member of staff / ops person [4], and that justifying their impact is not a priority for this relatively young organization.

With regards to the first study, it notes that a control group would be a difficult thing to implement, because it would be necessary to find people who would like to come to the program and forbidding them to do so. The study tries to compensate for the lack of a control by being statistically clever. It seems to be rigorous enough for a study which is not an RCT.

But I feel like that is only partially sufficient. The magnitude of the effect found could be wildly overestimated; MIT's Abdul Latif Jameel Poverty Action Lab provides the following slides [5]:

![](https://nunosempere.github.io/ESPR-Evaluation/Pre-post-1.jpg)
![](https://nunosempere.github.io/ESPR-Evaluation/Pre-post-2.jpg)

I find them scary; depending on the method used to test your effect, you can get an effect size that is 4-5 times as great as the effect you find with an RCT, or about as great, in the other direction. The effects the CFAR study finds, f.ex. the one most prominently displayed in CFAR's webpage, an increased life satisfaction of 0.17 standard deviations (i.e., going from 50 to 56.75%) are small enough for me to worry about such inconveniences.

Recently, CFAR has moved away from that more rigorous kind of study to Case Studies and Student Profiles. This annoys me, because asking participants for counterfactual estimations is such a swamp of complexity and complications that the error bars are bound to be incredibly wide, and thus most of the impact probably comes from the uncertainty. Additionally, it is just very easy to get very positive reviews of mostly anything; searching for "nonviolent communication testimonials" brings up [this webpage](https://www.rachellelamb.com/testimonials/). In other words, I would expect to find similar texts at mostly any level of impact. 

Finally, one their three Organization Case Studies (Arbital) is now a failed project, but this doesn't change my mind much, because learning that a sparky person who attended CFAR founded a project to improve some aspect of the world didn't give me much information to begin with.

### A note on perverse incentives
To the extent that OpenPhilantropy prefers these and other weak forms of evidence *now*, rather than stronger evidence two-three years later, OpenPhilantropy might be giving ESPR perverse incentives. Note that with 20-30 students per year, even after we start an RCT, there must pass a number of years before we can amass some meaningful statistical power (see the power calculations). On the other hand, taking a process of iterated improvement as an admission of failure would also be pretty shitty.

The questions designing a RCT poses are hard, but the bigger problem is that there's an incentive to not ask them at all. But that would be agaist CFAR's ethos.

## Some power calculations.
(For more detailed numbers, see: [the actual numbers](https://nunosempere.github.io/ESPR-Evaluation/3-Power-calculations.html))

Even after 4 years, under the most optimistic population projections (i.e., every participant answers our surveys every year, and 60 students who didn't get selected also do), we wouldn't have enough power to detect an effect size of 0.2 standard deviations with significance level = 0.05. We would, under somewhat less optimistic projections (20 students and 20 individuals in the control group answer every year), be able to detect an effect of 0.5 standard deviations within 4 years, in whatever we measure. 

At any point, the length the RCT would have to go on would depend on the minimal detectable effect per unit of money we care about. Some relevant data is that every interation of ESPR costs upwards of $150,000, or $5,000 per student, and there is nothing magical about a 0.05 significance level. The full bayesian treatment will have to wait until I have my computer back.

At any point, if we only cared about frequentist statistical power, it would be much better if an RCT could be carried out by CFAR on its workshops, because they have more students.

## Details of the implementation

### Talking with the staff about whether an RCT is a good idea.

Without the support of the staff, an RCT could not go forward. In particular, an RCT will require that we don't accept promising applicants, i.e., from the 2 most promising applicants, we'd want to have 1 in the control group. This to be a forced decision would probably engender great resentment.  

Similarly, though we would prefer to have smaller groups, of 20, we wouldn't have enough power, even after 4 years if we went that route. Instead, we'd want to accept upwards of 32 students (-2 who, on expectation, won't get their visa on time). Other design studies, like ranking our applicants from 1 to 40, taking the best 20 and randomizing the last 20 (10 for ESPR, 10 for the control group) would appease the staff, but again wouldn't buy us enough power.  

If we want our final alumni pool to be equally as good as in previous years, we would want to increase our reach, our advertising efforts say ~4x, i.e., to find 90 excellent students in total, 30 for the control and 60 for the treatment group. This would be possible by, f.ex., asking every previous participant to nominate a friend, by announcing the camp to the most prestigious highschools in countries with a rationality community, etc. An SSC post / banner wouldn't hurt. A successful effort in this area seems necessary for the full buy in of the staff, and might require additional funds.  
  
### Spillovers.

If a promising person from the control group tried to apply the next year, we'd have to deny them the chance to come, or else lose the most promising people from the control group, losing validity.  

We also don't want people on the control group to be disheartened because they didn't get in. For this, I suggest dividing our application in two steps: One in which we select both groups, and a coin toss.  

If people have heard about ESPR, they might read writings by Kahneman, Bostrom, Yudkowsky, et al. If they aren't accepted, they might fulfill their need for cognition by continuing reading such materials. Thus, what we will measure will be the difference between applicants interested in rationality and applicants interested in rationality who go to ESPR, not between equally talented people with no previous contact. At any point, it would seem necessary to disallow explicit mentoring of applicants. Here, again, the full buy in of the staff is needed.  

SPARC is another camp which teaches very similar stuff. I have considered doing the RCT both on ESPR and SPARC at the same time, but SPARC's emphasis on math olympiad people makes that a little bit sketchy. However, because they are still very similar interventions, we don't want to have a person in the control group going to SPARC. This might be a sore point.  

### Stratification.

Suppose that after randomly allocating the students, we found that the treatment group was richer. This would *suck*, because maybe our effect is just them being, f.ex., healthier. In expectation, the two groups are the same, but maybe in practice they turn out not to be.  

An alternative would be to divide the students into rich and poor, and randomly choose in each bucket. This is refered to as stratification, and buys additional power, though I still have to get into the gritty details. I'm still thinking about along which variables we want to stratify, if at all, and further reflection is needed.

Note to self: Paired random assignment might be a problem with respect to attrition (f.ex. no visa on time); JPAL recommends strata of at least 4 people. 

### Incentives.
The survey takes 15-30 minutes to complete, and while I've tried to make it engaging and propose pauses, I think that an incentive is needed (i.e., the people in the control group might tell us to fuck off). 

I initially thought about donating X USD to the AMF in their name every time they completed a survey, but I realized that this would motivate the most altruistical individuals the most, thus getting selection effects. Now, I'm leaning towards just giving the survey takers that amount of money. 

As a lower bound, 40 people * 3 years * 2 surveys * 10 USD = 2400 USD, or 800 USD/year, as an upper bound, 60 people * 4 years * 4 surveys * 15 USD = 14400 USD or 3600 USD / year. I don't feel this is that significant in comparison to the total cost of the camp. More expensive, I think, is the time which I and others would work on this for free / the counterfactual projects we might undertake with that time. I am as of yet uncertain of the weight of this factor. 

### Take off and burn. 

To end with a high note, there is a noninsignificant probability that the first year of the RTC we realize we've made a number of grievous mistakes. I.e., it would surprise me if everything went without a hitch the first time. Personally, this only worries me if we don't learn enough to be able to pull it off the next year, which I happen to consider rather unlikely. At any point, it might be useful to categorize the first year as a trial run.

If that risk is unacceptable, we could partner with someone like IDInsight, MIT's JPAL, etc. The problem is that those organizations specialize in development interventions. It wouldn't hurt to ask, though. 


## Next steps.

## Footnotes:
[1] of which I was an alumni and then JC. https://espr-camp.org/  
[2] To operationalize tentative: add a factor of 2:3 to your previous odds on CFAR workshops  
[3] I don't want to engage with this in this article, but on the other hand I didn't want to remove criticism.  
[4] I am very confused about this. I know that his role at EuroSparc (ESPR 1.0) was as an ops person.  
[5]  Obtained from MIT's course *Evaluating Social Programs* (Week 3), accessible at https://courses.edx.org/courses/course-v1:MITx+JPAL101x+2T2018/course/.  

