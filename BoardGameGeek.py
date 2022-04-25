from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import csv
from pathlib import Path

game_list = input('Enter games seperated by "|" >>')
game_list = (game_list .split('|'))
browser=webdriver.Chrome()
for game in game_list:
    browser.get('https://boardgamegeek.com/')
    search_bar = browser.find_element(By.NAME, 'searchTerm')
    search_bar.send_keys(game)
    search_bar.send_keys(Keys.ENTER)
    first_result = browser.find_element(By.CLASS_NAME, 'primary')
    game_name = browser.find_element(By.CLASS_NAME, 'primary')
    game_rank = browser.find_element(By.CLASS_NAME, 'collection_rank')
    game_name = game_name.text
    game_rank = game_rank.text
    first_result.click()
    game_URL = browser.current_url
    player_count = browser.find_element(By.CLASS_NAME, 'gameplay-item-primary')
    recomended_player_count = browser.find_element(By.CLASS_NAME, 'gameplay-item-secondary')
    player_count=player_count.text
    recomended_player_count=recomended_player_count.text
    csv_file = Path('BoardGameGeek Game Data.csv')
    if csv_file.exists():
        with open('BoardGameGeek Game Data.csv', 'a',newline='') as save:
            writer = csv.writer(save)
            writer.writerow([game_name, game_rank, player_count, recomended_player_count, game_URL])
    else:
        with open('BoardGameGeek Game Data.csv', 'a',newline='') as save:
            writer = csv.writer(save)
            writer.writerow(['Game Name', 'Rank','Player Count','Recommended Player Count', 'BGG URL'])                
            writer.writerow([game_name, game_rank, player_count, recomended_player_count, game_URL])
browser.quit