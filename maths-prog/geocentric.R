install.packages("ggplot2")
library(ggplot2)

circle = function(t){
  x = sin(t)
  y = cos(t)
  return(c(x,y))
}

d = list()
d$x = c()
d$y = c()
for(t in c(1:2000)){
  p_circle = circle(t)
  d$x=c(d$x,p_circle[1])
  d$y=c(d$y, p_circle[2])
}
d= as.data.frame(d)

blank = theme_void() + theme(legend.position="none")
ggplot(data = d)+
  geom_point(aes(x=x, y=y), size = 0.0001)+
  blank

p <- ggplot(data = data.frame(x = 0), mapping = aes(x = x))

p + stat_function(fun = sun) + xlim(-5,5)

ggsave("temp.png", width = 30, height = 30, units = "cm")

