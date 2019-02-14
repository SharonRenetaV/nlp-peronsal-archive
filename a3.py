from sklearn.metrics import jaccard_similarity_score
x=[2,1,1,9]
y=[0,2,1,0]
print(jaccard_similarity_score(x,y))
print(jaccard_similarity_score(x,y, normalize=false))