run1=int(input("Runs scored by Player 1 in 60 balls: "))
run2=int(input("Runs scored by Player 2 in 60 balls: "))
run3=int(input("Runs scored by Player 3 in 60 balls: "))
strike_rate1=(run1/60)*100
strike_rate2=(run2/60)*100
strike_rate3=(run3/60)*100
print("Strike rate of Player1:",strike_rate1)
print("Strike rate of Player1:",strike_rate2)
print("Strike rate of Player1:",strike_rate3)
print("Run for next 60 balls for Player1:",run1*2)
print("Run for next 60 balls for Player2:",run2*2)
print("Run for next 60 balls for Player3:",run3*2)
print("Maximum no of sixes of Player1",run1//6)
print("Maximum no of sixes of Player2",run2//6)
print("Maximum no of sixes of Player3",run3//6)
