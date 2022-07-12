{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d2974075",
   "metadata": {},
   "outputs": [],
   "source": [
    "import csv\n",
    "import os\n",
    "\n",
    "csvpath = os.path.join(\"Resources\",\"budget_data.csv\")\n",
    "\n",
    "with open(csvpath) as csvfile:\n",
    "    csvreader = csv.reader(csvfile, delimiter = \",\")\n",
    "    csv_header = next(csvreader,None)\n",
    "  \n",
    "\n",
    "    monthcount = []\n",
    "    pnl_list = []\n",
    "    pnl_change = []\n",
    "    for row in csvreader:\n",
    "        monthcount.append(row[0])\n",
    "        pnl_list.append(int(row[1]))\n",
    "        \n",
    "    for i in range(1,len(pnl_list)):\n",
    "        change = int(pnl_list[i] - pnl_list[i-1])\n",
    "        pnl_change.append(int(change))\n",
    "        \n",
    "    total_months = len(monthcount)\n",
    "    pnl_total = sum(pnl_list)\n",
    "    change_total = 0\n",
    "    \n",
    "    for i in range(len(pnl_change)):\n",
    "        change_total = change_total + float(pnl_change[i])\n",
    "    \n",
    "    greatest_increase = max(pnl_change)\n",
    "    greatest_decrease = min(pnl_change)\n",
    "    \n",
    "    max_month_index = pnl_change.index(max(pnl_change))\n",
    "    max_month = monthcount[max_month_index+1]\n",
    "\n",
    "    min_month_index = pnl_change.index(min(pnl_change))\n",
    "    min_month = monthcount[min_month_index+1]\n",
    "\n",
    "    pnl_average = round(change_total / len(pnl_change),2)\n",
    "\n",
    "    print(\"Financial Analysis\")\n",
    "    print(\"--------------------------------------\")\n",
    "    print(f\"Total Months: {total_months}\")\n",
    "    print(f\"Total Profits/Losses: ${pnl_total}\")\n",
    "    print(f\"Average Change: ${pnl_average}\")\n",
    "    print(f\"Greatest Increase in Profits: {max_month} (${greatest_increase})\")\n",
    "    print(f\"Greatest Decrease in Profits: {min_month} (${greatest_decrease})\")\n",
    "\n",
    "output_path = os.path.join(\"Analysis\",\"analysis.txt\")\n",
    "\n",
    "analysis = open(output_path, \"w\")\n",
    "    \n",
    "analysis.write(\"Financial Analysis\\n\")\n",
    "analysis.write(\"---------------------\\n\")\n",
    "analysis.write(f\"Total Months: {total_months}\\n\")\n",
    "analysis.write(f\"Total Profits/Losses: ${pnl_total}\\n\")\n",
    "analysis.write(f\"Average Change: ${pnl_average}\\n\")\n",
    "analysis.write(f\"Greatest Increase in Profits: {max_month} (${greatest_increase})\\n\")\n",
    "analysis.write(f\"Greatest Decrease in Profits: {min_month} (${greatest_decrease})\\n\")\n",
    "analysis.close()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9307258c",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "PythonData",
   "language": "python",
   "name": "pythondata"
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
   "version": "3.9.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
