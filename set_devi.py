
# coding: utf-8

# In[14]:


A=set([1,2,3,4,5])
B=set([4,5,6,7,8])


print(A.union(B))
print(A.intersection(B))
print(A.difference(B))
print(A.symmetric_difference(B))



# In[16]:


C=set([1,2,3,4,5])
D=set([4,5,6,7,8])
print(A|B)
print(A&B)
print(A-B)
print(A^B)

