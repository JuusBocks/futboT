import discord
import requests
import os
from discord.ext import commands

# Enable Discord bot intents
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", help_command=None, intents=intents)

@bot.command()
async def ucl_teams(ctx):
    url = "http://site.api.espn.com/apis/site/v2/sports/soccer/uefa.champions/teams"

    try:
        response = requests.get(url, timeout=10)  # Set timeout
        response.raise_for_status()  # Raise error for non-200 responses
        data = response.json()

        # Validate API response structure
        if "sports" in data and data["sports"]:
            leagues = data["sports"][0].get("leagues", [])
            for league in leagues:
                if "teams" in league:
                    teams = league["teams"]
                    teams_list = [
                        f"🔹 {team['team']['displayName']} ({team['team'].get('abbreviation', 'N/A')}) - [More Info]({team['team']['links'][0]['href']})"
                        for team in teams
                    ]

                    # Discord character limit fix: Send messages in chunks
                    message = "🏆 **UEFA Champions League Teams (2024-25)** 🏆\n"
                    char_limit = 1900  # Leave space for formatting
                    temp_message = message

                    for team in teams_list:
                        if len(temp_message) + len(team) + 2 > char_limit:  # Check if adding another team exceeds limit
                            await ctx.send(f"```{temp_message}```")
                            temp_message = ""  # Reset for next chunk
                        temp_message += f"{team}\n"

                    if temp_message:  # Send any remaining teams
                        await ctx.send(f"```{temp_message}```")
                    return

        await ctx.send("❌ No teams found for UCL 2024-25. API response may have changed.")

    except requests.exceptions.Timeout:
        await ctx.send("⏳ Request timed out. Please try again later.")
    except requests.exceptions.HTTPError as errh:
        await ctx.send(f"❌ HTTP Error: {errh}")
    except requests.exceptions.RequestException as err:
        await ctx.send("⚠️ Unable to connect to ESPN API. Check your internet connection.")
        print(f"Error: {err}")
    except Exception as e:
        await ctx.send("⚠️ An unexpected error occurred while retrieving UCL teams.")
        print(f"Error: {e}")

# Retrieve token from environment variables
bottoken = os.getenv("TOKEN")
bot.run(bottoken)