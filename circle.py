
r =int(input("Enter radius of circle:"))
 
rpoints = []
lpoints = []
    
for i in range (-r,r+1):
    for j in range (-r,r+1):
        if i**2 + j**2 == r**2:
            if i<0: 
                lpoints.append([i,j])
            else:
                rpoints.append([i,j])

print(lpoints)
print("\n\n\n\n\n\n\n\n")
print(rpoints)
