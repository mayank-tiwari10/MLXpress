"""Create Time Series Data"""
# Create time series data from a list
data_list = [10, 20, 30, 40, 50]
ts_from_list = create_time_series(data_list)
print("Time series from list:")
print(ts_from_list)

# Create time series data from a numpy array with custom index
data_array = np.array([1, 2, 3, 4, 5])
custom_index = pd.date_range(start='2024-01-01', periods=len(data_array), freq='D')
ts_from_array = create_time_series(data_array, index=custom_index)
print("\nTime series from numpy array with custom index:")
print(ts_from_array)

# Create time series data from a pandas DataFrame
data_df = pd.DataFrame({'values': [100, 200, 300, 400], 'date': pd.date_range(start='2024-01-01', periods=4)})
ts_from_df = create_time_series(data_df.set_index('date')['values'])
print("\nTime series from DataFrame:")
print(ts_from_df)


"""Time Indexing Operations"""
# Perform time indexing
start_time = '2024-01-03'
end_time = '2024-01-07'
sliced_time_series = time_indexing(time_series, start_time, end_time)
print("\nSliced time series from {} to {}:".format(start_time, end_time))
print(sliced_time_series)


"""Resampling and Aggregation"""
# Create a sample daily time series data
date_range = pd.date_range(start='2024-01-01', periods=10, freq='D')
data = [i for i in range(10)]
time_series = pd.Series(data, index=date_range)
print("Original time series (daily):")
print(time_series)

# Resample and aggregate the time series to monthly frequency using mean aggregation
resampled_time_series = resample_and_aggregate(time_series, frequency='M', method='mean')
print("\nResampled time series (monthly, mean aggregation):")
print(resampled_time_series)


"""Time Shift"""
# Create a sample time series data
date_range = pd.date_range(start='2024-01-01', periods=5, freq='D')
data = [i for i in range(5)]
time_series = pd.Series(data, index=date_range)
print("Original time series:")
print(time_series)

# Shift the time series data forward by 2 periods
shifted_time_series = time_shift(time_series, periods=2)
print("\nShifted time series (forward by 2 periods):")
print(shifted_time_series)

# Shift the time series data backward by 1 period with hourly frequency
shifted_time_series_hourly = time_shift(time_series, periods=-1, freq='H')
print("\nShifted time series (backward by 1 period with hourly frequency):")
print(shifted_time_series_hourly)


"""Rolling Statistics"""
# Create a sample time series data
date_range = pd.date_range(start='2024-01-01', periods=10, freq='D')
data = [i for i in range(10)]
time_series = pd.Series(data, index=date_range)
print("Original time series:")
print(time_series)

# Calculate the 3-period moving average
moving_average = calculate_rolling_statistics(time_series, window=3)
print("\n3-period Moving Average:")
print(moving_average)

# Calculate the 4-period rolling standard deviation
rolling_std = calculate_rolling_statistics(time_series, window=4, statistic='std')
print("\n4-period Rolling Standard Deviation:")
print(rolling_std)


"""Time Series Analysis"""
# Create a sample time series data
date_range = pd.date_range(start='2024-01-01', periods=100, freq='D')
data = [i + 10 * (i // 20) for i in range(100)]  # Trend + Seasonality
time_series = pd.Series(data, index=date_range)
print("Original time series:")
print(time_series)

# Perform time series analysis
analysis_results = time_series_analysis(time_series)
print("\nStatistical Analysis Results:")
for key, value in analysis_results.items():
    print(f"{key}: {value}")

"""Handling Missing Data"""
# Create a sample time series data with missing values
date_range = pd.date_range(start='2024-01-01', periods=10, freq='D')
data = [1, 2, None, 4, None, 6, 7, None, 9, None]
time_series = pd.Series(data, index=date_range)
print("Original time series with missing values:")
print(time_series)

# Handle missing data using interpolation
filled_time_series = handle_missing_data(time_series, method='interpolate')
print("\nTime series with missing data filled using interpolation:")
print(filled_time_series)

# Handle missing data using forward fill
filled_time_series_ffill = handle_missing_data(time_series, method='ffill')
print("\nTime series with missing data filled using forward fill:")
print(filled_time_series_ffill)

# Handle missing data using backward fill
filled_time_series_bfill = handle_missing_data(time_series, method='bfill')
print("\nTime series with missing data filled using backward fill:")
print(filled_time_series_bfill)


"""Outlier Detection"""
# Create a sample time series data with outliers
date_range = pd.date_range(start='2024-01-01', periods=100, freq='D')
data = [i + 10 * (i // 20) for i in range(100)]  # Trend + Seasonality
# Introduce outliers
data[5] = 100
data[20] = -50
data[60] = 150
time_series = pd.Series(data, index=date_range)
print("Original time series:")
print(time_series)

# Detect outliers using z-score method
outliers = detect_outliers(time_series)
print("\nOutlier detection using z-score method:")
print(outliers)

# Remove outliers
filtered_series = detect_outliers(time_series, remove_outliers=True)
print("\nTime series with outliers removed:")
print(filtered_series)


"""ForeCasting"""
# Example usage:
# Create a sample time series data
date_range = pd.date_range(start='2024-01-01', periods=100, freq='D')
data = [i + 10 * (i // 20) for i in range(100)]  # Trend + Seasonality
time_series = pd.Series(data, index=date_range)
print("Original time series:")
print(time_series)

# Perform time series forecasting using naive method
forecast_steps = 10
forecast_series = time_series_forecast(time_series, steps=forecast_steps)
print(f"\nForecasted values for the next {forecast_steps} steps:")
print(forecast_series)
