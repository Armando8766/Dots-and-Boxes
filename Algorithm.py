
class Algo: # A class for defining algorithms used (minimax and alpha-beta pruning)
    
    def miniMax(State, Ply_num): # Function for the minimax algorithm

        for i in range(State.Current.dimY):
            for j in range(State.Current.dimX):
                if State.Current.Mat[i][j] == ' ' and (j, i) not in State.children:
                    State.Make(j, i, True)
                    if Ply_num < 2:
                        return (i, j)

        Minimum_Score = 1000
        i = 0
        j = 0
        for k, z in State.children.items():
            Result = Algo.Maximum(z, Ply_num - 1, Minimum_Score)
            if Minimum_Score > Result:
                Minimum_Score = Result
                i = k[0]
                j = k[1]

        return (i, j)


    def Maximum(State, Ply_num, Alpha): # Alpha-beta pruning function for taking care of Alpha values
        if Ply_num == 0:
            return State.CurrentScore

        for i in range(State.Current.dimY):
            for j in range(State.Current.dimX):
                if State.Current.Mat[i][j] == ' ' and (j, i) not in State.children:
                    State.Make(j, i, False)

        Maximum_Score = -1000
        i = 0
        j = 0
        for k, z in State.children.items():
            Result = Algo.Minimum(z, Ply_num - 1, Maximum_Score)
            if Maximum_Score < Result:
                Maximum_Score = Result
            if Result > Alpha:
                return Result

        return Maximum_Score


    def Minimum(State, Ply_num, Beta): # Alpha-beta pruning function for taking care of Beta values
        if Ply_num == 0:
            return State.CurrentScore

        for i in range(State.Current.dimY):
            for j in range(State.Current.dimX):
                if State.Current.Mat[i][j] == ' ' and (j, i) not in State.children:
                    State.Make(j, i, True)

        Minimum_Score = 1000
        i = 0
        j = 0
        for k, z in State.children.items():
            Result = Algo.Maximum(z, Ply_num - 1, Minimum_Score)
            if Minimum_Score > Result:
                Minimum_Score = Result
            if Result < Beta:
                return Result

        return Minimum_Score
