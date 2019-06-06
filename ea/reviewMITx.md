# A review of two free online development policy courses

Sanford L. Segal's *Mathematicians under the Nazis* has been one of the foundational books in my intellectual development. It, together with an anthopology course I took, made me grokk that, when deciding how to make the world better, many cultures/individuals have thought that they had a unique advantage (and were wrong). Some of these people were not only better mathematicians, but also brighter than myself, and also they were Nazis. And so we fall into moral uncertainty, and moral relativism.

But from off in the distance, there comes the simple idea of making the world better by making the world's poor better off. It seemed to me that this idea wasn't dependent on many cultural assumptions. Meanwhile, MIT's Poverty Action Lab happens to have made their courses freely available. I took *Microeconomics*, *Evaluating Social Programs*, *The Challenges of Global Poverty* and *Foundations of Development Policy*, and they proved to be excellent. 

Here I review the last two, as they're fresh in my mind. They both scavenge from the book *Poor Economics*. Because they have significant overlap, I would recommend just the second, *Foundations of Development Policy*, which covers the material in more depth.

## General structure

The general structure of each unit of both courses is:
- A question is presented
- Different options, which all *a priori* sound plausible, are discussed. 
- An experiment or a series of experiments is presented which answers the question in a manner more decisive than speculation could.

I think that constant repetition of this structure pushes the point that you really can't trust the arguments, but instead have to go and do the experiment. This is one of the important intuition which the course helps grokk.

When the professors deviate from that general structure, they become less convincing. In particular, they seem to really not like macro-economy / geopolitics. For example, [they help increase Pakistan's tax revenue](https://www.povertyactionlab.org/evaluation/incentivizing-property-tax-inspectors-through-performance-based-postings-pakistan), and it is not at all clear to me whether that that is at all positive, and might be a blunder.

## An example unit: Nutrition and Productivity.

The question presented is whether there is a nutrition based poverty trap. A mathematical formalism for a poverty trap is presented, in which wealth at time t+1 depends on wealth at time t. A poverty trap appears if falling below a wealth threshold leads to a further sliding down, that is, if the relationship between wealth at time t and t+1 looks like:

![](Image 1)

as opposed to like

![](Image 2)

And this formalism is then applied to the case of nutrition:
- On day n, you have wealth W(n)
- On day n, you consume an amount of food F(n) = f(W(n))
- On day n+1, your production depends on how well you've been fed the day before, that is W(n+1) = g(F(n)) = g(f(W(n)) = h(W(n)) , so ultimately, wealth on day n+1 depends on wealth on day n.

The question is whether, in practice, a poverty trap mediated by nutrition arises. A mathematical condition necessary and sufficient for a poverty trap to arise is not just stated, but successful efforts are made so that students without a mathematical background can understand why that is.

Then, some data is presented, which solves the problem. First, some cross-sectional data, that is, getting data from the population in general, without conducting a trial. But this is insuficient. Then, they present data from a GiveDirectly randomized trial, and give some details as to the implementation. They get some numbers for how calories and food expenditure vary with wealth. Then, they look at another randomized trial which looks at the impact of calories on productivity. Putting both things together, they conclude that a poverty trap as mediated by nutrition is unlikely. 

However, child nutrition could cause such a poverty trap, because nutrition deficiencies when a child could affect productivity throughout life. They look at the impact of deworming (because if worms don't eat your food, you do) and see that it does have a significant impact on wages.

To complement the lectures, a bibliography is provided:
- *Poor Economics*: Chapter 2.
- "Household Response to Income Changes: Evidence from an Unconditional Cash Transfer Program in Kenya" (Haushofer and Shapiro, 2013). "Giffen behavior and subsistence consumption" (Jensen and Miller, 2008).
- "Causal effect of health on labor market outcomes: Experimental evidence" (Thomas et al., 2006).
- "Worms at work: Long-run impacts of child health gains" (Baird, Hicks, Kremer, and Miguel, 2012). 
- "Are there nutrient-based poverty traps? Evidence on iron deficiency and schooling attainment in Peru" (Chong et al., 2014).
- Video: "The Name of the Disease"
- Optional: "Wealth, Health, and Health Services in Rural Rajasthan" (Banerjee, Deaton and Duflo, 2004). Working paper available for download here.
- Optional: *Poor Economics*: Chapter 3.

The readings comprise ~300 pages; the size of a small book (every week). In other words, the student has the possibility of digging pretty deep, which I generally did. It was a significant time investment.

As homework, some data from the Kremer’s deworming project in Kenya (see the readings) is provided, and one plays around with it in R and does some analysis, which gets more complicated as the course progresses. Then, some questions about an unrelated 45 page report on malaria nets. 

## R

Throughout the courses, I picked up R. I then read parts of the book [R for Data Science](https://r4ds.had.co.nz/), which is available for free online, and used it for [some self-experimentation in calibration](https://nunosempere.github.io/rat/Self-experimentation-calibration.html), for a data science hackathon, and [to analyze the results of an EA mental health survey](https://nunosempere.github.io/rat/eamentalhealth/analysis/writeup), as well as for some other private projects. The courses definitely helped, but I think that it was more a function of a personal interest + previous experience with programming. That is, I don't think that mastery of R would come automatically.

## Quality of the teachers & of the pedagogy
I feel that the quality of the teachers is incomparably better than that of the teachers to which I have access at the University of Vienna or at the Universidad Autónoma de Madrid. Perhaps they closely approach the ideal of a [zetetic explanation](https://www.lesswrong.com/posts/i2Dnu9n7T3ZCcQPxm/zetetic-explanation). Perhaps they just have a *depth* to them. If a student asks a miscellaneous question, they can answer it, and they take the time to do it.

The teachers seem to have a carefully-considered cognitive model of the student, as opposed to every other university teacher I have had, ever (see: [Why books don't work:  Why lectures don't work](https://andymatuschak.org/books/)). They're good pedagogs. They ask the student questions, and keep the lectures engaging. Implicitly, all the students in the recorded classroom have read all the recommended texts beforehand, so the interaction is meaningful.

I remember just being introduced to Fourier transforms and just having been given the mathematical formalism, without the history, without the examples, without the motivation; that is not the case here. Here, some of the RCTs which are discussed have been carried out by the professors themselves, and this is not a function of their vanity, but of the relevance of these RCTs.

## Value of the certification

I'm uncertain of the signalling value of the certification. See: [this article](https://www.huffpost.com/highline/article/capitalist-takeover-college).
