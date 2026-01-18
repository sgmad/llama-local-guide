import os
import random
import json
from datetime import datetime
import pytz

def run_logic():
    try:
        with open('config.json', 'r') as f:
            config = json.load(f)
    except FileNotFoundError:
        return False

    raw_forced_mode = os.getenv("FORCED_MODE", "").strip()
    mode_name = raw_forced_mode if raw_forced_mode and raw_forced_mode != "none" else config.get("active_mode", "standard")
    
    tz = pytz.timezone(config.get("timezone", "Asia/Manila"))
    now = datetime.now(tz)
    date_str = now.strftime('%Y-%m-%d')
    today_name = now.strftime('%A')

    if date_str in config.get("blackout_dates", []) or mode_name not in config.get("modes", {}):
        return False

    mode_settings = config["modes"][mode_name]
    day_settings = mode_settings["schedule"].get(today_name, mode_settings["schedule"]["Default"])
    
    if random.random() < day_settings["probability"]:
        num_commits = random.randint(day_settings["min"], day_settings["max"])
        if num_commits <= 0: return False

        messages = ["fix: resolve null pointer in helper [skip ci]", "docs: update readme with new api endpoints [skip ci]", "refactor: optimize data processing loop [skip ci]", "chore: routine dependency update [skip ci]", "style: fix linting issues in controllers [skip ci]", "test: expand coverage for auth module [skip ci]", "feat: add experimental support for batch processing [skip ci]", "patch: minor configuration tweak [skip ci]", "cleanup: remove deprecated utility functions [skip ci]", "perf: improve database query execution time [skip ci]", "ci: update github actions workflow for robustness [skip ci]"]
        
        # LOGIC: Use your verified GitHub email here to get contribution credit
        os.system('git config user.email "scmad@proton.me"')
        os.system('git config user.name "sgmad"')
        
        for i in range(num_commits):
            with open("activity.txt", "a") as f:
                f.write(f"Commit {i+1}/{num_commits} at {now.isoformat()} (PHT)\n")
            os.system("git add activity.txt")
            os.system(f'git commit -m "{random.choice(messages)}"')
        return True
    return False

if __name__ == "__main__":
    run_logic()
