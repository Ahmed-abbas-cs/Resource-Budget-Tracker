import pandas as pd
import random
from datetime import datetime, timedelta

# Define the core variables for the project
materials = ['Cement (Bags)', 'Steel (Tons)', 'Sand (Trucks)', 'Wood (Pallets)', 'Bricks (Pallets)']
contractors = ['Contractor A', 'Contractor B', 'Contractor C']
statuses = ['Used', 'Used', 'Used', 'Wasted', 'Pending'] # 'Used' is repeated to make it the most frequent status

data = []
start_date = datetime(2026, 1, 1)

# Generate 500 rows of mock data
for _ in range(500):
    order_date = start_date + timedelta(days=random.randint(0, 150))
    material = random.choice(materials)
    quantity = random.randint(10, 100)
    unit_price = random.randint(50, 500)
    contractor = random.choice(contractors)
    status = random.choice(statuses)
    
    data.append([order_date.strftime('%Y-%m-%d'), material, quantity, unit_price, contractor, status])

# Convert the generated data into a pandas DataFrame
df = pd.DataFrame(data, columns=['Order Date', 'Material Type', 'Quantity', 'Unit Price', 'Contractor', 'Status'])

# Export the DataFrame to a CSV file
df.to_csv('Construction_Materials_Log.csv', index=False)
print("Dataset generated successfully!")