import random
def game():
  print("you are palying the game ..")
  score=random.randint(1,64)
   #fetch the his score
  with open("hiscore.txt") as f:
    hiscore=f.read()
    if(hiscore!=""):
      hiscore= int(hiscore)
    else:
      hiscore=0
  print(f"your score : {score}")
  if(score>hiscore):
    with open("hiscore.txt","w") as f:
      f.write(str(score))

  return score    
game()