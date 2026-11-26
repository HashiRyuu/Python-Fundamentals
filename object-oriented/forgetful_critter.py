from critter import Critter

##
#  A ForgetfulCritter can't remember it's history.
#
class ForgetfulCritter(Critter) :
    def __init__(self):
        super().__init__()

    def addHistory(self):
        super().addHistory("?")
            
def main() :
   dopey = ForgetfulCritter()
   dopey.addHistory("eat");
   print(dopey.getHistory())
   print("Expected: [?]")
   dopey.move(10)
   print(dopey.getHistory())
   print("Expected: [?, ?]")

main()
