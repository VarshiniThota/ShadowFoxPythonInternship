justice_league = ["Superman","Batman","WonderWoman","Flash","Aquaman","Green Lantern"]
#1
print("No.of members in just_league : ",len(justice_league))
#2
print("adding new members to the list ")
justice_league.append("Batgirl")
justice_league.append("Nightwing")
print("New list after addition ",justice_league)
#3
for i in justice_league :
    if i=='WonderWoman' :
        j=justice_league.index(i)
        k=justice_league[0]
        justice_league[0]=i
        justice_league[j]=k
print("New list after modification ",justice_league)
#4
for i in range(len(justice_league)) :
    if justice_league[i]=='Flash' :
        if justice_league[i + 1] == "Aquaman":
            green_lantern_index = justice_league.index("Green Lantern")
            justice_league[i + 1] = "Green Lantern"
            justice_league[green_lantern_index] = "Aquaman"
            print("New list after inserting Green latern between Flash and Aquaman ",justice_league)
#5
justice_league = list(filter(lambda member: member == "Superman", justice_league))
new_mem=["Cyborg","Shazam","Hawkgirl","MartianManhunter","Green Arrow"]
justice_league.extend(new_mem)
print("justice_league with new members ",justice_league)
#6
justice_league.sort()
print("list after sorting :",justice_league)
print("New leader :",justice_league[0])