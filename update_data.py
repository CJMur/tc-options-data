import pandas as pd

OPTIONS_SHEET_URL = "https://docs.google.com/spreadsheets/d/1d9FQ5mn--MSNJ_WJkU--IvoSRU0gQBqE0f9s9zEb0Q4/export?format=csv&gid=0"
FWD_CURVE_URL = "https://docs.google.com/spreadsheets/d/1d9FQ5mn--MSNJ_WJkU--IvoSRU0gQBqE0f9s9zEb0Q4/export?format=csv&gid=861426630"

print("Fetching Options Data from Google...")
df_opts = pd.read_csv(OPTIONS_SHEET_URL, dtype=str, on_bad_lines='skip')
df_opts.to_parquet('options_data.parquet', engine='pyarrow', index=False)

print("Fetching Forward Curve from Google...")
df_fwd = pd.read_csv(FWD_CURVE_URL, dtype=str, on_bad_lines='skip')
df_fwd.to_parquet('fwd_curve.parquet', engine='pyarrow', index=False)

print("Successfully generated Parquet files!")
