import requests, json

user_search = input("Please Enter a username: ")
v = json.loads(requests.get(f"https://www.roblox.com/search/users/results?keyword={str(user_search)}&maxRows=100&startIndex=0").text)
print("Total Results:",v["TotalResults"])

total_results = int(v["TotalResults"])
if total_results > 5:
    total_results = 5
print("\n----------------------------------------------------------------------")

# Loop through all users that show up in search results
for x in range(total_results):
    
    # Gather Data
    webpage = requests.get("https://www.roblox.com/users/"+str(v['UserSearchResults'][x]['UserId'])+"/profile")
    
    profile_image = json.loads(requests.get("https://thumbnails.roblox.com/v1/users/avatar-headshot?size=48x48&format=png&userIds="+str(v['UserSearchResults'][x]['UserId'])+"").text)["data"][0]["imageUrl"]
    
    Badges = json.loads(requests.get("https://accountinformation.roblox.com/v1/users/"+str(v['UserSearchResults'][x]['UserId'])+"/roblox-badges").text)
    
    # Print out basic user data
    print("Basic User Data:")
    print("    User Id:",v["UserSearchResults"][x]["UserId"])
    print("    User Name:",v["UserSearchResults"][x]["Name"])
    print("    Display Name:",v["UserSearchResults"][x]["DisplayName"])
    print("    Previous User Names:",v["UserSearchResults"][x]["PreviousUserNamesCsv"])
    print("    User Online:",v["UserSearchResults"][x]["IsOnline"])
    print("    About Section:",f"\"{v['UserSearchResults'][x]['Blurb']}\"")
    print("    Link to Avatar image:",profile_image)
    print("    Url to profile page:","https://www.roblox.com/users/"+str(v['UserSearchResults'][x]['UserId'])+"/profile")
    print()
    
    print("Advanced User Data:")
    print("    Last Location:",v["UserSearchResults"][x]["LastLocation"])
    print("    Last Seen Date:",v["UserSearchResults"][x]["LastSeenDate"])
    print("    Primary Group:",v["UserSearchResults"][x]["PrimaryGroup"])
    print("    Primary Group URL:",v["UserSearchResults"][x]["PrimaryGroupUrl"])
    print()
    
    # Print out all of users badges
    print("Badges:")
    total_badges = len(Badges)
    if total_badges != 0:
        for x in range(total_badges):
            print("    Badge Id:",Badges[x]["id"])
            print("    Badge Name:",Badges[x]["name"])
            print("    Badge Description:","\""+Badges[x]["description"]+"\"")
            print("    Badge Image Url:",Badges[x]["imageUrl"])
            if total_badges - (x+1) != 0:
                print("    -----------------------")
    else:
        print("    No Current Badges")
        
    print()
    print("----------------------------------------------------------------------")
