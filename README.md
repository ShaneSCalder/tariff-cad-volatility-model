

# tariff-cad-volatility-model
This repository contains a simple Python-based simulation tool for projecting potential changes in the Canadian Dollar (CAD) exchange rate under various tariff and recovery scenarios. Using a combination of parameterized uncertainties (initial drop and post-recovery), the model generates a distribution of possible CAD/USD outcomes and visualizes the results in a histogram.

---

![volCad](https://github.com/user-attachments/assets/a15f9e9e-3f46-4e7e-922b-adc0f28db71b)

---

# Overview
In periods of heightened trade tensions—such as potential U.S. tariff implementations—currency fluctuations can pose significant risks for businesses and policymakers. This simulation provides a straightforward way to assess how multiple factors (tariff severity, market uncertainties, and recovery assumptions) might combine to influence the CAD/USD exchange rate.

The approach uses a simple uniform sampling around mean drop and recovery values, applies a severity_factor for scaling, and visualizes the resulting distribution of possible post-recovery exchange rates.

---

# Features
Parameter-based Simulation: Adjust current_rate, initial_drop_mean, recovery_mean, and severity_factor to explore different scenarios.
Uncertainty Modeling: Samples from uniform distributions to represent the range of plausible outcomes around the means.
Histogram Visualization: Quickly see the distribution of simulated CAD rates, including the original (current) rate for comparison.
Saveable Plot: Outputs the histogram as a PNG file for easy sharing or reporting.

--- 

# Dependencies
Python 3.7+ (the code should work on Python 3.7 and above)
NumPy (for numerical computations)
Matplotlib (for plotting the histogram)

You can install the dependencies using:

```
pip install numpy matplotlib
```

---

# Files
currency.py & currency.ipynb
- A standalone Python script that runs the simulation and saves the resulting histogram as simulated_cad_rates.png. (currency.py)
- Jupyter Notebook (currency.ipynb)
A notebook version of the code for interactive exploration. You can run code cells step by step and modify parameters on the fly.

---

# Ussage 

## Python Script 
Run the Script:

``` 
python currency.py
``` 

- This script will generate a histogram of post-recovery CAD rates based on your specified parameters.
- After the script finishes, you should see the generated image file, simulated_cad_rates.png.

## Jupyter Notebook:

- Launch Jupyter Lab or Notebook and open currency.ipynb.
- Run cells sequentially to see step-by-step results and modify parameters in real time.

---

# Example Output

- Below is a sample histogram you might see after running currency.py.
- The red dashed line shows the current rate (0.7 CAD/USD), while the histogram bins represent the distribution of simulated post-recovery rates:

``` 
Simulated Distribution of Post-Recovery CAD Rates (5000 Iterations)
<Histogram displayed, saved as "simulated_cad_rates.png">
```

---
# References

[Draft Paper
](https://github.com/ShaneSCalder/tariff-cad-volatility-model/blob/main/docs/NavigatingTariffTurbulenceProjecting%20theCanadianDollarunderUSTradePressuresDraft.pdf)


---

# License

This project is licensed under the MIT License. Feel free to modify or distribute this simulation as permitted under the license terms.

---

