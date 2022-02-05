#lex_auth_0127426391777280001519

class Player:
    def __init__(self,name,experience):
        self.__name=name
        self.__experience=experience

    def get_name(self):
        return self.__name

    def get_experience(self):
        return self.__experience

    def __str__(self):
        return(self.__name+" "+(str)(self.__experience))

#Implement Game class here
class Game:
  def __init__(self, players_list):
    self.players_list = players_list

  def sort_players_based_on_experience(self):
    for i in range(len(self.players_list)):
      for j in range(i+1, len(self.players_list)):
        if self.players_list[i].get_experience() < self.players_list[j].get_experience():
          temp = self.players_list[i]
          self.players_list[i] = self.players_list[j]
          self.players_list[j] = temp
      #print(self.players_list[i].__str__())

  def shif_player_to_new_position(self, old_index_position, new_index_position):
    self.sort_players_based_on_experience()
    temp = self.players_list[new_index_position]
    self.players_list[new_index_position] = self.players_list[old_index_position]
    self.players_list[old_index_position] = temp

    # for i in range(len(self.players_list)):
    #   print(self.players_list[i].__str__())
    
  def display_player_details(self):
    for i in range(len(self.players_list)):
      print(self.players_list[i].__str__())



player1=Player("Dhoni",15)
player2=Player("Virat",10)
player3=Player("Rohit",12)
player4=Player("Raina",11)
player5=Player("Jadeja",13)
player6=Player("Ishant",9)
player7=Player("Shikhar",8)
player8=Player("Axar",7.5)
player9=Player("Ashwin",6)
player10=Player("Stuart",7)
player11=Player("Bhuvneshwar",5)
#Add different values to the list and test the program
players_list=[player1,player2,player3,player4,player5,player6,player7,player8,player9,player10,player11]
#Create object of Game class, invoke the methods and test your program
