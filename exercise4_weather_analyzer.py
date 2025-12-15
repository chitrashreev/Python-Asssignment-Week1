{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "fdf5ac27",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: requests in c:\\users\\abhin\\anaconda3\\lib\\site-packages (2.31.0)\n",
      "Requirement already satisfied: charset-normalizer<4,>=2 in c:\\users\\abhin\\anaconda3\\lib\\site-packages (from requests) (2.0.4)\n",
      "Requirement already satisfied: idna<4,>=2.5 in c:\\users\\abhin\\anaconda3\\lib\\site-packages (from requests) (3.4)\n",
      "Requirement already satisfied: urllib3<3,>=1.21.1 in c:\\users\\abhin\\anaconda3\\lib\\site-packages (from requests) (1.26.16)\n",
      "Requirement already satisfied: certifi>=2017.4.17 in c:\\users\\abhin\\anaconda3\\lib\\site-packages (from requests) (2023.7.22)\n",
      "Note: you may need to restart the kernel to use updated packages.\n"
     ]
    }
   ],
   "source": [
    "pip install requests"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "7100db5e",
   "metadata": {},
   "outputs": [],
   "source": [
    "import requests\n",
    "import csv\n",
    "from datetime import datetime"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "322b9b27",
   "metadata": {},
   "outputs": [],
   "source": [
    "def fetch_weather(city: str, api_key: str) -> dict:\n",
    "    \"\"\"\n",
    "    Fetch weather data for a given city using OpenWeatherMap API\n",
    "    \"\"\"\n",
    "    try:\n",
    "        # API endpoint\n",
    "        url = \"https://api.openweathermap.org/data/2.5/weather\"\n",
    "\n",
    "        # Parameters for API call\n",
    "        params = {\n",
    "            \"q\": city,\n",
    "            \"appid\": api_key,\n",
    "            \"units\": \"metric\"\n",
    "        }\n",
    "\n",
    "        # Make API request\n",
    "        response = requests.get(url, params=params)\n",
    "        response.raise_for_status()  # checks for HTTP errors\n",
    "\n",
    "        # Return JSON response\n",
    "        return response.json()\n",
    "\n",
    "    except requests.exceptions.HTTPError:\n",
    "        print(\"❌ Invalid city name or API key.\")\n",
    "    except requests.exceptions.ConnectionError:\n",
    "        print(\"❌ Network error. Check your internet connection.\")\n",
    "    except Exception as e:\n",
    "        print(\"❌ Unexpected error:\", e)\n",
    "\n",
    "    return {}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "18bb4bb1",
   "metadata": {},
   "outputs": [],
   "source": [
    "def analyze_weather(weather_data: dict) -> str:\n",
    "    \"\"\"\n",
    "    Analyze weather data and return summary\n",
    "    \"\"\"\n",
    "    try:\n",
    "        # Extract required values\n",
    "        temperature = weather_data[\"main\"][\"temp\"]\n",
    "        humidity = weather_data[\"main\"][\"humidity\"]\n",
    "        wind_speed = weather_data[\"wind\"][\"speed\"]\n",
    "\n",
    "        # Temperature analysis\n",
    "        if temperature <= 10:\n",
    "            summary = \"Cold (≤10°C)\"\n",
    "        elif 11 <= temperature <= 24:\n",
    "            summary = \"Mild (11–24°C)\"\n",
    "        else:\n",
    "            summary = \"Hot (≥25°C)\"\n",
    "\n",
    "        # Add warnings\n",
    "        if wind_speed > 10:\n",
    "            summary += \" | High wind alert!\"\n",
    "        if humidity > 80:\n",
    "            summary += \" | Humid conditions!\"\n",
    "\n",
    "        return summary\n",
    "\n",
    "    except KeyError:\n",
    "        return \"❌ Invalid weather data received.\"\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "efe7ce2a",
   "metadata": {},
   "outputs": [],
   "source": [
    "def log_weather(city: str, filename: str, api_key: str):\n",
    "    \"\"\"\n",
    "    Fetches weather data and saves it to a CSV file\n",
    "    \"\"\"\n",
    "    weather = fetch_weather(city, api_key)\n",
    "\n",
    "    if not weather:\n",
    "        return\n",
    "\n",
    "    # Extract required data\n",
    "    temp = weather[\"main\"][\"temp\"]\n",
    "    humidity = weather[\"main\"][\"humidity\"]\n",
    "    wind = weather[\"wind\"][\"speed\"]\n",
    "    time = datetime.now().strftime(\"%Y-%m-%d %H:%M:%S\")\n",
    "\n",
    "    # Append data to CSV file\n",
    "    with open(filename, \"a\", newline=\"\") as file:\n",
    "        writer = csv.writer(file)\n",
    "\n",
    "        # Write header only if file is empty\n",
    "        if file.tell() == 0:\n",
    "            writer.writerow([\"City\", \"Temperature\", \"Humidity\", \"Wind Speed\", \"DateTime\"])\n",
    "\n",
    "        writer.writerow([city, temp, humidity, wind, time])\n",
    "\n",
    "    print(\"✅ Weather data saved to file.\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "ab333b27",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter city name: Hyderabad\n",
      "Enter your OpenWeatherMap API key: 23154767ed4077d510a67dd4fed4ed02\n",
      "\n",
      "Weather Analysis:\n",
      "Hot (≥25°C)\n",
      "✅ Weather data saved to file.\n"
     ]
    }
   ],
   "source": [
    "city = input(\"Enter city name: \")\n",
    "api_key = input(\"Enter your OpenWeatherMap API key: \")\n",
    "\n",
    "# Fetch weather\n",
    "weather_data = fetch_weather(city, api_key)\n",
    "\n",
    "# Analyze weather\n",
    "if weather_data:\n",
    "    analysis = analyze_weather(weather_data)\n",
    "    print(\"\\nWeather Analysis:\")\n",
    "    print(analysis)\n",
    "\n",
    "    # Save to file\n",
    "    log_weather(city, \"weather_log.csv\", api_key)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ffd3ce25",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
