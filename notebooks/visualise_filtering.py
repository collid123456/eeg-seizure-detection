"""Visualise the effect of filtering on a real Bonn EEG signal."""

import matplotlib.pyplot as plt
import sys

sys.path.append("src")

from data.load_bonn import load_bonn_dataset
from preprocessing.filters import preprocess_signal

# Load the data
signals, labels = load_bonn_dataset()

# Grab one non-seizure signal and one seizure signal
non_seizure_signal = signals[0]  # first Z signal
seizure_signal = signals[100]  # first S signal (S starts at index 100)

# Filter both
non_seizure_filtered = preprocess_signal(non_seizure_signal)
seizure_filtered = preprocess_signal(seizure_signal)

# Plot: raw vs filtered, for both classes
fig, axes = plt.subplots(2, 2, figsize=(14, 8))

axes[0, 0].plot(non_seizure_signal, color="steelblue")
axes[0, 0].set_title("Non-seizure (Set Z) — Raw")

axes[0, 1].plot(non_seizure_filtered, color="steelblue")
axes[0, 1].set_title("Non-seizure (Set Z) — Filtered")

axes[1, 0].plot(seizure_signal, color="crimson")
axes[1, 0].set_title("Seizure (Set S) — Raw")

axes[1, 1].plot(seizure_filtered, color="crimson")
axes[1, 1].set_title("Seizure (Set S) — Filtered")

for ax in axes.flat:
    ax.set_xlabel("Sample")
    ax.set_ylabel("Amplitude")

plt.tight_layout()
plt.savefig("reports/figures/filtering_comparison.png", dpi=150)
print("Saved plot to reports/figures/filtering_comparison.png")
plt.show()
