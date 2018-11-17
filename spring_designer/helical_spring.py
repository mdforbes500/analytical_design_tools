#!/usr/bin/env python3

import sqlite3

print('Connecting to database...')
conn = sqlite3.connect('../tables/test.dB')
print('Connection successful!')

cursor = conn.execute('''
select material, exponent, A_metric from table10_4
''')
material = cursor.fetchone()

print(material[0])
