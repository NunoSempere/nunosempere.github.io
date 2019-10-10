## Code in R, for the Addendum of [Shapley Values: Better than Counterfactuals](https://forum.effectivealtruism.org/posts/XHZJ9i7QBtAJZ6byW/shapley-values-better-than-counterfactuals)

```
AMV <-function(foundations, roomforfoundingfoundations, roomforfoundingOP, projects, numprojects){

  avm = ValueOfFunded((foundations*roomforfoundingfoundations + roomforfoundingOP), projects, numprojects) - ValueOfFunded(foundations*roomforfoundingfoundations, projects, numprojects)
  # Note that the code could easily be optimized by computing both calls to ValueOfFunded at the same time. However, this loses clarity.
  
  return(avm)
  
}

ValueOfFunded <-function(room, projects, numprojects){
  value = 0
  for(k in c(1:numprojects)){
    #print(c("k=",k))
    value = value + ProbabilityThatKwillBeAmongTheRSmallestNumbers(k,room,projects, numprojects)*Impact(k)
  }
  #print(c("value=", value))
  return(value)
  
}

ProbabilityThatKwillBeAmongTheRSmallestNumbers <-function(k,r,q,n){
  #print(c("k=",k,"r=", r,"q=",q,"n=",n))
  ## Probability that K is the i-th smallest number =
  ## = choose(k-1,i-1)*choose(n-1,p-i-1)/choose(n,p)
  p=0
  for(i in c(0:r)){
    # we notice that all of the terms contain the factor choose(n,p), so we can leave it at the end.
    p=p+(choose(k-1,i-1)*choose(n-k,q-i))
  }
  p = p/ choose(n,q)
  return(p)
}


ComputeShapleyValue <-function(numfoundations, roomforfoundingfoundations, roomforfoundingOP, numprojects){
  ShapleyValue = 0
  for(Foundations in c(0:numfoundations)){
    for(Projects in c(0:numprojects)){
      print(paste("We're at: (",Foundations,"/", Projects, ") of (", numfoundations,",", numprojects, ")" , sep=""))
      ShapleyValue = ShapleyValue+choose(numfoundations,Foundations)*choose(numprojects,Projects)*AMV(Foundations, roomforfoundingfoundations, roomforfoundingOP, Projects, numprojects)/choose(numprojects+numfoundations, Foundations+Projects)
    }
  }
  return(ShapleyValue/(numfoundations+numprojects+1))
}

ComputeShapleyValue(1, 1, 1, 3)
ComputeShapleyValue(1, 1, 2, 3)

ComputeShapleyValue(numfoundations=1, roomforfoundingfoundations=1, roomforfoundingOP=1, numprojects=3)

Impact <- function(k){
  #return(0.99^k)
  return(2/(k^2))
}

## IT WORKS!!!!

start <- Sys.time()
ComputeShapleyValue(numfoundations=10, roomforfoundingfoundations=10, roomforfoundingOP=10, numprojects=500)
end <- Sys.time()
end-start
sum(0.99^c(1:500))

start <- Sys.time()
ComputeShapleyValue(numfoundations=10, roomforfoundingfoundations=20, roomforfoundingOP=250, numprojects=500)
end <- Sys.time()
end-start
sum(0.99^c(1:500))

# With a different impact measure.
start <- Sys.time()
ComputeShapleyValue(numfoundations=10, roomforfoundingfoundations=20, roomforfoundingOP=250, numprojects=500)
end <- Sys.time()
end-start
sum(2/(c(1:1000))^2)```

```
