p1= input("Enter boy name ").lower()
p2= input('Enter Girl name').lower()
p1_array=list(p1)
p2_array=list(p2)
for i in p1:
 if i in p2:
   p1_array.remove(i)
   p2_array.remove(i)
count=len(p1_array)+len(p2_array)
flames=['F','L','A','M','E','S']
while len(flames)>1:
 split = (count % len(flames)-1 )
 if (split>=0):
   right = flames[split + 1 :]
   left = flames[:split]
   flames = right +left
 else:
   flames = flames[:len(flames)-1]
 
print(flames)
