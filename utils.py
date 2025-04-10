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
    """
    Calculates the completion percentage for each year and the total progress,
    considering that each day has two parts (`part1.py` and `part2.py`).

    Returns:
        dict: A dictionary containing the progress and color for each year and the total.
    """
    data = {}

    years = [year for year in os.listdir('years') if not year.startswith('.')]
    total_parts = len(years) * 25 * 2  # 25 days per year, 2 parts per day

    completed_parts = 0
    for year in years:
        parts_completed = 0
        days = [day for day in os.listdir(f'years/{year}') if os.path.isdir(f'years/{year}/{day}')]

        for day in days:
            day_path = f'years/{year}/{day}'
            part1_path = os.path.join(day_path, 'part1.py')
            part2_path = os.path.join(day_path, 'part2.py')

            # Check if part1.py and part2.py exist and are marked as completed
            if os.path.isfile(part1_path) and open(part1_path).readline().startswith('# COMPLETED'):
                parts_completed += 1
            if os.path.isfile(part2_path) and open(part2_path).readline().startswith('# COMPLETED'):
                parts_completed += 1

        progress = calculate_progress(parts_completed, 25 * 2)  # 25 days * 2 parts per day
        color = percentage_to_color(progress)
        data[year] = (progress, color)
        completed_parts += parts_completed

    total_percentage = calculate_progress(completed_parts, total_parts)
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

    with open(os.path.join(day_folder, 'part1.py'), 'w') as p1_file:
        p1_file.write('# MARK AS COMPLETED WHEN FINISHED\n')
        p1_file.write('# COMPLETED\n')
        p1_file.write('\n')
        p1_file.write('import os\n')
        p1_file.write('\n')
        p1_file.write('if __name__ == "__main__":\n')
        p1_file.write('    pass\n')

    with open(os.path.join(day_folder, 'part2.py'), 'w') as p2_file:
        p2_file.write('# MARK AS COMPLETED WHEN FINISHED\n')
        p2_file.write('# COMPLETED\n')
        p2_file.write('\n')
        p2_file.write('import os\n')
        p2_file.write('\n')
        p2_file.write('if __name__ == "__main__":\n')
        p2_file.write('    pass\n')


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
