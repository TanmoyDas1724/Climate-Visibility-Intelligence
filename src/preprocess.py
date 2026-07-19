import pandas as pd


FEATURE_COLUMNS = [
    'Temperature (C)',
    'Apparent Temperature (C)',
    'Humidity',
    'Wind Speed (km/h)',
    'Wind Bearing (degrees)',
    'Loud Cover',
    'Pressure (millibars)',
    'Year',
    'Month',
    'Day',
    'Hour',
    'DayOfWeek',
    'IsWeekend',
    'Summary_Breezy',
    'Summary_Breezy and Dry',
    'Summary_Breezy and Foggy',
    'Summary_Breezy and Mostly Cloudy',
    'Summary_Breezy and Overcast',
    'Summary_Breezy and Partly Cloudy',
    'Summary_Clear',
    'Summary_Dangerously Windy and Partly Cloudy',
    'Summary_Drizzle',
    'Summary_Dry',
    'Summary_Dry and Mostly Cloudy',
    'Summary_Dry and Partly Cloudy',
    'Summary_Foggy',
    'Summary_Humid and Mostly Cloudy',
    'Summary_Humid and Overcast',
    'Summary_Humid and Partly Cloudy',
    'Summary_Light Rain',
    'Summary_Mostly Cloudy',
    'Summary_Overcast',
    'Summary_Partly Cloudy',
    'Summary_Rain',
    'Summary_Windy',
    'Summary_Windy and Dry',
    'Summary_Windy and Foggy',
    'Summary_Windy and Mostly Cloudy',
    'Summary_Windy and Overcast',
    'Summary_Windy and Partly Cloudy',
    'Precip Type_rain',
    'Precip Type_snow',
    'Season_Autumn',
    'Season_Spring',
    'Season_Summer',
    'Season_Winter'
]


def preprocess_input(input_dict):

    df = pd.DataFrame([input_dict])

    df = df.reindex(columns=FEATURE_COLUMNS, fill_value=0)

    return df