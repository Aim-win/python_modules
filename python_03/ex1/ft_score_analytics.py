import sys


def ft_score_analytics() -> None:
    print("=== Player Score Analytics ===")
    try:
        argv = sys.argv
        args_len = len(argv)
        score_list = []
        if args_len == 1:
            raise ValueError(
                "No scores provided. Usage: python3 "
                "ft_score_analytics.py <score1> <score2> ..."
            )
        for i in argv[1:]:
            score_list.append(int(i))
        print(f"Scores processed: {score_list}")
        print(f"Total players: {args_len - 1}")
        print(f"Total score: {sum(score_list)}")
        print(f"Average score: {(sum(score_list) / (args_len - 1)):.1f}")
        print(f"High score: {max(score_list)}")
        print(f"Low score: {min(score_list)}")
        print(f"Score range: {max(score_list) - min(score_list)}\n")
    except Exception as err:
        print(err)


if __name__ == '__main__':
    ft_score_analytics()
