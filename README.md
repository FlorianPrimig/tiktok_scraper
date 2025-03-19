# tiktok_scraper
Unofficial TikTok API scraping script based on Dan Freelon's PykTok (https://github.com/dfreelon/pyktok)
Before using, pay attention to line 9 in the script (specify your browser if needed), and line 28/29 (put in the path to your CSV input file that contains the links), and line 37 (change timer if needed).
The code works with a CSV file as input containing the links of TikTok videos to scrape. An example file is attached to the repository (Friedrich Merz video links).
## Output
As output you get the video as .mp4 and some metadata (video_id,video_timestamp,video_duration,video_locationcreated,video_diggcount,video_sharecount,video_commentcount,video_playcount,video_description,video_is_ad,video_stickers,author_username,author_name,author_followercount,author_followingcount,author_heartcount,author_videocount,author_diggcount,author_verified,poi_name,poi_address,poi_city). 
## Get profile video links:
To automatically scrape the video links of a profile and save them as csv, use the "get_video_links_of_profile" script. You just need to add the profile name in there and then you'll be good to go getting around 36 video links. More than 36 videos seems to be blocked by lazy loading of TikTok.
Dependency for links scraping:
pip install selenium webdriver-manager pandas

## Citation
Primig, F. (2025). TikTok Scraper [Computer software]. Freie Universität Berlin. https://github.com/FlorianPrimig/tiktok_scraper.
