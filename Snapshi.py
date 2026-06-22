from bs4 import BeautifulSoup
import os

def extract_snapchat_friends(file_path):
    if not os.path.exists(file_path):
        print(f"Error: {file_path} not found.")
        return

    with open(file_path, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f, 'html.parser')

    # Snapchat exports often use tables for the friend list
    # We look for the display names and usernames
    friends_list = []
    
    # Target common Snapchat HTML structures
    # Usually: <tr><td>Username</td><td>Display Name</td>...</tr>
    rows = soup.find_all('tr')
    
    for row in rows:
        cells = row.find_all('td')
        if len(cells) >= 2:
            username = cells[0].get_text().strip()
            display_name = cells[1].get_text().strip()
            
            # Filter out the header row if it exists
            if username.lower() != "username":
                friends_list.append({
                    "username": username,
                    "display_name": display_name
                })

    return friends_list

if __name__ == "__main__":
    # Ensure this matches your file name
    input_file = "friends.html" 
    
    friends = extract_snapchat_friends(input_file)
    
    if friends:
        print(f"{'USERNAME':<20} | {'DISPLAY NAME'}")
        print("-" * 40)
        
        with open("snapchat_usernames_list.txt", "w", encoding='utf-8') as out_file:
            for friend in friends:
                line = f"{friend['username']:<20} | {friend['display_name']}"
                print(line)
                out_file.write(f"{friend['username']}\n")
        
        print(f"\nSuccessfully extracted {len(friends)} usernames.")
        print("Usernames (only) have been saved to 'snapchat_usernames_list.txt'.")
    else:
        print("No usernames found. Check if the file format has changed.")