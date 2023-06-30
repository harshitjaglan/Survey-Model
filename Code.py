class Students:
    # created a dictionary for each group that counts how many members are in the group
    # and how many of them like a specific genre.
    E_dict = {'Members': 0, 'Action': 0, 'Scifi': 0, 'Comedy': 0, 'History': 0}
    M_dict = {'Members': 0, 'Action': 0, 'Scifi': 0, 'Comedy': 0, 'History': 0}
    H_dict = {'Members': 0, 'Action': 0, 'Scifi': 0, 'Comedy': 0, 'History': 0}
    C_dict = {'Members': 0, 'Action': 0, 'Scifi': 0, 'Comedy': 0, 'History': 0}
    key_list = list(E_dict.keys())[1:]

    def __init__(self, name, age, *Movie_genre) -> None:
        self.__name = name
        self.__age = age
        # list for the like and dislike in Movie_genres
        a = []
        for x in Movie_genre:
            a.append(x)
        self.__Movie_genre = a
        # Assigning Groups and Calculating Likes for a genre
        import itertools as it
        if 4 <= int(self.__age) <= 9:
            Students.E_dict['Members'] += 1
            for x, y in it.zip_longest(self.__Movie_genre, Students.key_list):
                if x == 'yes':
                    Students.E_dict[y] += 1
        if 10 <= int(self.__age) <= 14:
            Students.M_dict['Members'] += 1
            for x, y in it.zip_longest(self.__Movie_genre, Students.key_list):
                if x == 'yes':
                    Students.M_dict[y] += 1

        if 15 <= int(self.__age) <= 18:
            Students.H_dict['Members'] += 1
            for x, y in it.zip_longest(self.__Movie_genre, Students.key_list):
                if x == 'yes':
                    Students.H_dict[y] += 1

        if 19 <= int(self.__age) <= 22:
            Students.C_dict['Members'] += 1
            for x, y in it.zip_longest(self.__Movie_genre, Students.key_list):
                if x == 'yes':
                    Students.C_dict[y] += 1

    def get_genre(self):
        return self.__Movie_genre

    # method to find Fav Movie genre for a group
    @classmethod
    def find_fav_genre(cls, x):
        x = x.lower()
        if x == 'e':
            val_list = list(Students.E_dict.values())[1:]
        elif x == 'm':
            val_list = list(Students.M_dict.values())[1:]
        elif x == 'h':
            val_list = list(Students.H_dict.values())[1:]
        elif x == 'c':
            val_list = list(Students.C_dict.values())[1:]
        else:
            return "Invalid group!"
        
        max_likes = max(val_list)
        fav_genres = [Students.key_list[i] for i, likes in enumerate(val_list) if likes == max_likes]
        return 'Favorite genre(s): ' + ', '.join(fav_genres)

    # method to find what percentage of a group likes a specific genre
    @classmethod
    def calc_percentage_genre(cls, x, y):
        y = y.lower().capitalize()
        l = ('Action', 'Comedy', 'History', 'Scifi')
        if x.lower() == 'e':
            
            if y in l:
                total_members = Students.E_dict['Members']
                genre_likes = Students.E_dict[y]
        elif x.lower() == 'm':
            if y in l:
                total_members = Students.M_dict['Members']
                genre_likes = Students.M_dict[y]
        elif x.lower() == 'h':
            if y in l:
                total_members = Students.H_dict['Members']
                genre_likes = Students.H_dict[y]
        elif x.lower() == 'c':
            if y in l:
                total_members = Students.C_dict['Members']
                genre_likes = Students.C_dict[y]
        else:
            return "Invalid group!"
    
        percentage = (genre_likes / total_members) * 100
        return f"Percentage of group {x.upper()} that likes {y}: {percentage:.2f}%"


z = list(range(1, 100))
x = 0

# Taking the survey through standard input
while True:
    a1 = input('Enter your name or press "Q" to stop the survey: ')
    if a1.lower() == 'q':
        break

    while True:
        a2 = input('Enter your age (4 to 22): ')
        if a2.isdigit() and 4 <= int(a2) <= 22:
            break
        else:
            print('Invalid input! Please enter an integer value between 4 and 22.')
            

    while True:
        a3 = input('Do you like Action Movies? "YES" or "NO": ')
        if a3.lower() == "yes" or a3.lower() == "no":
            break
        else:
            print('Invalid input! Please enter "YES" or "NO".')
            

    while True:
        a4 = input('Do you like Sci-fi Movies? "YES" or "NO": ')
        if a4.lower() == "yes" or a4.lower() == "no":
            break
        else:
            print('Invalid input! Please enter "YES" or "NO".')
            

    while True:
        a5 = input('Do you like Comedy Movies? "YES" or "NO": ')
        if a5.lower() == "yes" or a5.lower() == "no":
            break
        else:
            print('Invalid input! Please enter "YES" or "NO".')
            

    while True:
        a6 = input('Do you like History Movies? "YES" or "NO": ')
        if a6.lower() == "yes" or a6.lower() == "no":
            break
        else:
            print('Invalid input! Please enter "YES" or "NO".')
            

    if a1.lower() == 'q':
        break

    z[x] = Students(a1, a2, a3, a4, a5, a6)
    x += 1

# Taking commands to do calculation
print('******')
print('Enter command for Favorite Genre or Percentage Genre:')
print('Example commands: "Fav Genre E", "Percentage Genre C Action"')
print('Enter "Q" to exit.')
print('*******')


while True:
    cmnd = input().lower()
    if cmnd == 'q':
        break

    cmd_parts = cmnd.split()
    if len(cmd_parts) == 3 and cmd_parts[0].lower() == 'fav' and cmd_parts[1].lower() == 'genre':
        print(Students.find_fav_genre(cmd_parts[2]))
    elif len(cmd_parts) == 4 and cmd_parts[0].lower() == 'percentage' and cmd_parts[1].lower() == 'genre':
        print(Students.calc_percentage_genre(cmd_parts[2].lower(), cmd_parts[3]))
    else:
        print('Invalid command! Please try again.')
