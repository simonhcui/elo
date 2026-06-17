import json
import math
import sys

Z_98 = 2.3263478740408408  # two-sided 98% confidence interval

def calculate_field_strength(players):
    n = len(players)

    if n == 0:
        raise ValueError("No players found in JSON file.")

    ratings = [p["rating"] for p in players]

    # Convert CI half-widths to standard deviations
    sigmas = [p["ci98"] / Z_98 for p in players]

    mean_rating = sum(ratings) / n

    variance_of_mean = sum(s * s for s in sigmas) / (n * n)
    sigma_mean = math.sqrt(variance_of_mean)

    ci98_half_width = Z_98 * sigma_mean

    return {
        "num_players": n,
        "average_rating": mean_rating,
        "average_rating_sigma": sigma_mean,
        "average_rating_ci98": ci98_half_width,
        "lower_98": mean_rating - ci98_half_width,
        "upper_98": mean_rating + ci98_half_width,
    }

def main():
    if len(sys.argv) != 2:
        print("Usage: python field_strength.py ratings.json")
        sys.exit(1)

    filename = sys.argv[1]

    with open(filename, "r", encoding="utf-8") as f:
        players = json.load(f)

    result = calculate_field_strength(players)

    print(f"Players: {result['num_players']}")
    print(f"Average field strength: {result['average_rating']:.2f}")
    print(
        f"98% CI: ±{result['average_rating_ci98']:.2f}"
    )
    print(
        f"Range: [{result['lower_98']:.2f}, {result['upper_98']:.2f}]"
    )

if __name__ == "__main__":
    main()