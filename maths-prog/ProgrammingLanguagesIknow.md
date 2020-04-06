# Programming Languages I Know and Cherish

tl;dr: I have some experience with programming languages, and learning the syntax of a new one to a decent level takes me about a week.

# Turing complete:

## Turing machines

Representative project: [A Turing Machine that finds out the nth prime](https://github.com/NunoSempere/Turing_Machine)

Useful for: Elegant & nifty arguments in set theory. The programming language for the mathematician.

Personal experience: Cognitively effortful, interesting to work with. I've programmed a TM that finds the n-th prime. Turing Machines are necessary to understand some arguments in Paul Cohen's *Set theory and the continuum hypothesis*. More recently, [here](https://www.scottaaronson.com/blog/?p=2725) is a Turing Machine which halts iff ZFC is inconsistent.

## C and C++

Representative project: [Calibration](https://github.com/NunoSempere/calibration)

Useful for: Pedal to the metal programming.

Personal experience: One of the first programming languages I learnt, and thus my documentation was in Spanish. I've used it to crunch numbers when a speedup mattered. I've also abused it to program a database application, to analyze a lexical corpus, to solve riddles. This has led me to appreciate higher level languages more, and to understand them better. For example:

In JavaScript, consider the function:

```
function reverseArrayInPlace(array) {
  for (let i = 0; i < Math.floor(array.length / 2); i++) {
    let old = array[i];
    array[i] = array[array.length - 1 - i];
    array[array.length - 1 - i] = old;
  }
  return array;  
}
```

This function reverses an array, and changes it. However, the scope of the array which the function manipulates is local, and yet the original array is changed. This is because, although JavaScript doesn't work with pointers, it is working with pointers, and the local copy of the pointer is pointing to the same place.

Having had to deal with memory allocation, working in a language which just deals with it is orgasmic.

## Python.

Representative project: [Some machine learning](https://nunosempere.github.io/maths-prog/MachineLearningDemystified/). 

Useful for: Mostly everything.

Personal experience: I learnt Python while young, and used it to program Arduino. More recently, I've used it for some machine learning.

## R

Representative project: [EA Mental Health](https://forum.effectivealtruism.org/posts/FheKNFgPqEsN8Nxuv/ea-mental-health-survey-results-and-analysis)

Useful for: Statistical analysis; writting programs quickly. Beautiful plots.

Personal experience: I view this language with a lot of affection, and I like it a lot; I have found analyzing datasets to be very cognitively stimulating. The ggplot2 library is amazing. The time required to create a new program is basically 0, in RStudio, because you don't really compile the whole program at once, but instruction by instruction / line by line. Would recommend. Ultimately, when working with huge datasets, what one does is to load a library which has functions written in C.

## Haskell
Representative project: [Newspaper scrapper](https://github.com/NunoSempere/NewspaperScraper)

Useful for: Aesthetics.

Personal experience: Learnt for the novelty, and I appreciate the aesthetic appeal. I then programmed a newpaper scrapper, which is I found hillarious because of the bad fit between the task and the language.

## PHP 

Representative project: [shapleyvalue.com](http://shapleyvalue.com); [accompanying post](https://forum.effectivealtruism.org/posts/XHZJ9i7QBtAJZ6byW/shapley-values-better-than-counterfactuals)

Useful for: Server side programming.

Personal experience: I learnt PHP to program the above webpage. Ultimately, however, I could have just used JavaScript, because I don't really needed a database / everything could have been computed on the user's side. Demistifyies some webpages. 

## JavaScript
Representative project: This [utility](https://observablehq.com/@nunosempere/foretold-notebook-into-csv), which takes a [foretold](https://www.foretold.io/) notebook, queries some data and converts it into a csv.

Useful for: Code which is executed on the client's side. Interactive webpages. Server side with Node.js

Personal experience: When I first wrote this, reading Chapter 5 of *Eloquent JavaScript*,  [Higher order functions](https://en.wikipedia.org/wiki/Higher-order_function) had just clicked for me. In hindsight, I had already used ```lapply``` in R, and functions which modify other functions are pretty natural in Haskell, but I had the Eureka moment. Later, I used JavaScript to implement approval voting for the Center for Eletion Science, and for some contributions to foretold.io, a forecasting platform. I later built a small app to help me write poetry in Spanish using node and electron, as well as a glorified diary program.

## Various others:

- OCaml & ReasonML & React: Foretold uses ReasonML / React and I invested some time into understanding it.
- Ruby: [Sparkwave](https://www.sparkwave.tech/) mentioned that they used them, so I checked it out. I really like that the amount of boilerplate needed to open a file is minimal compared to doing the same thing in node.
- Lisp: I read the [Paul Graham summary](http://www.paulgraham.com/rootsoflisp.html), got the aha! moment about Lisp being an interesting model of computation, fucked around with it for a bit, and then never used it for a practical project. 

Unix shell, Matlab (a less worthy R). Honorable mention to JSFuck for its practical uses. Honorable mention to Intercal for the following paragraph, which has stayed with me: 

> Until the new INTERCAL compiler with better RYM[6] access comes out, the old compiler has no way of knowing which language you are familiar with and thus it doesn't know what language to produce its output in[7]. INTERCAL elegantly solves this problem by producing its output in Roman numerals, under the assumption that when Rome was at the height of its strength, half the world was under its dominion, so the comprehension of Roman numerals is part of our racial memory.
> [Source](http://www.catb.org/~esr/intercal/paper.html)


# Not Turing complete

Update: It has since been pointed out to me that Latex, HTML and MySQL might be Turing complete. This is not the first time that I've encountered an unexpected Turing; the game *Magic The Gathering* also turns out to belong to this category. I feel that this fact contains a deep lesson about the structure of the world, though it escapes me at the moment. 

## Latex
Representative project: My CV.

Useful for: Typesetting; producing beautiful pdfs.

Personal experience: There when I've needed it. 

## Markdown
Representative project: This document is written in markdown.

Useful for: GithubPages. Just writting without the need to worry about html.

Personal experience: Easy to pick up. With pandoc I can compile it into latex (!) and add all the math I want.

## HTML and CSS
Representative project: [easyfirma.es](easyfirma.es)

Useful for: Webpages!

Personal experience: Templates are not evil; they're the difference between [shapleyvalue.com](shapleyvalue.com) and [easyfirma.es](easyfirma.es). Easy to pick up. Also easy to clutter.

##  MySQL / MariaDB
Representative project: None as of yet. 

Useful for: Databases on the server's side.

Personal experience: Pretty straightforward; it's not even Turing complete. I prefer MariaDB on principle, because it's Free (Libre!) Software.


## GraphQL
Foretold.io uses GraphQL in the background, so I learnt to use it at a jack-of-all trades level.
