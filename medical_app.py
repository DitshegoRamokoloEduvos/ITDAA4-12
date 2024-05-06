{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "360fb2e0",
   "metadata": {},
   "outputs": [],
   "source": [
    "import os\n",
    "\n",
    "os.environ[\"KERAS_BACKEND\"] = \"tensorflow\"\n",
    "\n",
    "import streamlit as st\n",
    "import tensorflow as tf\n",
    "import keras\n",
    "import numpy as np"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "1a09bce2",
   "metadata": {},
   "outputs": [
    {
     "ename": "ValueError",
     "evalue": "File not found: filepath=C:\\Users\\Ditshego.Ramokolo\\medical_app.keras. Please ensure the file is an accessible `.keras` zip file.",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mValueError\u001b[0m                                Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[16], line 1\u001b[0m\n\u001b[1;32m----> 1\u001b[0m model \u001b[38;5;241m=\u001b[39m  keras\u001b[38;5;241m.\u001b[39mmodels\u001b[38;5;241m.\u001b[39mload_model(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mC:\u001b[39m\u001b[38;5;130;01m\\\\\u001b[39;00m\u001b[38;5;124mUsers\u001b[39m\u001b[38;5;130;01m\\\\\u001b[39;00m\u001b[38;5;124mDitshego.Ramokolo\u001b[39m\u001b[38;5;130;01m\\\\\u001b[39;00m\u001b[38;5;124mmedical_app.keras\u001b[39m\u001b[38;5;124m\"\u001b[39m)\n",
      "File \u001b[1;32mC:\\Program Files\\Anaconda\\Lib\\site-packages\\keras\\src\\saving\\saving_api.py:187\u001b[0m, in \u001b[0;36mload_model\u001b[1;34m(filepath, custom_objects, compile, safe_mode)\u001b[0m\n\u001b[0;32m    183\u001b[0m     \u001b[38;5;28;01mreturn\u001b[39;00m legacy_h5_format\u001b[38;5;241m.\u001b[39mload_model_from_hdf5(\n\u001b[0;32m    184\u001b[0m         filepath, custom_objects\u001b[38;5;241m=\u001b[39mcustom_objects, \u001b[38;5;28mcompile\u001b[39m\u001b[38;5;241m=\u001b[39m\u001b[38;5;28mcompile\u001b[39m\n\u001b[0;32m    185\u001b[0m     )\n\u001b[0;32m    186\u001b[0m \u001b[38;5;28;01melif\u001b[39;00m \u001b[38;5;28mstr\u001b[39m(filepath)\u001b[38;5;241m.\u001b[39mendswith(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m.keras\u001b[39m\u001b[38;5;124m\"\u001b[39m):\n\u001b[1;32m--> 187\u001b[0m     \u001b[38;5;28;01mraise\u001b[39;00m \u001b[38;5;167;01mValueError\u001b[39;00m(\n\u001b[0;32m    188\u001b[0m         \u001b[38;5;124mf\u001b[39m\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mFile not found: filepath=\u001b[39m\u001b[38;5;132;01m{\u001b[39;00mfilepath\u001b[38;5;132;01m}\u001b[39;00m\u001b[38;5;124m. \u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m    189\u001b[0m         \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mPlease ensure the file is an accessible `.keras` \u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m    190\u001b[0m         \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mzip file.\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m    191\u001b[0m     )\n\u001b[0;32m    192\u001b[0m \u001b[38;5;28;01melse\u001b[39;00m:\n\u001b[0;32m    193\u001b[0m     \u001b[38;5;28;01mraise\u001b[39;00m \u001b[38;5;167;01mValueError\u001b[39;00m(\n\u001b[0;32m    194\u001b[0m         \u001b[38;5;124mf\u001b[39m\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mFile format not supported: filepath=\u001b[39m\u001b[38;5;132;01m{\u001b[39;00mfilepath\u001b[38;5;132;01m}\u001b[39;00m\u001b[38;5;124m. \u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m    195\u001b[0m         \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mKeras 3 only supports V3 `.keras` files and \u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[1;32m   (...)\u001b[0m\n\u001b[0;32m    204\u001b[0m         \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmight have a different name).\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m    205\u001b[0m     )\n",
      "\u001b[1;31mValueError\u001b[0m: File not found: filepath=C:\\Users\\Ditshego.Ramokolo\\medical_app.keras. Please ensure the file is an accessible `.keras` zip file."
     ]
    }
   ],
   "source": [
    "model =  keras.models.load_model(\"C:\\\\Users\\\\Ditshego.Ramokolo\\\\medical_app.keras\")  # Replace with your model's path"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "40fc8c17",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2024-05-06 11:38:49.444 \n",
      "  \u001b[33m\u001b[1mWarning:\u001b[0m to view this Streamlit app on a browser, run it with the following\n",
      "  command:\n",
      "\n",
      "    streamlit run C:\\Program Files\\Anaconda\\Lib\\site-packages\\ipykernel_launcher.py [ARGUMENTS]\n",
      "2024-05-06 11:38:49.448 Session state does not function when running a script without `streamlit run`\n"
     ]
    }
   ],
   "source": [
    "st.title(\"Medical Practitioner Model\")\n",
    "\n",
    "# Input widgets for user data (replace with your model's input requirements)\n",
    "age = st.number_input(\"Age\", min_value=18, max_value=120)\n",
    "gender = st.selectbox(\"Gender\", [\"Male\", \"Female\"])\n",
    "# Add more widgets as needed based on your model's input features\n",
    "\n",
    "# Button to trigger prediction\n",
    "if st.button(\"Predict\"):\n",
    "    # Preprocess user input if necessary\n",
    "    processed_data = [age, gender]  # Example preprocessing\n",
    "\n",
    "    # Make prediction using the loaded model\n",
    "    prediction = model.predict(processed_data)\n",
    "\n",
    "    # Display prediction results\n",
    "    st.write(\"Prediction:\", prediction)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "45c8d350",
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
