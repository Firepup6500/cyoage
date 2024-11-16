from fkeycapture import getchars as gco
from fkeycapture import get as g
p, e = print, exit
def i(s):
  print(s,end="",flush=True)
def gc(ch):
  sel = gco(chars=ch).upper()
  print(sel)
  return sel
p("Start your adventure!\nPick a path:\nThe left path\nThe right path")
i("Left (L) or right (R)? ")
LR = gc(["L","l","R","r"])
if LR == "L":
  print("Walking down this path, you come across a house. Do you\nEnter the house\nWalk into the woods")
  i("House (H) or Woods (W)? ")
  house = gc(["H","h","W","w"])
  if house == "H":
    p("""Well. Who knew there was a witch in there?

Game Over!
Ending 1/16""")
    e(1)
  elif house == "W":
    p("You decide not to trust the house made of candy, and walk into the woods...")
    i("Continue ")
    g()
    p("\nIt's getting late... Do you:\nPush on\nGo to sleep")
    i("Push on (P) or Sleep (S)? ")
    woods = gc(["P","p","S","s"])
    if woods == "P":
      p("""You eventually reach the house again, even though you were walking in a straight line. The witch throws a potion at you...

Game Over!
Ending 2/16""")
      e(2)
    elif woods == "S":
      p("""Good night...

???? ?????
Ending 3/16""")
      e(3)
elif LR == "R":
  p("You choose the right path.\nDo you:\nWalk on the left side of the path\nWalk on the right side of the path")
  i("Left (L) or right (R)? ")
  side = gc(["L","l","R","r"])
  if side == "L":
    p("""You walk into the void.

Game Over!
Ending 4/16""")
    e(4)
  elif side == "R":
    p("You see a Void on the left side of the path, good thing you didn't go that way!")
    i("Continue ")
    g()
    p("\nYou reach a large castle. Do you:\nAsk nicely to be let in\nDemand to see their leader")
    i("Ask (A) or Demand (D)? ")
    castle = gc(["A","a","D","d"])
    if castle == "A":
      p("""The soldiers laugh at you. Then they flip a switch which flings you into the moat of lava!

Game Over!
Ending 5/16""")
      e(5)
    elif castle == "D":
      p("The Aliens are surprised, but they let you in their castle.")
      i("Continue")
      g()
      p("\nYou have reached the Aliens' leader. Do you:\nLeave\nTalk to their leader\nThird option go brr")
      i("Leave (L), Talk (T) or Third (3)? ")
      leader = gc(["L","l","T","t","3"])
      if leader == "L":
        p("""You can't leave this place!

Game Over!
Ending 6/16""")
        e(6)
      elif leader == "T":
        p("""The cow moos at you. Apparently the Aliens think that means to put you in the moat, which they promptly do.

Game Over!
Ending 7/16""")
        e(7)
      elif leader == "3":
        p("You break the fourth wall, dragging the narrator into the game with you.")
        i("Excuse me? ")
        g()
        p("\nWhy would you pull me in here?\nI'm sick of this\nI wanted to see what would happen")
        i("Sick (S) or Curious (C)? ")
        nar = gc(["S","s","C","c"])
        if nar == "S":
          p("""Well. Have an ending then.

Ending 8/16""")
          e(8)
        elif nar == "C":
          p("Hmm. I suppose I can let that one go then.")
          i("Continue ")
          g()
          p("\nI give you a rare and magical item. Use it wisely.")
          i("Oh right, the Aliens.")
          g()
          p("\nI leave you to the aliens. What do you do?\nSmack their leader with the rare and magical item\nTelepop to a different dimension")
          i("Smack (S) or Telepop (T)? ")
          rare = gc(["S","s","T","t"])
          if rare == "S":
            p("""Nothing happens. The Aliens throw you into space.

Game Over!
Ending 9/16""")
            e(9)
          elif rare == "T":
            p("Are you tobby?\nYes\nNo, but I need to get out of here!")
            i("Yes (Y) or No (N)? ")
            tobby = gc(["Y","y","N","n"])
            if tobby == "Y":
              p("""Liar. You Telepop to the lava dimension. You die.

Game Over!
Ending 10/16""")
              e(10)
            elif tobby == "N":
              p("Fine. Just this once. You telepop to a dimension where you are the Aliens' leader. Do you:\nGo to space\nGet a cow\nGet the narrator\nGet a time machine\nDance off???")
              i("Space (S), Cow (C), Narrator (N), Time machine (T) or DANCE OFF (D)? ")
              big = gc(["S","s","C","c","N","n","T","t","D","d"])
              if big == "S":
                p("""You suffocate.

Game Over!
Ending 11/16""")
                e(11)
              elif big == "C":
                p("""You make a cow the Aliens' leader. You leave. The cow moos.

Game Over!
Ending 12/16""")
                e(12)
              elif big == "N":
                p("""I said only that once. The universe collapses.

Game Over!
Ending 13/16""")
                e(13)
              elif big == "T":
                p("Where do you go?\nThe Past\nThe Future")
                i("Past (P) or Future (F)? ")
                time = gc(["P","p","F","f"])
                if time == "P":
                  p("""There is nothing.

Game Over!
Ending 14/16""")
                  e(14)
                elif time == "F":
                  p("""You emerge to find the universe is ruled by aliens. They see you come out of the machine and worship you.

You Win!
Ending 15/16""")
                  e(15)
              elif big == "D":
                p("""No. You are crushed by a tank.

Game Over!
Ending 16/16""")
                e(16)

e("You tried to break the game. Too bad.")