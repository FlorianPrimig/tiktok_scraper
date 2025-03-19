# tiktok_scraper
Unofficial TikTok API scraping script based on Dan Freelon's PykTok (https://github.com/dfreelon/pyktok)
Before using, pay attention to line 9 in the script (specify your browser if needed), and line 28/29 (put in the path to your CSV input file that contains the links), and line 37 (change timer if needed).
The code works with a CSV file as input containing the links of TikTok videos to scrape. An example file is attached to the repository (Friedrich Merz video links).
### Install dependencies PykTok:
``` bash
git clone https://github.com/dfreelon/pyktok.git
cd pyktok
pip install .
```
### And TikTokApi
``` bash
pip install TikTokApi
```
### Specify browser
``` bash
pyk.specify_browser('firefox')  # Browser specification may or may not be necessary depending on your local settings
```
#### Set path to the CSV file containing TikTok video links
``` bash
csv_file_path = r'path_to_my_links.csv'  # Replace with your actual CSV file path - I added an example .csv file with some Friedrich Merz links to the repository.
#important! The script expects a csv file that contains the TikTok links to scrape in the format of one link per row. Open Excel, put one link per row into the first column and save as CSV (UTF-8 encoded). Examples of intput and output are in the project folder)
```

## Output
As output you get the video as .mp4 and some metadata as a csv file (video_id,video_timestamp,video_duration,video_locationcreated,video_diggcount,video_sharecount,video_commentcount,video_playcount,video_description,video_is_ad,video_stickers,author_username,author_name,author_followercount,author_followingcount,author_heartcount,author_videocount,author_diggcount,author_verified,poi_name,poi_address,poi_city). 

## Additional TikTok profile video links scraper (based on selenium):
To automatically scrape the video links of a profile and save them as csv, use the "Get_all_Links_of_profile.py" script. You just need to add the profile name in there and then you'll be good to go getting around 36 video links. More than 36 videos seems to be blocked by lazy loading of TikTok.
### Install dependencies
```bash
pip install selenium webdriver-manager pandas
```
Make sure to adjust the username you aim to scraoe in the script. I used markus.soeder as an example here. You can also play with the wait times (here 5 sec) and the maximum attempts (here 30).
```bash
    username = "markus.soeder" #add the suername to scrape here, no "@" needed!
    video_links = get_tiktok_video_links(username, max_attempts=30, scroll_pause=5)
```

## Citation
Primig, F. (2025). TikTok Scraper [Computer software]. Freie Universität Berlin. https://github.com/FlorianPrimig/tiktok_scraper.
