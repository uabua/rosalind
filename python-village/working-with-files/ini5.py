"""
My soulution to Rosalind problem 'Working with Files'

ID: INI5
Title: Working with Files
URL: http://rosalind.info/problems/ini5/
"""

dataset_path = ""

with open(dataset_path, "r") as dataset:
    data = dataset.readlines()

file_path = ""

with open (file_path, "a") as file:
    for index in range(1, len(data), 2):
        file.write(data[index])
