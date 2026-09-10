from bs4 import BeautifulSoup
from urllib.parse import urlparse


def extract_usernames(filename):
    """Extract Instagram usernames from an Instagram HTML export."""

    with open(filename, "r", encoding="utf-8") as f:
        html = f.read()

    soup = BeautifulSoup(html, "html.parser")
    usernames = set()

    # Look at every Instagram link
    for a in soup.find_all("a", href=True):
        href = a["href"].strip()

        try:
            parsed = urlparse(href)

            # Only process Instagram URLs
            if parsed.netloc.lower() not in (
                "instagram.com",
                "www.instagram.com"
            ):
                continue

            # Break URL into parts
            parts = [p for p in parsed.path.split("/") if p]

            if not parts:
                continue

            # Following.html format:
            # https://www.instagram.com/_u/usernamehere
            if parts[0].lower() == "_u" and len(parts) >= 2:
                username = parts[1]

            # Followers format:
            # https://www.instagram.com/usernamehere
            else:
                username = parts[0]

            # Ignore non-profile Instagram URLs
            ignored = {
                "_u",
                "accounts",
                "about",
                "direct",
                "explore",
                "reels",
                "stories",
                "p",
                "privacy",
                "legal",
            }

            if username.lower() not in ignored:
                usernames.add(username.lower())

        except Exception:
            pass

    return usernames


# -----------------------------------------
# Extract followers and following
# -----------------------------------------

followers = extract_usernames("followers_1.html")
following = extract_usernames("following.html")


# -----------------------------------------
# Find people you follow who don't follow you
# -----------------------------------------

not_following_back = following - followers


# Sort alphabetically
not_following_back = sorted(not_following_back)


# -----------------------------------------
# Save results
# -----------------------------------------

with open("not_following_back.txt", "w", encoding="utf-8") as f:
    for username in not_following_back:
        f.write(username + "\n")


# -----------------------------------------
# Display results
# -----------------------------------------

print()
print("----------------------------------------")
print(" IG moots comparison")
print("----------------------------------------")
print(f"Followers:             {len(followers)}")
print(f"Following:             {len(following)}")
print(f"Not following you back: {len(not_following_back)}")
print("----------------------------------------")
print()
print("Saved to:")
print("not_following_back.txt")
print()