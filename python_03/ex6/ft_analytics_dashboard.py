def get_data() -> dict:
    data = {
        "players": {
            "alice": {
                "score": 2300,  # changed from 0
                "sessions_played": 12,
                "region": "north",
                "achievements": [
                    "first_kill",
                    "level_10",
                    "speed_runner",
                    "treasure_seeker",
                    "boss_slayer",
                ],
            },
            "bob": {
                "score": 1800,
                "sessions_played": 9,
                "region": "east",
                "achievements": [
                    "first_kill",
                    "level_10",
                    "explorer",
                ],
            },
            "charlie": {
                "score": 2150,
                "sessions_played": 15,
                "region": "central",
                "achievements": [
                    "first_kill",
                    "level_10",
                    "boss_slayer",
                    "combo_king",
                    "pixel_perfect",
                    "explorer",
                    "speed_runner",
                ],
            },
            "diana": {
                "score": 2050,  # changed from 2100
                "sessions_played": 1,
                "region": "north",
                "achievements": [
                    "first_kill",
                ],
            },
        },
        "sessions": [
            {
                "player": "alice", "duration_minutes": 45,
                "score": 500, "completed": True
            },
            {
                "player": "alice", "duration_minutes": 60,
                "score": 700, "completed": True
            },
            {
                "player": "alice", "duration_minutes": 30,
                "score": 400, "completed": False
            },
            {
                "player": "bob", "duration_minutes": 50,
                "score": 600, "completed": True
            },
            {
                "player": "bob", "duration_minutes": 40,
                "score": 550, "completed": False
            },
            {
                "player": "charlie", "duration_minutes": 70,
                "score": 800, "completed": True
            },
            {
                "player": "charlie", "duration_minutes": 65,
                "score": 750, "completed": True
            },
            {
                "player": "charlie", "duration_minutes": 55,
                "score": 600, "completed": False
            },
            {
                "player": "diana", "duration_minutes": 35,
                "score": 500, "completed": True
            },
        ],
    }
    return data


def list_comprehension(players: dict) -> None:
    high_scores = [
        player for player, v in players.items()
        if v.get('score') > 2000
    ]
    scores_doubled = [v.get('score') * 2 for v in players.values()]
    active_players = [
        k for k, v in players.items()
        if v.get('sessions_played') >= 3
    ]
    print("High scorers (>2000): ", end="")
    print(high_scores)
    print("Scores doubled: ", end="")
    print(scores_doubled)
    print("Active players: ", end="")
    print(active_players)


def dict_comprehension(players: dict) -> None:
    players_scores = {k: v.get('score') for k, v in players.items()}
    score_categories = {
        'high': len([v for v in players.values() if v.get('score') > 2000]),
        'low': len([v for v in players.values() if v.get('score') < 1800]),
        'medium': len([
            v for v in players.values()
            if 1800 <= v.get('score') <= 2000
        ])
    }
    achievement_count = {
        k: len(v.get('achievements'))
        for k, v in players.items()
    }
    print("Player scores: ", end="")
    print(players_scores)
    print("Score categories: ", end="")
    print(score_categories)
    print("Achievement counts: ", end="")
    print(achievement_count)


def set_comprehension(sessions: dict, players: dict) -> None:
    unique_player = set(v.get('player') for v in sessions)
    unique_ach = set(
        c for v in players.values() for c in v.get('achievements')
    )
    active_regions = set(v.get('region') for v in players.values())
    print("Unique player: ", end="")
    print(unique_player)
    print("Unique achievements: ", end="")
    print(unique_ach)
    print("Active regions: ", end="")
    print(active_regions)


def combined_analytics(players: dict) -> None:
    total_players = len([k for k in players])
    total_unique_ach = len(
        set(c for v in players.values() for c in v.get('achievements'))
    )
    scores = list(v.get('score') for v in players.values())
    average_score = sum(scores) / len(scores)
    max_score = max(scores)
    top_performer = {
        k: v for k, v in players.items() if v.get('score') == max_score
    }
    print("Total players: ", end="")
    print(total_players)
    print("Total unique achievements: ", end="")
    print(total_unique_ach)
    print("Average score: ", end="")
    print(average_score)
    print("Top performer: ", end="")
    if len(top_performer) == 1:
        name = list(top_performer)[0]
        score = list(top_performer.values())[0].get('score')
        ach_count = len(list(top_performer.values())[0].get('achievements'))
        print(f"{name} ({score} points, {ach_count} achievements)")


def ft_analytics_dashboard() -> None:
    try:
        print("=== Game Analytics Dashboard ===\n")
        players = get_data().get('players')
        print("=== List Comprehension Examples ===")
        list_comprehension(players)
        print("\n=== Dict Comprehension Examples ===")
        dict_comprehension(players)
        print("=== Set Comprehension Examples ===")
        set_comprehension(get_data().get('sessions'), players)
        print("=== Combined Analysis ===")
        combined_analytics(players)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    ft_analytics_dashboard()
