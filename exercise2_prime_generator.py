{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "fc87dd6e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter range start (positive integer): 1\n",
      "Enter range end (positive integer): 9\n",
      "\n",
      "Prime numbers in the given range:\n",
      "\n",
      "    2     3     5     7 "
     ]
    }
   ],
   "source": [
    "# Step 1: Define a function to check prime number\n",
    "def is_prime(num):\n",
    "    if num <= 1:\n",
    "        return False\n",
    "    for i in range(2, int(num ** 0.5) + 1):\n",
    "        if num % i == 0:\n",
    "            return False\n",
    "    return True\n",
    "\n",
    "\n",
    "try:\n",
    "    # Step 2: Take input from user\n",
    "    start = int(input(\"Enter range start (positive integer): \"))\n",
    "    end = int(input(\"Enter range end (positive integer): \"))\n",
    "\n",
    "    # Step 3: Validate input\n",
    "    if start <= 0 or end <= 0:\n",
    "        raise ValueError(\"Numbers must be positive\")\n",
    "\n",
    "    if start > end:\n",
    "        start, end = end, start  # swap if order is wrong\n",
    "\n",
    "    print(\"\\nPrime numbers in the given range:\\n\")\n",
    "\n",
    "    count = 0  # to print 10 numbers per line\n",
    "\n",
    "    # Step 4: Find prime numbers in range\n",
    "    for num in range(start, end + 1):\n",
    "        if is_prime(num):\n",
    "            print(f\"{num:5}\", end=\" \")\n",
    "            count += 1\n",
    "\n",
    "            # Step 5: Print 10 numbers per line\n",
    "            if count % 10 == 0:\n",
    "                print()\n",
    "\n",
    "    if count == 0:\n",
    "        print(\"No prime numbers found in this range.\")\n",
    "\n",
    "except ValueError:\n",
    "    # Step 6: Handle invalid input\n",
    "    print(\"❌ Invalid input! Please enter only positive integers.\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0abce892",
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
