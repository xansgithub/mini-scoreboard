# mini-scoreboard
A lightweight Flask app that pulls live NFL scores from ESPN's API and displays them on an auto-scrolling web page. Built as a homelab project to practice REST API integration, Python web development, and self-hosting.

# Features
- Fetches current NFL scoreboard data from ESPN API
- Parses the JSON response into simple matchup strings (e.g. BUF: 24 KC: 0)
- Render games with Flask and Jinja templates
- Small display window that auto-scrolls and snaps to each matchup
- Pauses auto-scroll on hover/touch so you can read or scroll manually

# Tech Stack
- Python3
- Flask
- Requests (ESPN API calls)
- HTML / CSS / JavaScript

# Notes
- Uses ESPN's public, unofficial API, which is undocumented and may change without notice
- Intended for personal, non-commercial use

# Future Improvements
- Auto-refresh scores without reloading the program. It is currently designed otherwise to prevent excessive API requests
- Show game status (quarter, clock, final)
- Add team logos
- Docker container for easier homelab deployment
