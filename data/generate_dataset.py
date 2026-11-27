import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

np.random.seed(42)
random.seed(42)

# 1. Buat Dim_Branch (Tabel Dimensi Cabang)
branches = pd.DataFrame({
    'branch_id': ['BR-01', 'BR-02', 'BR-03', 'BR-04', 'BR-05'],
    'branch_name': ['Jakarta', 'Surabaya', 'Bandung', 'Medan', 'Semarang'],
    'region': ['Jabodetabek', 'Jawa Timur', 'Jawa Barat', 'Sumatera', 'Jawa Tengah']
})
branches.to_csv('dim_branch.csv', index=False)

# 2. Buat Dim_Vehicle (Tabel Dimensi Armada - sengaja dikotori)
vehicle_types = ['MPV - Avanza', 'Box Truck - Engkel', 'SUV - Innova', 'Blind Van - GranMax']
vehicles = []
for i in range(1, 51):
    v_id = f'VH-{i:03d}'
    v_type = random.choice(vehicle_types)
    # Sengaja buat penulisan status tidak konsisten & ada spasi
    status = random.choice(['Active', 'active ', 'ACTIVE', 'Maintenance', 'Inactive'])
    year = random.randint(2019, 2025)
    vehicles.append([v_id, v_type, status, year])

df_vehicles = pd.DataFrame(vehicles, columns=['vehicle_id', 'vehicle_type', 'status', 'manufacture_year'])
# Sengaja tambahkan 2 baris duplikat untuk latihan deduplikasi
df_vehicles = pd.concat([df_vehicles, df_vehicles.iloc[:2]], ignore_index=True)
df_vehicles.to_csv('dim_vehicle.csv', index=False)

# 3. Buat Fact_Operations (Tabel Fakta Operasional & Logistik - 1.500 baris)
start_date = datetime(2026, 1, 1)
records = []

for i in range(1, 1501):
    trip_id = f'TRP-{i:05d}'
    v_id = f'VH-{random.randint(1, 50):03d}'
    b_id = random.choice(['BR-01', 'BR-02', 'BR-03', 'BR-04', 'BR-05'])
    trip_date = (start_date + timedelta(days=random.randint(0, 300))).strftime('%Y-%m-%d')
    
    distance_km = round(random.uniform(25.0, 450.0), 1)
    # Sengaja buat 15 data jarak negatif (error sensor/input) untuk divalidasi
    if random.random() < 0.01:
        distance_km = -distance_km
        
    maintenance_cost = round(distance_km * random.uniform(800, 2200), 0) if random.random() < 0.25 else 0
    # Sengaja buat beberapa nilai kosong (NaN) pada biaya servis
    if random.random() < 0.02:
        maintenance_cost = np.nan
        
    target_hours = round(distance_km / 45.0, 1)
    actual_hours = round(target_hours * random.uniform(0.85, 1.35), 1)
    
    records.append([trip_id, trip_date, v_id, b_id, distance_km, maintenance_cost, target_hours, actual_hours])

df_fact = pd.DataFrame(records, columns=[
    'trip_id', 'trip_date', 'vehicle_id', 'branch_id', 
    'distance_km', 'maintenance_cost_idr', 'target_hours', 'actual_hours'
])
df_fact.to_csv('fact_operations.csv', index=False)
print("Berhasil membuat 3 file CSV!")