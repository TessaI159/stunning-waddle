# stunning-waddle
Simple script to benchmark languages against each other.

Call compare.py <filname_without_extension> <num_loops> [<extension> <interpreter> ... ]

Example:
python compare.py coin_values 100 py python3 rb ruby ms MiniScript\

This will compare the average runtime over 100 runs of coin_values.rb, coin_values.py, and coin_values.ms
The output is ordered based on speed from highest to lowest.
