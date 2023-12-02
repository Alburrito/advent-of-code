# This file contains utility functions for the Advent of Code repository.
# This IS NOT RELATED with the Advent of Code challenge itself.
# It is only used to update the README.md file with the progress badge
# and to create the folder structure for a new day (too lazy to do it manually)

# If you still want to use this file, you can do it by running:
# python3 utils.py <command> <args>
# where <command> is one of the following:
# - update-progress: updates the progress badge in the README.md file. Runned with a pre-commit hook.
# - mkday YYYY DD: creates the folder structure for a new day.

import os
import re
import sys

def percentage_to_color(percentage):
    color = 'blue'
    if 0 <= percentage < 25:
        color = 'red'
    elif 25 <= percentage < 50:
        color = 'orange'
    elif 50 <= percentage < 75:
        color = 'yellow'
    elif 75 <= percentage <= 100:
        color = 'green'
    return color

def calculate_progress(completed_days, total_days):
    progress = (completed_days / total_days) * 100 if total_days > 0 else 0
    return int(progress * 100) / 100

def calculate_completion_percentage():
    data = {}

    years = [year for year in os.listdir('years') if not year.startswith('.')]
    total_days = len(years) * 25

    completed_days = 0
    for year in years:
        days = [ # Add day if the folder contains 'main.py' with # COMPLETED flag
            day for day in os.listdir(f'years/{year}') if \
                os.path.isfile(os.path.join(f'years/{year}/{day}', 'main.py')) and \
                open(os.path.join(f'years/{year}/{day}', 'main.py')).readline().startswith('# COMPLETED')
        ]
        progress = calculate_progress(len(days), 25)
        color = percentage_to_color(progress)
        data[year] = (progress, color)
        completed_days += len(days)

    total_percentage = calculate_progress(completed_days, total_days)
    total_color = percentage_to_color(total_percentage)
    data['total'] = (total_percentage, total_color)
    
    return data

def create_day_files(year, day):
    day_folder = f"years/{year}/Day{day:02d}/"
    os.makedirs(day_folder, exist_ok=True)

    with open(os.path.join(day_folder, 'input'), 'w') as input_file:
        input_file.write('Add your challenge input here')

    with open(os.path.join(day_folder, 'README.md'), 'w') as readme_file:
        readme_file.write(f'# Day {day}: Challenge\n\nPut your challenge explanation here.')

    with open(os.path.join(day_folder, 'main.py'), 'w') as main_file:
        main_file.write('# Add your Python solution code here')

def update_readme_badge(data):
    with open('README.md', 'r') as file:
        readme_content = file.read()

    for year, (progress, color) in data.items():
        if year == 'total':
            continue
        badge_url = f"https://img.shields.io/badge/Progress-{progress:.2f}%25-{color}"
        badge_markdown = f"![Progress]({badge_url})"
        readme_content = re.sub(
            fr'(\[Year {year}\]\(.*?\) \!\[Progress\]\()https://img.shields.io/badge/Progress-[0-9]*\.[0-9]*%25-[a-z]*\)',
            f'[Year {year}](./years/{year}/) {badge_markdown}',
            readme_content
        )

    total_progress, total_color = data['total']
    badge_url_total = f"https://img.shields.io/badge/Progress-{total_progress:.2f}%25-{total_color}"
    badge_markdown_total = f"![Progress]({badge_url_total})"
    total_pattern = r'!\[Progress\]\(.*?\)'
    total_match = re.search(total_pattern, readme_content)
    if total_match:
        start, end = total_match.span()
        readme_content = readme_content[:start] + f'{badge_markdown_total}' + readme_content[end:]

    with open('README.md', 'w') as file:
        file.write(readme_content)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage:")
        print("python3 utils.py update-progress")
        print("python3 utils.py mkday <year> <day>")
        sys.exit(1)

    command = sys.argv[1]

    if command == 'update-progress':
        data = calculate_completion_percentage()
        update_readme_badge(data)
    elif command == 'mkday' and len(sys.argv) == 4:
        year_arg, day_arg = sys.argv[2], sys.argv[3]

        try:
            year = int(year_arg)
            day = int(day_arg)
        except ValueError:
            print("Please provide valid year and day values.")
            sys.exit(1)

        if not (1 <= day <= 25):
            print("Day should be between 1 and 25.")
            sys.exit(1)

        create_day_files(year, day)
        print(f"Day {day} for year {year} has been created in 'years/{year}/Day{day:02d}/'")
    else:
        print("Invalid command or arguments.")
        print("Usage:")
        print("python3 utils.py update-progress")
        print("python3 utils.py mkday <year> <day>")
        sys.exit(1)
