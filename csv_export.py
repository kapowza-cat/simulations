import csv

def export_to_csv(filename, *arrays):
    # Ensure all arrays are the same length
    length = len(arrays[0])
    if not all(len(arr) == length for arr in arrays):
        raise ValueError("All arrays must have the same length.")

    # Write rows to CSV
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        for i in range(length):
            row = [arr[i] for arr in arrays]
            writer.writerow(row)
