players = [
    {
        "name": "Kevin Durant", 
        "age":34, 
        "position": "small forward", 
        "team": "Brooklyn Nets"
    },
    {
        "name": "Jason Tatum", 
        "age":24, 
        "position": "small forward", 
        "team": "Boston Celtics"
    },
    {
        "name": "Kyrie Irving", 
        "age":32, "position": "Point Guard", 
        "team": "Brooklyn Nets"
    },
    {
        "name": "Damian Lillard", 
        "age":33, "position": "Point Guard", 
        "team": "Portland Trailblazers"
    },
    {
        "name": "Joel Embiid", 
        "age":32, "position": "Power Foward", 
        "team": "Philidelphia 76ers"
    },
    {
        "name": "", 
        "age":16, 
        "position": "P", 
        "team": "en"
    }
]

class Player:
    def __init__(self,some_dic):
        self.name = some_dic["name"]
        self.age = some_dic["age"]
        self.position = some_dic["position"]
        self.team = some_dic["team"]

    @classmethod
    def get_team(cls,team_list):
        new_team = []
        for one_dictionary in team_list:
            this_player = Player(one_dictionary)
            new_team.append(this_player)
        return new_team


kevin = {
    "name": "Kevin Durant", 
    "age":34, 
    "position": "small forward", 
    "team": "Brooklyn Nets"
}
jason = {
    "name": "Jason Tatum", 
    "age":24, 
    "position": "small forward", 
    "team": "Boston Celtics"
}
kyrie = {
    "name": "Kyrie Irving", 
    "age":32, "position": "Point Guard", 
    "team": "Brooklyn Nets"
}
    
player_kevin = Player(kevin)
player_jason = Player(kevin)
player_kyrie = Player(kevin)


print("A")
print(player_kevin,player_jason,player_kyrie)

print("B")
print(player_kevin.name,player_kevin.age,player_kevin.position,player_kevin.team)

print("C")
new_team = []
for player in players:
    this_player = Player(player)
    new_team.append(this_player)
print(new_team)
for player in new_team:
    print(player.name,player.age,player.position,player.team)

print("D")
new_team = Player.get_team(players)
print(new_team)
for player in new_team:
    print(player.name,player.age,player.position,player.team)




