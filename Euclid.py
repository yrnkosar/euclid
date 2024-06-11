import math
points = [(1, 2), (4, 6), (5, 1), (7, 3), (2, 8)]

def euclideanDist(pnt1,pnt2):
  return math.sqrt((pnt2[0]-pnt1[0])**2+(pnt2[1]-pnt1[1])**2)

distances=[]

for i in range (len(points)):
    for j in range (i+1,len (points)):
        distance =euclideanDist(points[i],points[j])
        distances.append(distance)

mindist=min(distances)

print(f"minimum öklid mesafesi: {mindist}")