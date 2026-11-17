
levels = [1, 2, 3, 4, 5]
coins = [5, 8, 3, 10, 7]
enemies = [2, 4, 1, 5, 3]
power_ups = ["Mushroom", "Star", "Flower", "Mushroom", "Star"]

print("===== PLATFORM ADVENTURE =====")
for i in range(len(levels)):
    print(f"Level {levels[i]}")
    print(f"Coins: {coins[i]}")
    print(f"Enemies: {enemies[i]}")
    print(f"Power ups: {power_ups[i]}")

player_name="Hero"
lives=3
score=0
total_coins=0

print("===== PLAYER INFORMATION =====")
print(f"Player: {player_name}")
print(f"Lives: {lives}")
print(f"Score: {score}")
print(f"Coins: {total_coins}")

coin_points=10
enemy_points=-5
star_bonus=25

level_scores=[]
for i in range(len(levels)):
    level_score=coins[i] * coin_points + enemies[i] * enemy_points
    if power_ups[i] == "Star":
        level_score+=star_bonus
    level_scores.append(level_score)

print("===== LEVEL SCORES =====")
for i in range (len(levels)):
    print(f"Level {levels[i]} Score: {level_scores[i]}")

print("===== ADVENTURE ACTIONS =====")
actions= [0, 1, 0, 2, 1]
action_results=[]

for i in range(len(actions)):
    if actions[i]==0:
        action="Collect Coins"
    elif actions[i]==1:
        action="Fight Enemies"
    else:
        action="Use Power-Up"
    action_results.append(action)
    print(f"Level {levels[i]} {action_results[i]}")

print("==== LIFE HISTORY ====")
life_history= []
for i in range(len(levels)):
    if enemies[i] >= 4 and power_ups[i] != "Star":
        lives-=1
        life_history.append(lives)
for i in range(len(coins)):
    total_coins += coins[i]

bonus_coin_levels= [coin for coin in coins if coin >= 7]

print("==== COIN COLLECTION ====")
print(f"Coins Collected: {total_coins}")
print(f"Levels with 7 or more coins: {bonus_coin_levels}")

print("==== INVENTORY ====")
inventory = ["Mushroom", "Star", "Flower"]
used_powerups= ["Mushroom", "Star"]

starting_inventory = inventory[:]
for i in range(len(used_powerups)):
    inventory.pop(0)
print(f"Starting Inventory: {starting_inventory}")
print(f"Used Power-Ups: {used_powerups}")
print(f"Remaining Inventory: {inventory}")

print("==== LEVEL ANALYSIS =====")

most_coins=max(coins)
fewest_coins=min(coins)
average_coins=total_coins/ len(coins)
total_enemies= sum(enemies)
most_enemies=max(enemies)

print(f"Total Coins: {total_coins}")
print(f"Most Coins in One Level: {most_coins}")
print(f"Fewest Coins in One Level: {fewest_coins}")
print(f"Average Coins in One Level: {average_coins}")
print(f"Total Enemies: {total_enemies}")
print(f"Most Enemies in One Level: {most_enemies}")

high_scores= [level_score for level_score in level_scores if level_score >= 50]

print("==== HIGH SCORES ====")
print("Scores of 50 or Higher: {high_scores}")

print("==== SCORE HISTORY ====")
for i in range (len(high_scores)):
    print(f"After Level {levels[i]}")
print(f"First Two Scores: {life_history[:2]}")
print(f"Last Two Scores: {life_history[-2:]}")

if lives == 0:
    final_status = "Game Over"
elif score >=250:
    final_status = "Adventure Champion"
elif score >= 150:
    final_status = "Great Adventure"
else:
    final_status = "Keep Practicing"
print(f"Final Status: {final_status}")

print("==== FINAL STATUS ===")
print(final_status)

print("==== ADVENTURE RANKING =====")
print(f"Final Score: {score}")
print(f"Final Lives: {lives}")
print("Rank: Legend")







