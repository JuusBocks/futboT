Bot hosted in: https://replit.com/~

# ⚽ UEFA Champions League Teams API

This project uses the **ESPN API** to fetch **UEFA Champions League (UCL) teams** for the current season. The API provides real-time team data without requiring an API key.

## 📌 API Endpoint

Base URL: http://site.api.espn.com/apis/site/v2/sports/soccer/uefa.champions/teams

## 📌 How It Works

1. Sends a `GET` request to the ESPN API.
2. Extracts **team names**, **abbreviations**, and **official links**.
3. Formats the data for easy use in a Discord bot or web app.

## 📌 Example API Response (JSON)
```json
{
    "sports": [
        {
            "leagues": [
                {
                    "teams": [
                        {
                            "team": {
                                "id": "359",
                                "displayName": "Arsenal",
                                "abbreviation": "ARS",
                                "links": [
                                    {
                                        "href": "https://www.espn.com/soccer/club/_/id/359/arsenal"
                                    }
                                ]
                            }
                        },
                        {
                            "team": {
                                "id": "86",
                                "displayName": "Real Madrid",
                                "abbreviation": "RMA",
                                "links": [
                                    {
                                        "href": "https://www.espn.com/soccer/club/_/id/86/real-madrid"
                                    }
                                ]
                            }
                        }
                    ]
                }
            ]
        }
    ]
}

🔄 Updated Discord Bot: Integrated UCL Live Scores, Fixtures, Standings, Team Stats & News

- Added `!ucl_scores`: Fetches live Champions League match updates.
- Added `!ucl_fixtures`: Retrieves upcoming UCL match schedules.
- Added `!ucl_standings`: Displays current UCL group standings.
- Added `!ucl_team_stats <team>`: Shows stats for a specific UCL team.
- Added `!ucl_news`: Fetches the latest Champions League news.
- Improved error handling for missing API data.
- Ensured environment variables are correctly handled.
- Optimized message formatting for better Discord readability.

🚀 Now the bot provides real-time UEFA Champions League updates directly in Discord! ⚽🔥


