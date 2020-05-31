import numpy as np

questionArr = np.array([[2,1,-1,-1],[1,3,2,13],[1,-2,4,11]])

# Step One
coefR2 = ( questionArr[1][0] / questionArr[0][0] )
questionArr[1] = np.subtract(questionArr[1], np.multiply(questionArr[0],coefR2))
print(questionArr)
print('\n')

# Step Two
coefR31 = ( questionArr[2][0] / questionArr[0][0] )
coefR32 = ( questionArr[2][1] / questionArr[1][1] )

questionArr[2] = np.subtract(questionArr[2], np.multiply(questionArr[0],coefR31))
questionArr[2] = np.subtract(questionArr[2], np.multiply(questionArr[1],coefR32))

# Step Three
z = 






print(questionArr)
