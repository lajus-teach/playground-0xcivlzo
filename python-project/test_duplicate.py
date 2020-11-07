from duplicate import find_duplicate

def send_msg(channel, msg):
    print("TECHIO> message --channel \"{}\" \"{}\"".format(channel, msg))


def success():
    print("TECHIO> success true")


def fail():
    print("TECHIO> success false")
    

def test_count_all_stars():
    try:
        dup1 = find_duplicate(["Order 66", "Order 66"])
        assert dup1 == "Order 66", "Running count_all_stars([\"Order 66\", \"Order 66\"])... Expected \"Order 66\", got {}".format(count2)
        dup2 = find_duplicate(["Only hope", "Order 66", "Order 66", "Obiwan Kenobi"])
        assert dup2 == "Order 66", "Running count_all_stars([\"Only hope\", \"Order 66\", \"Order 66\", \"Obiwan Kenobi\"])... Expected \"Order 66\", got {}".format(count2)
        dup3 = find_duplicate([2, 3, 1, 0, 1, 12])
        assert dup3 == 1, "Running find_duplicate([2, 3, 1, 0, 1, 12])... Expected 1, got {}".format(count1)
        success()

        if sum_builtin_used:
            send_msg("Bien joué", "")
        else:
            send_msg("C'est tout bon, mais...", "Tu peux aussi utiliser directement la fonction sum.")
            send_msg("C'est tout bon, mais...", "Essaye donc:")
            send_msg("C'est tout bon, mais...", "")
            send_msg("C'est tout bon, mais...", "galaxies = [37, 3, 2]")
            send_msg("C'est tout bon, mais...", "total_stars = sum(galaxies)  # 42")
    except AssertionError as e:
        fail()
        send_msg("Oops! 🐞", e)
        send_msg("Hint 💡", "Ajoute le nombre d'étoile de chaque galaxie à la variable total_stars.")

if __name__ == "__main__":
    test_count_all_stars()
