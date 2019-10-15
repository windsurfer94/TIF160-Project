from blockshaped import blockshaped


import numpy as np
# This function coverts the image to an array form. Canny method is used here to identify the edges
def Image2Array(matrix,threshold):

    AugmentedMatrix = blockshaped(matrix, 50,50) #Decomposes image array into (64,50,50) for 400*400* image
    size = AugmentedMatrix.shape # Error handler
    counter = 0

    AverageMatrix = np.empty((8,8)) #Create empty matrix to get the Chessboard layout (before filter-with decimal)
    MainMatrix = np.empty((8,8)) #Create empty matrix to get the Chessboard layout (after filter-with ones and zeros)

    for i in range(7,-1,-1):
        for j in range(7,-1,-1):
            AverageMatrix[i,j] = np.mean(AugmentedMatrix[counter]/np.max(AugmentedMatrix))
            counter += 1

    for i in range(7,-1,-1):
        for j in range(7,-1,-1):
            if AverageMatrix[i,j] <threshold:
                MainMatrix[i,j] =0 #indicates empty square
            else:
                MainMatrix[i,j] =1 #indicates square with piece

    return MainMatrix,AverageMatrix