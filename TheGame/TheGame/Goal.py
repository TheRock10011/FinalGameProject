class Goal:
    pass
    def checkGoalCollission(self, playerX, playerY, goalX, goalY):
        distanceAmount = 20
       
        if playerX >= goalX -distanceAmount and playerX <= goalX + distanceAmount and playerY >= goalY -distanceAmount and playerY  <= goalY + distanceAmount:
            #print("Loads Next Level")
            return True
        return False
        #return True