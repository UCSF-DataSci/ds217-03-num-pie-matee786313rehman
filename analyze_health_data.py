#!/usr/bin/env python3
"""
Health Sensor Data Analysis Script

Complete the TODO sections to analyze health sensor data using NumPy.
This script demonstrates basic NumPy operations for data loading, statistics,
filtering, and report generation.
"""

import numpy as np


def load_data(filename):
    """Load CSV data using NumPy.
    
    Args:
        filename: Path to CSV file
        
    Returns:
        NumPy structured array with all columns
    """
    # This code is provided because np.genfromtxt() is not covered in the lecture
    dtype = [('patient_id', 'U10'), ('timestamp', 'U20'), 
             ('heart_rate', 'i4'), ('blood_pressure_systolic', 'i4'),
             ('blood_pressure_diastolic', 'i4'), ('temperature', 'f4'),
             ('glucose_level', 'i4'), ('sensor_id', 'U10')]
    
    data = np.genfromtxt(filename, delimiter=',', dtype=dtype, skip_header=1)
    return data


def calculate_statistics(data):
    """Calculate basic statistics for numeric columns.
    
    Args:
        data: NumPy structured array
        
    Returns:
        Dictionary with statistics
    """
    # Calculate averages for requested numeric fields
    avg_heart_rate = float(data['heart_rate'].mean())
    avg_systolic_bp = float(data['blood_pressure_systolic'].mean())
    avg_glucose = float(data['glucose_level'].mean())

    return {
        'avg_heart_rate': avg_heart_rate,
        'avg_systolic_bp': avg_systolic_bp,
        'avg_glucose': avg_glucose
    }


def find_abnormal_readings(data):
    """Find readings with abnormal values.
    
    Args:
        data: NumPy structured array
        
    Returns:
        Dictionary with counts
    """
    # Use boolean indexing and sum to count True values
    high_hr_count = int((data['heart_rate'] > 90).sum())
    high_bp_count = int((data['blood_pressure_systolic'] > 130).sum())
    high_glucose_count = int((data['glucose_level'] > 110).sum())

    return {
        'high_heart_rate': high_hr_count,
        'high_blood_pressure': high_bp_count,
        'high_glucose': high_glucose_count
    }


def generate_report(stats, abnormal, total_readings):
    """Generate formatted analysis report.
    
    Args:
        stats: Dictionary of statistics
        abnormal: Dictionary of abnormal counts
        total_readings: Total number of readings
        
    Returns:
        Formatted string report
    """
    report_lines = []
    report_lines.append("Health Sensor Data Analysis Report")
    report_lines.append("==================================")
    report_lines.append("")
    report_lines.append("Dataset Summary:")
    report_lines.append(f"- Total readings: {total_readings}")
    report_lines.append("")
    report_lines.append("Average Measurements:")
    report_lines.append(f"- Heart Rate: {stats['avg_heart_rate']:.1f} bpm")
    report_lines.append(f"- Systolic BP: {stats['avg_systolic_bp']:.1f} mmHg")
    report_lines.append(f"- Glucose Level: {stats['avg_glucose']:.1f} mg/dL")
    report_lines.append("")
    report_lines.append("Abnormal Readings:")
    # Add raw counts and percentages
    hr_pct = (abnormal['high_heart_rate'] / total_readings) * 100 if total_readings else 0
    bp_pct = (abnormal['high_blood_pressure'] / total_readings) * 100 if total_readings else 0
    gl_pct = (abnormal['high_glucose'] / total_readings) * 100 if total_readings else 0

    report_lines.append(f"- High Heart Rate (>90): {abnormal['high_heart_rate']} readings ({hr_pct:.1f}%)")
    report_lines.append(f"- High Blood Pressure (>130): {abnormal['high_blood_pressure']} readings ({bp_pct:.1f}%)")
    report_lines.append(f"- High Glucose (>110): {abnormal['high_glucose']} readings ({gl_pct:.1f}%)")

    return "\n".join(report_lines)


def save_report(report, filename):
    """Save report to file.
    
    Args:
        report: Report string
        filename: Output filename
    """
    # Ensure output directory exists
    import os
    outdir = os.path.dirname(filename)
    if outdir and not os.path.exists(outdir):
        os.makedirs(outdir, exist_ok=True)

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(report)


def main():
    """Main execution function."""
    # Orchestrate the analysis pipeline
    data_file = 'health_data.csv'
    report_file = 'output/analysis_report.txt'

    data = load_data(data_file)
    stats = calculate_statistics(data)
    abnormal = find_abnormal_readings(data)
    total_readings = len(data)
    report = generate_report(stats, abnormal, total_readings)
    save_report(report, report_file)

    print(f"\n✓ Analysis complete. Report saved to: {report_file}")


if __name__ == "__main__":
    main()