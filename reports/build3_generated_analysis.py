import argparse
import pandas as pd
import matplotlib.pyplot as plt
import os

def main(data_file, report_dir):
    # Load the dataset
    df = pd.read_csv(data_file)

    # Validate column names
    required_columns = ['Date', 'Revenue ($B)']
    for col in required_columns:
        if col not in df.columns:
            raise ValueError(f"Missing required column: {col}")

    # Handle missing values
    df['Revenue ($B)'].fillna(df['Revenue ($B)'].mean(), inplace=True)

    # Convert 'Date' to datetime
    df['Date'] = pd.to_datetime(df['Date'])

    # Create a line plot of Revenue over Date
    plt.figure(figsize=(12, 6))
    plt.plot(df['Date'], df['Revenue ($B)'], marker='o', linestyle='-')
    plt.title('Revenue Over Time')
    plt.xlabel('Date')
    plt.ylabel('Revenue ($B)')
    plt.grid()
    
    # Save the plot
    output_file = os.path.join(report_dir, 'revenue_over_time.png')
    plt.savefig(output_file)
    plt.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process financial data.')
    parser.add_argument('--data', required=True, help='Path to the input data file (CSV)')
    parser.add_argument('--report_dir', required=True, help='Directory to save the report')
    args = parser.parse_args()
    
    main(args.data, args.report_dir)