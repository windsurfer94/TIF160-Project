# This function enables system to check for initial conditions.

def InitialChecker(FilledPlacesCV, EmptyPlacesCV, TotalPiece, TotalEmpty):

    if (FilledPlacesCV != TotalPlace)  :
    
        print('The number pieces and the pieces recognized by a camera do not match. Please check the conditions')
        IsOk = 0

    elif (EmptyPlacesCV != TotalEmpty) :

        print('The number empty places and the empty places recognized by a camera do not match. Please check the conditions')
        IsOk = 0

    else:

        isOk = 1

    return(IsOk)
