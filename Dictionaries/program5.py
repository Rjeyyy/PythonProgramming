cricketer = {
    "VinayKumar": [102, 5],
    "Yuzvendra Chahal": [89, 10],
    "Sandeep Sharma": [95, 8],
    "Umesh Yadav": [85, 6],
    "BhuvaneswarKumar": [106, 10],
    "Basil Thampi": [70, 5]
}

for player, stats in cricketer.items():
    runs_conceded, wickets_taken = stats
    bowling_average = runs_conceded / wickets_taken
    cricketer[player] = [round(bowling_average, 2)]

sorted_cricketer = dict(sorted(cricketer.items(), key=lambda x: x[1]))

print(sorted_cricketer)
