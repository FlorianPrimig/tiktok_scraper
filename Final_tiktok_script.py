#Unofficial TikTok API scraping script based on Dan Freelon's PykTok (https://github.com/dfreelon/pyktok)
#Before using, pay attention to line 9 (specify your browser if needed), line 28/29 (put in the path to your CSV input file that contains the links), and line 37 (change timer if needed).
import pyktok as pyk
import csv
import os
from datetime import datetime

# Specify browser
pyk.specify_browser('firefox')  # Browser specification may or may not be necessary depending on your local settings

# Function to read TikTok video links from a CSV file
def read_links_from_csv(file_path):
    tiktok_links = []
    with open(file_path, 'r', newline='', encoding='utf-8-sig') as csvfile:  # Use 'utf-8-sig' to handle BOM
        reader = csv.reader(csvfile)
        for row in reader:
            if row:  # Ensure the row is not empty
                tiktok_links.append(row[0].strip())  # Strip any leading/trailing whitespace which sometimes happen to be there when links are collected manually and might cause issues
    return tiktok_links


# Function to generate a unique output file name. This avoids that file outputs are overwritten when one does multiple collections a day.
def generate_unique_filename(base_name, extension):
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    return f"{base_name}_{timestamp}.{extension}"

# Path to the CSV file containing TikTok video links
csv_file_path = r'path_to_my_links.csv'  # Replace with your actual CSV file path in between the single quotation marks.
#important! The script expects a csv file that contains the TikTok links to scrape in the format of one link per row. Open Excel, put one link per row into the first column and save as CSV (UTF-8 encoded). Examples of intput and output are in the project folder)
# Read the TikTok video links from the CSV file
tiktok_videos = read_links_from_csv(csv_file_path)

# Generate a unique output file name
output_file = generate_unique_filename('tiktok_data', 'csv')

# Save the TikTok videos data
pyk.save_tiktok_multi_urls(tiktok_videos, True, output_file, 15) # the number here in the end limits the requests made. 15 = 15 seconds between executions. You can play with that to either speed it up (unnecessary in small data collections) or slow it down to avoid rate limits and bans.
