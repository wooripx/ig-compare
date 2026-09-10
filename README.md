# ig-compare
script to output usernames (non-moots in ig) using python and beautifulsoup4

# usage
1. put all files in one folder

  nonmoots
  ├── followers_1.html
  ├── following.html
  └── compare.py

2. run in cmd
    python compare.py

3. if everything is good, output is like this:
   
  --------------------------------
  Followers: 850
  Following: 920
  Not following you back: 125
  --------------------------------
  Saved to: not_following_back.txt

4. folder will then be:

  nonmoots
  ├── followers_1.html
  ├── following.html
  ├── compare.py
  └── not_following_back.txt
