{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "9f1f07b7",
   "metadata": {},
   "outputs": [
    {
     "ename": "ModuleNotFoundError",
     "evalue": "No module named 'streamlit'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mModuleNotFoundError\u001b[0m                       Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[1], line 1\u001b[0m\n\u001b[1;32m----> 1\u001b[0m \u001b[38;5;28;01mimport\u001b[39;00m \u001b[38;5;21;01mstreamlit\u001b[39;00m \u001b[38;5;28;01mas\u001b[39;00m \u001b[38;5;21;01mst\u001b[39;00m\n\u001b[0;32m      4\u001b[0m \u001b[38;5;28;01mdef\u001b[39;00m \u001b[38;5;21mcalculate_sum\u001b[39m(n1, n2):\n\u001b[0;32m      5\u001b[0m     \u001b[38;5;28;01mreturn\u001b[39;00m n1 \u001b[38;5;241m+\u001b[39m n2\n",
      "\u001b[1;31mModuleNotFoundError\u001b[0m: No module named 'streamlit'"
     ]
    }
   ],
   "source": [
    "import streamlit as st\n",
    "\n",
    "\n",
    "def calculate_sum(n1, n2):\n",
    "    return n1 + n2\n",
    "\n",
    "\n",
    "st.title(\"Add numbers\")\n",
    "\n",
    "n1 = st.number_input(\"First Number\")\n",
    "n2 = st.number_input(\"Second Number\")\n",
    "\n",
    "if st.button(\"Calculate\"):\n",
    "    st.write(\"Summation is: \" + str(calculate_sum(n1, n2)))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d7f74c58",
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
