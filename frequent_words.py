from collections import Counter

text = "Comcast Corporationis an American global telecommunications conglomerate that is the largest broadcasting and cable television company in the world by revenue.It is the second-largest pay-TV company after AT&T, largest cable TV company and largest home Internet service provider in the United States, and the nation's third-largest home telephone service provider. Comcast services U.S. residential and commercial customers in 40 states and in the District of Columbia.The company's headquarters are located in Philadelphia, Pennsylvania. As the owner of the international media company NBCUniversal since 2011, Comcast is a producer of feature films and television programs intended for theatrical exhibition and over-the-air and cable television broadcast."

words=text.split()


counter = Counter(words)
top_three = counter.most_common(5)

print(top_three)