# 100 predictions

Para la versión en español, ve a [aquí](nunosempere.github.io/rat/100-predicciones)

## Day 1
{SHA is an acronym for "Secure Hashing Algorithm"; a hash algorithm recieves a string, or more generally a document, an returns a number.
Thus, a hash can identify a document, such that the hash can be revealed without revealing the document. 
If the document is published afterwards, people know it hasn't been changed (because the hash would also change)

In 2017, a project by CWI Amsterdam and Google produced 2 different legible pdfs which had the same SHA1 hash.
This makes SHA1 insecure; it is no longer enough to uniquely identify a document.

The hash family continued with SHA2, and then SHA3. The most secure version of SHA3 is SHA-512.

Questions
- What probability, per year, do you assign to SHA-512 being successfully attacked?  
By successfully attacked, we understand that someone finds x, x' such that SHA3-512(x) = SHA3-512(x'), or that given a
y = SHA3-512(z) someone finds a z' =/= z such that SHA3-512(z')=y.
- WHat probability, per year, do you assign to SHA3-512 being replaced as a standard?}

Recommended time: 15 mins.

## Day 2
{Elisabeth II, Queen of England, was born on 1926, whereas King Juan Carlos I of Spain was born on 1938. 

Question:
- What probability do you assign to ELisabeth the II dying before Juan Carlos the I?
}

## Day 2 Discussion
In our group, probablities ranged from 4% (my own estimate) to 25%. I obtained my 6% figure going to (life tables)[https://www.ons.gov.uk/peoplepopulationandcommunity/birthsdeathsandmarriages/lifeexpectancies/datasets/nationallifetablesunitedkingdomreferencetables], and searching for life expectancies at 80 and 92 years old. I created a simplified model in which the queen of england was just an English peasant, ditto for the king of Spain.
With those tables in mind, it's relatively easy to calculate the probability that the queen will still ve alive in X years, and that the king will die in exactly X years. Multiplying both to get the probability of both events happening, and summing over all possible years, I arrive at a probability of 5,5575% for the statement under discussion. I adjust this upwards a little bit to 6%, because the queen seems healthier, the king broke his hip, and I'd guess the English Health system has better top notch doctors. If I really cared about the result, I might consider the rate of death not per year, but per week/month (interpolating those from the values at the beginning and end of each year), and would take into account rising life expectancies.

## Day 3
{The Effective Altruism Group in Spain wanted to give a TedX talk. What probability do you assign to one being given by the end of 2019? Pro tip: Consider the question in the negative:  What probability do you assign to one NOT being given by the end of 2019?}

## Hashes
Everything between {} is hashed through SHA3-512 (https://www.browserling.com/tools/sha3-hash), and published on Twitter (@NunoSempere).
This, of course means that corrections or notes can't be made.

### Day 1
0addb6466a2fb3a537fa276e39306f2b57f8d31e66b826f57b62d141ff3de821fca5b9e35de06092c3847bc018b1531ecc3123e09b0f137700c2433b58f8781f
Notes: SHA-3 is replaced is interpreted as "SHA-4" is accepted as a standard.

### Day 2
3bb19d34fbb08347389f9d38cd5660235a5114df3890a052926d36988529b52fc3f72e27b00af88b1390b32591f54093d951abc7cbec94efb42f145d705786e0

### Day 3
