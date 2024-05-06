{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "4fb046a5",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2024-05-06 12:44:38.074 WARNING streamlit.runtime.caching.cache_data_api: No runtime found, using MemoryCacheStorageManager\n",
      "2024-05-06 12:44:38.078 WARNING streamlit.runtime.caching.cache_data_api: No runtime found, using MemoryCacheStorageManager\n",
      "2024-05-06 12:44:38.080 WARNING streamlit.runtime.caching.cache_data_api: No runtime found, using MemoryCacheStorageManager\n",
      "2024-05-06 12:44:38.786 \n",
      "  \u001b[33m\u001b[1mWarning:\u001b[0m to view this Streamlit app on a browser, run it with the following\n",
      "  command:\n",
      "\n",
      "    streamlit run C:\\Program Files\\Anaconda\\Lib\\site-packages\\ipykernel_launcher.py [ARGUMENTS]\n",
      "2024-05-06 12:44:41.843 Session state does not function when running a script without `streamlit run`\n",
      "2024-05-06 12:44:41.845 Please replace `st.experimental_get_query_params` with `st.query_params`.\n",
      "\n",
      "`st.experimental_get_query_params` will be removed after 2024-04-11.\n",
      "\n",
      "Refer to our [docs page](https://docs.streamlit.io/library/api-reference/utilities/st.query_params) for more information.\n",
      "2024-05-06 12:44:41.849 No runtime found, using MemoryCacheStorageManager\n",
      "2024-05-06 12:44:41.870 No runtime found, using MemoryCacheStorageManager\n",
      "2024-05-06 12:44:42.458 No runtime found, using MemoryCacheStorageManager\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "DeltaGenerator()"
      ]
     },
     "execution_count": 1,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# -*- coding: utf-8 -*-\n",
    "# Copyright 2018-2022 Streamlit Inc.\n",
    "#\n",
    "# Licensed under the Apache License, Version 2.0 (the \"License\");\n",
    "# you may not use this file except in compliance with the License.\n",
    "# You may obtain a copy of the License at\n",
    "#\n",
    "#    http://www.apache.org/licenses/LICENSE-2.0\n",
    "#\n",
    "# Unless required by applicable law or agreed to in writing, software\n",
    "# distributed under the License is distributed on an \"AS IS\" BASIS,\n",
    "# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n",
    "# See the License for the specific language governing permissions and\n",
    "# limitations under the License.\n",
    "\n",
    "\"\"\"An example of showing geographic data.\"\"\"\n",
    "\n",
    "import os\n",
    "\n",
    "import altair as alt\n",
    "import numpy as np\n",
    "import pandas as pd\n",
    "import pydeck as pdk\n",
    "import streamlit as st\n",
    "\n",
    "# SETTING PAGE CONFIG TO WIDE MODE AND ADDING A TITLE AND FAVICON\n",
    "st.set_page_config(layout=\"wide\", page_title=\"NYC Ridesharing Demo\", page_icon=\":taxi:\")\n",
    "\n",
    "\n",
    "# LOAD DATA ONCE\n",
    "@st.cache_resource\n",
    "def load_data():\n",
    "    path = \"uber-raw-data-sep14.csv.gz\"\n",
    "    if not os.path.isfile(path):\n",
    "        path = f\"https://github.com/streamlit/demo-uber-nyc-pickups/raw/main/{path}\"\n",
    "\n",
    "    data = pd.read_csv(\n",
    "        path,\n",
    "        nrows=100000,  # approx. 10% of data\n",
    "        names=[\n",
    "            \"date/time\",\n",
    "            \"lat\",\n",
    "            \"lon\",\n",
    "        ],  # specify names directly since they don't change\n",
    "        skiprows=1,  # don't read header since names specified directly\n",
    "        usecols=[0, 1, 2],  # doesn't load last column, constant value \"B02512\"\n",
    "        parse_dates=[\n",
    "            \"date/time\"\n",
    "        ],  # set as datetime instead of converting after the fact\n",
    "    )\n",
    "\n",
    "    return data\n",
    "\n",
    "\n",
    "# FUNCTION FOR AIRPORT MAPS\n",
    "def map(data, lat, lon, zoom):\n",
    "    st.write(\n",
    "        pdk.Deck(\n",
    "            map_style=\"mapbox://styles/mapbox/light-v9\",\n",
    "            initial_view_state={\n",
    "                \"latitude\": lat,\n",
    "                \"longitude\": lon,\n",
    "                \"zoom\": zoom,\n",
    "                \"pitch\": 50,\n",
    "            },\n",
    "            layers=[\n",
    "                pdk.Layer(\n",
    "                    \"HexagonLayer\",\n",
    "                    data=data,\n",
    "                    get_position=[\"lon\", \"lat\"],\n",
    "                    radius=100,\n",
    "                    elevation_scale=4,\n",
    "                    elevation_range=[0, 1000],\n",
    "                    pickable=True,\n",
    "                    extruded=True,\n",
    "                ),\n",
    "            ],\n",
    "        )\n",
    "    )\n",
    "\n",
    "\n",
    "# FILTER DATA FOR A SPECIFIC HOUR, CACHE\n",
    "@st.cache_data\n",
    "def filterdata(df, hour_selected):\n",
    "    return df[df[\"date/time\"].dt.hour == hour_selected]\n",
    "\n",
    "\n",
    "# CALCULATE MIDPOINT FOR GIVEN SET OF DATA\n",
    "@st.cache_data\n",
    "def mpoint(lat, lon):\n",
    "    return (np.average(lat), np.average(lon))\n",
    "\n",
    "\n",
    "# FILTER DATA BY HOUR\n",
    "@st.cache_data\n",
    "def histdata(df, hr):\n",
    "    filtered = data[\n",
    "        (df[\"date/time\"].dt.hour >= hr) & (df[\"date/time\"].dt.hour < (hr + 1))\n",
    "    ]\n",
    "\n",
    "    hist = np.histogram(filtered[\"date/time\"].dt.minute, bins=60, range=(0, 60))[0]\n",
    "\n",
    "    return pd.DataFrame({\"minute\": range(60), \"pickups\": hist})\n",
    "\n",
    "\n",
    "# STREAMLIT APP LAYOUT\n",
    "data = load_data()\n",
    "\n",
    "# LAYING OUT THE TOP SECTION OF THE APP\n",
    "row1_1, row1_2 = st.columns((2, 3))\n",
    "\n",
    "# SEE IF THERE'S A QUERY PARAM IN THE URL (e.g. ?pickup_hour=2)\n",
    "# THIS ALLOWS YOU TO PASS A STATEFUL URL TO SOMEONE WITH A SPECIFIC HOUR SELECTED,\n",
    "# E.G. https://share.streamlit.io/streamlit/demo-uber-nyc-pickups/main?pickup_hour=2\n",
    "if not st.session_state.get(\"url_synced\", False):\n",
    "    try:\n",
    "        pickup_hour = int(st.experimental_get_query_params()[\"pickup_hour\"][0])\n",
    "        st.session_state[\"pickup_hour\"] = pickup_hour\n",
    "        st.session_state[\"url_synced\"] = True\n",
    "    except KeyError:\n",
    "        pass\n",
    "\n",
    "\n",
    "# IF THE SLIDER CHANGES, UPDATE THE QUERY PARAM\n",
    "def update_query_params():\n",
    "    hour_selected = st.session_state[\"pickup_hour\"]\n",
    "    st.experimental_set_query_params(pickup_hour=hour_selected)\n",
    "\n",
    "\n",
    "with row1_1:\n",
    "    st.title(\"NYC Uber Ridesharing Data\")\n",
    "    hour_selected = st.slider(\n",
    "        \"Select hour of pickup\", 0, 23, key=\"pickup_hour\", on_change=update_query_params\n",
    "    )\n",
    "\n",
    "\n",
    "with row1_2:\n",
    "    st.write(\n",
    "        \"\"\"\n",
    "    ##\n",
    "    Examining how Uber pickups vary over time in New York City's and at its major regional airports.\n",
    "    By sliding the slider on the left you can view different slices of time and explore different transportation trends.\n",
    "    \"\"\"\n",
    "    )\n",
    "\n",
    "# LAYING OUT THE MIDDLE SECTION OF THE APP WITH THE MAPS\n",
    "row2_1, row2_2, row2_3, row2_4 = st.columns((2, 1, 1, 1))\n",
    "\n",
    "# SETTING THE ZOOM LOCATIONS FOR THE AIRPORTS\n",
    "la_guardia = [40.7900, -73.8700]\n",
    "jfk = [40.6650, -73.7821]\n",
    "newark = [40.7090, -74.1805]\n",
    "zoom_level = 12\n",
    "midpoint = mpoint(data[\"lat\"], data[\"lon\"])\n",
    "\n",
    "with row2_1:\n",
    "    st.write(\n",
    "        f\"\"\"**All New York City from {hour_selected}:00 and {(hour_selected + 1) % 24}:00**\"\"\"\n",
    "    )\n",
    "    map(filterdata(data, hour_selected), midpoint[0], midpoint[1], 11)\n",
    "\n",
    "with row2_2:\n",
    "    st.write(\"**La Guardia Airport**\")\n",
    "    map(filterdata(data, hour_selected), la_guardia[0], la_guardia[1], zoom_level)\n",
    "\n",
    "with row2_3:\n",
    "    st.write(\"**JFK Airport**\")\n",
    "    map(filterdata(data, hour_selected), jfk[0], jfk[1], zoom_level)\n",
    "\n",
    "with row2_4:\n",
    "    st.write(\"**Newark Airport**\")\n",
    "    map(filterdata(data, hour_selected), newark[0], newark[1], zoom_level)\n",
    "\n",
    "# CALCULATING DATA FOR THE HISTOGRAM\n",
    "chart_data = histdata(data, hour_selected)\n",
    "\n",
    "# LAYING OUT THE HISTOGRAM SECTION\n",
    "st.write(\n",
    "    f\"\"\"**Breakdown of rides per minute between {hour_selected}:00 and {(hour_selected + 1) % 24}:00**\"\"\"\n",
    ")\n",
    "\n",
    "st.altair_chart(\n",
    "    alt.Chart(chart_data)\n",
    "    .mark_area(\n",
    "        interpolate=\"step-after\",\n",
    "    )\n",
    "    .encode(\n",
    "        x=alt.X(\"minute:Q\", scale=alt.Scale(nice=False)),\n",
    "        y=alt.Y(\"pickups:Q\"),\n",
    "        tooltip=[\"minute\", \"pickups\"],\n",
    "    )\n",
    "    .configure_mark(opacity=0.2, color=\"red\"),\n",
    "    use_container_width=True,\n",
    ")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ad132786",
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