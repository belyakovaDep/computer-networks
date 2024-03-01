from selenium import webdriver as wd
from selenium.webdriver.common.by import By
import csv

class DayWeatherInfo:
    def __init__(self, day, month, min_weather, max_weather, 
                 wind_direction_am = None, wind_speed_am = None, 
                 wind_direction_pm = None, wind_speed_pm = None):
        self.day = day
        self.month = month
        self.min_wth = min_weather
        self.max_wth = max_weather
        self.w_direction_am = wind_direction_am
        self.w_speed_am = wind_speed_am
        self.w_direction_pm = wind_direction_pm
        self.w_speed_pm = wind_speed_pm


browser = wd.Chrome()

browser.get('https://www.weatheronline.co.uk/Sweden/Enkoping.htm')

min_temp_for_4_days = browser.find_elements(By.CLASS_NAME, 'Temp_minus')
max_temp_for_4_days = browser.find_elements(By.CLASS_NAME, 'Temp_plus')

grid_with_dates = browser.find_element(By.CLASS_NAME, 'gr1')
dates_site_info = grid_with_dates.find_element(By.XPATH, '/html/body/div/div[3]/div[1]/div/div[4]/div[2]/div[1]/div[4]/table/tbody/tr[1]')
dates_in_array = dates_site_info.text.strip().split(' ')

today = DayWeatherInfo(dates_in_array[2], dates_in_array[1], 
                       min_temp_for_4_days[0].text, max_temp_for_4_days[0].text)

tmrw = DayWeatherInfo(dates_in_array[5], dates_in_array[4], 
                       min_temp_for_4_days[1].text, max_temp_for_4_days[1].text)

day_after_tmrw = DayWeatherInfo(dates_in_array[8], dates_in_array[7], 
                       min_temp_for_4_days[2].text, max_temp_for_4_days[2].text)

snd_day_after_tmrw = DayWeatherInfo(dates_in_array[11], dates_in_array[10], 
                       min_temp_for_4_days[3].text, max_temp_for_4_days[3].text)


wind = browser.find_element(By.XPATH, '/html/body/div/div[3]/div[1]/div/div[4]/div[2]/div[1]/div[3]/div/ul/li[2]/a')
wind.click()

wind_info_am = browser.find_element(By.XPATH, '/html/body/div/div[3]/div[1]/div/div[4]/div[2]/div[1]/div[4]/table/tbody/tr[2]')
wind_info_array_am = wind_info_am.text.strip().split(' ')[1:]

wind_info_pm = browser.find_element(By.XPATH, '/html/body/div/div[3]/div[1]/div/div[4]/div[2]/div[1]/div[4]/table/tbody/tr[3]')
wind_info_array_pm = wind_info_pm.text.strip().split(' ')[1:]

today.w_direction_am = wind_info_array_am[0]
today.w_speed_am = wind_info_array_am[1]
today.w_direction_pm = wind_info_array_pm[0]
today.w_speed_pm = wind_info_array_pm[1]

tmrw.w_direction_am = wind_info_array_am[2]
tmrw.w_speed_am = wind_info_array_am[3]
tmrw.w_direction_pm = wind_info_array_pm[2]
tmrw.w_speed_pm = wind_info_array_pm[3]

day_after_tmrw.w_direction_am = wind_info_array_am[4]
day_after_tmrw.w_speed_am = wind_info_array_am[5]
day_after_tmrw.w_direction_pm = wind_info_array_pm[4]
day_after_tmrw.w_speed_pm = wind_info_array_pm[5]

snd_day_after_tmrw.w_direction_am = wind_info_array_am[6]
snd_day_after_tmrw.w_speed_am = wind_info_array_am[7]
snd_day_after_tmrw.w_direction_pm = wind_info_array_pm[6]
snd_day_after_tmrw.w_speed_pm = wind_info_array_pm[7]

days_info = [today, tmrw, day_after_tmrw, snd_day_after_tmrw]

with open('weather_info.csv', 'w') as f:
    writer = csv.writer(f)

    writer.writerow(['Day', 'Month', 'MinTemp', 'MaxTemp', 
                     'WindDirectionAM', 'WindSpeedAM',
                     'WindDirectionPM', 'WindSpeedPM'])

    for i in days_info:
        writer.writerow([i.day, i.month, i.min_wth, i.max_wth, 
                         i.w_direction_am, i.w_speed_am, 
                         i.w_direction_pm, i.w_speed_pm])