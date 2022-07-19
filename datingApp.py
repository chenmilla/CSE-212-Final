from numpy import empty


def things_in_common(set1, set2):
    pass
    set_intersection = set()
    
    for item in set1:
        if item in set2:
             set_intersection.add(item)
    if len(set_intersection) >= 3:
        print("This couple should go on a date")
    else:
        print("This couple don't have many things in common")


#Couple 1

Luisca = {"Video Games","Soccer","Books","Lakes","Books","Mountain Bike","Dancing","Karate","Sushi","Tacos"}
Renata = {"Sushi","Mountain Bike", "Soccer", "Ballet", "Church activities", "Dancing","Bad Bunny", "Nature"}
print("Results for Luisca and Renata: ")
things_in_common(Luisca,Renata)
print("")

#Couple 2
Theo = {"Naruto", "Video Games", "Programming", "IT", "Dragon Ball Z", "Camping", "Chess", "In-and-out","Computers"}
Lizzy = {"Netflix", "Spa", "Tennis", "Camping", "Gym", "Pasta", "Books", "Painting", "Community Service", "Institute", "FHE Group"}
print("Results for Theo and Lizzy: ")
things_in_common(Theo,Lizzy)
