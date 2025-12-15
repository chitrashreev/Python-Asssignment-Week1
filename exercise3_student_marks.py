{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "bd2cb7b1",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "❌ Input file not found. Please check the file name.\n"
     ]
    }
   ],
   "source": [
    "# Step 1: Import required library\n",
    "import numpy as np\n",
    "\n",
    "try:\n",
    "    # Step 2: Read data from input file\n",
    "    data = []\n",
    "    with open(\"input.txt\", \"r\") as file:\n",
    "        for line in file:\n",
    "            reg, exam, course = line.split()\n",
    "            data.append((reg, float(exam), float(course)))\n",
    "\n",
    "    # Step 3: Create structured NumPy array\n",
    "    students = np.array(\n",
    "        data,\n",
    "        dtype=[\n",
    "            (\"regno\", \"U10\"),\n",
    "            (\"exam\", \"f4\"),\n",
    "            (\"course\", \"f4\"),\n",
    "            (\"overall\", \"f4\"),\n",
    "            (\"grade\", \"U1\")\n",
    "        ]\n",
    "    )\n",
    "\n",
    "    # Step 4: Compute overall marks\n",
    "    students[\"overall\"] = students[\"exam\"] * 0.7 + students[\"course\"] * 0.3\n",
    "\n",
    "    # Step 5: Assign grades\n",
    "    for i in range(len(students)):\n",
    "        mark = students[\"overall\"][i]\n",
    "        if mark >= 70:\n",
    "            students[\"grade\"][i] = \"A\"\n",
    "        elif mark >= 60:\n",
    "            students[\"grade\"][i] = \"B\"\n",
    "        elif mark >= 50:\n",
    "            students[\"grade\"][i] = \"C\"\n",
    "        elif mark >= 40:\n",
    "            students[\"grade\"][i] = \"D\"\n",
    "        else:\n",
    "            students[\"grade\"][i] = \"F\"\n",
    "\n",
    "    # Step 6: Sort students by overall marks (descending)\n",
    "    students = np.sort(students, order=\"overall\")[::-1]\n",
    "\n",
    "    # Step 7: Write results to output file\n",
    "    with open(\"output.txt\", \"w\") as out:\n",
    "        out.write(\"RegNo  Exam  Course  Overall  Grade\\n\")\n",
    "        for s in students:\n",
    "            out.write(f\"{s['regno']}  {s['exam']}  {s['course']}  {s['overall']:.2f}  {s['grade']}\\n\")\n",
    "\n",
    "    # Step 8: Display grade statistics\n",
    "    print(\"\\nGrade Statistics:\")\n",
    "    grades, counts = np.unique(students[\"grade\"], return_counts=True)\n",
    "    for g, c in zip(grades, counts):\n",
    "        print(f\"Grade {g}: {c} students\")\n",
    "\n",
    "except FileNotFoundError:\n",
    "    print(\"❌ Input file not found. Please check the file name.\")\n",
    "\n",
    "except ValueError:\n",
    "    print(\"❌ Invalid data format in input file.\")\n",
    "\n",
    "except Exception as e:\n",
    "    print(\"❌ An unexpected error occurred:\", e)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b3725e69",
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
