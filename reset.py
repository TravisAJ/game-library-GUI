import pickle

games = {1:['Rhythm', 'Beat Saber', 'Beat Games', 'Oculus', 'Virtual Reality', 
            '2018', '10', 'Singleplayer', '30.00', 'No', '12/25/19', 'My favorite VR Game!'], 
         2:['Action', 'Just Shapes and Beats', 'Berzerk Studio', 'Steam', 'Windows',
            '2018', '9', 'Either', '20.00', 'Yes', '7/31/19', 'Great Music!'], 
         3:['MOBA', 'Brawl Stars', 'Supercell', 'Supercell', 'Android',
            '2017', '8.5', 'Multiplayer', 'Free', '12/12/18', 'The best mobile game!'],
         4:['Action-Adventure', 'Lego Star Wars', 'Travellers Tales', 'LucasArts', 'Xbox One',
            '2007', '7', 'Single', '20.00', 'No', '1/10/20', 'Hmmmmmm....herrrrrmmmmm']
         }

datafile = open("game_lib.pickle", "wb")
pickle.dump(games, datafile)
datafile.close()
print("Data Reseted. Go Back to the Game Library.")