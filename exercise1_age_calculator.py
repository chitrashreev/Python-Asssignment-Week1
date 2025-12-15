{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "2741e7fd",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter your birth date (mm/dd/yyyy): 08/22/2002\n",
      "\n",
      "--- Age Calculator Result ---\n",
      "Your age is: 23 years\n",
      "Birth date (European format): 22/08/2002\n"
     ]
    }
   ],
   "source": [
    "# Step 1: Import required modules\n",
    "from datetime import datetime, date\n",
    "\n",
    "try:\n",
    "    # Step 2: Ask user to enter birth date\n",
    "    birth_input = input(\"Enter your birth date (mm/dd/yyyy): \")\n",
    "\n",
    "    # Step 3: Validate input format and convert to date\n",
    "    birth_date = datetime.strptime(birth_input, \"%m/%d/%Y\").date()\n",
    "\n",
    "    # Step 4: Get today's date\n",
    "    today = date.today()\n",
    "\n",
    "    # Step 5: Calculate age in years\n",
    "    age = today.year - birth_date.year\n",
    "\n",
    "    # Adjust age if birthday hasn't occurred this year\n",
    "    if (today.month, today.day) < (birth_date.month, birth_date.day):\n",
    "        age -= 1\n",
    "\n",
    "    # Step 6: Convert birth date to European format (dd/mm/yyyy)\n",
    "    european_format = birth_date.strftime(\"%d/%m/%Y\")\n",
    "\n",
    "    # Step 7: Display results\n",
    "    print(\"\\n--- Age Calculator Result ---\")\n",
    "    print(\"Your age is:\", age, \"years\")\n",
    "    print(\"Birth date (European format):\", european_format)\n",
    "\n",
    "except ValueError:\n",
    "    # Step 8: Handle invalid input errors\n",
    "    print(\"❌ Invalid date format or invalid date.\")\n",
    "    print(\"Please enter date in mm/dd/yyyy format (Example: 08/25/2001)\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "426ad50b",
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
