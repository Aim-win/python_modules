
def ft_achievement_tracker() -> None:
    print("=== Achievement Tracker System ===\n")
    alice = {
        'first_kill', 'first_kill', 'level_10',
        'treasure_hunter', 'speed_demon'
    }
    bob = {
        'first_kill', 'level_10', 'level_10',
        'boss_slayer', 'collector'
    }
    charlie = {
        'level_10', 'treasure_hunter', 'boss_slayer', 'speed_demon',
        'perfectionist', 'speed_demon'
    }
    try:
        print(f"Player alice achievements: {alice}")
        print(f"Player bob achievements: {bob}")
        print(f"Player charlie achievements: {charlie}\n")

        print("=== Achievement Analytics ===")
        unique_ach = alice.union(bob).union(charlie)
        print(f"All unique achievements: {unique_ach}")
        print(f"Total unique achievements: {len(unique_ach)}\n")

        common_ach = alice.intersection(bob, charlie)
        print(f"Common to all players: {common_ach}")
        alice_rare_ach = alice.difference(bob, charlie)
        bob_rare_ach = bob.difference(alice, charlie)
        charlie_rare_ach = charlie.difference(alice, bob)
        rare_ach = alice_rare_ach.union(charlie_rare_ach, bob_rare_ach)
        print(f"Rare achievements (1 player): {rare_ach}\n")

        print(f"Alice vs Bob common: {alice.intersection(bob)}")
        print(f"Alice unique: {alice.difference(bob)}")
        print(f"Bob unique: {bob.difference(alice)}")
    except Exception as e:
        print(e)


if __name__ == '__main__':
    ft_achievement_tracker()
