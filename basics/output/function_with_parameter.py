#Escape_by("jumping over")
#Escape_by("running around")
#Escape_by("going deeper")

#we cannot escape that way! The boulder is too big!
#we cannot escape that way!The boulder is moving fast!
#That might just work! Let's go deeper!

#This is function with single plan and the name if 'plan'

def escape_by(plan):
  if (plan=="jumping over"):
   print("We cannot escape that way, the boulder is too big!")
  elif(plan=="running around"):
    print("We cannot escape that way, The boulder is moving too fast!")
  elif(plan=="going deeper"):
     print("That might be a good idea, let's do it.")
  else:
   print("Not sure about the plan")

#call the function

escape_by("jumping over")
escape_by("running around")
escape_by("going deeper")
escape_by("let's listen")