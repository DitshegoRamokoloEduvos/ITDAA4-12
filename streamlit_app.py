{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "85f0d9cb",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2024-05-06 11:49:13.314 \n",
      "  \u001b[33m\u001b[1mWarning:\u001b[0m to view this Streamlit app on a browser, run it with the following\n",
      "  command:\n",
      "\n",
      "    streamlit run C:\\Program Files\\Anaconda\\Lib\\site-packages\\ipykernel_launcher.py [ARGUMENTS]\n"
     ]
    }
   ],
   "source": [
    "# Import necessary libraries\n",
    "import streamlit as st\n",
    "import pandas as pd\n",
    "import numpy as np\n",
    "import matplotlib.pyplot as plt\n",
    "\n",
    "# Generate random data\n",
    "np.random.seed(42)\n",
    "n_points = 100\n",
    "x_values = np.random.rand(n_points)\n",
    "y_values = np.random.rand(n_points)\n",
    "\n",
    "# Create a DataFrame\n",
    "df = pd.DataFrame({\"X\": x_values, \"Y\": y_values})\n",
    "\n",
    "# Streamlit app layout\n",
    "st.title(\"Random Scatter Plot\")\n",
    "st.write(\"This is a simple Streamlit app that displays a scatter plot.\")\n",
    "\n",
    "# Display the scatter plot\n",
    "st.scatter_chart(df)\n",
    "\n",
    "# Add some additional content\n",
    "st.write(\"Feel free to customize this app by adding more components, charts, or interactive elements!\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1325d682",
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
