import numpy as np
import os
import sys

# Ensure project root is on sys.path so tests can import local modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from analyze_health_data import calculate_statistics, find_abnormal_readings


def make_test_array():
    dtype = [('patient_id', 'U10'), ('timestamp', 'U20'),
             ('heart_rate', 'i4'), ('blood_pressure_systolic', 'i4'),
             ('blood_pressure_diastolic', 'i4'), ('temperature', 'f4'),
             ('glucose_level', 'i4'), ('sensor_id', 'U10')]

    data = np.array([
        ('P00001', '2024-01-01T00:00:00', 80, 120, 80, 98.6, 100, 'S001'),
        ('P00002', '2024-01-01T01:00:00', 95, 135, 85, 99.0, 120, 'S002'),
        ('P00003', '2024-01-01T02:00:00', 70, 110, 75, 97.5, 90, 'S003'),
    ], dtype=dtype)
    return data


def test_calculate_statistics():
    data = make_test_array()
    stats = calculate_statistics(data)

    assert round(stats['avg_heart_rate'], 1) == round((80 + 95 + 70) / 3, 1)
    assert round(stats['avg_systolic_bp'], 1) == round((120 + 135 + 110) / 3, 1)
    assert round(stats['avg_glucose'], 1) == round((100 + 120 + 90) / 3, 1)


def test_find_abnormal_readings():
    data = make_test_array()
    abnormal = find_abnormal_readings(data)

    # heart rate > 90: one reading (95)
    assert abnormal['high_heart_rate'] == 1
    # systolic BP > 130: one reading (135)
    assert abnormal['high_blood_pressure'] == 1
    # glucose > 110: one reading (120)
    assert abnormal['high_glucose'] == 1
