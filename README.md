![image](https://github.com/user-attachments/assets/c361c305-927b-43b7-8e4b-b34a997aa288)


---

# Minecraft JVM Arguments Generator

A simple Python script that suggests optimized JVM arguments for launching Minecraft Java Edition based on your system’s RAM. The generated JVM options aim to improve performance and stability by tuning the Java Garbage Collector (G1GC) settings and memory allocation, following best practices for Minecraft Java launch options.

---

## Features

* Automatically detects your system's total RAM
* Suggests an appropriate max heap size (`-Xmx`) between 1 GB and 12 GB based on available RAM
* Uses a proven JVM arguments template optimized for Minecraft:

  ```
  -Xmx{heap}G -XX:+UnlockExperimentalVMOptions -XX:+UseG1GC -XX:G1NewSizePercent=20 -XX:G1ReservePercent=20 -XX:MaxGCPauseMillis=50 -XX:G1HeapRegionSize=32M
  ```
* Allows manual override of max heap size
* Outputs JVM arguments in a ready-to-use format for Minecraft launchers

---

## Requirements

* Python 3.6 or newer
* [psutil](https://pypi.org/project/psutil/) Python package

---

## Installation

1. Clone this repository or download the script file `jvm.py`.

2. Install dependencies:

```bash
pip install psutil
```

---

## Usage

Run the script:

```bash
python jvm_args_generator.py
```

The script will detect your system’s RAM and suggest a max heap size for Minecraft. You can accept the suggestion or enter your preferred heap size in gigabytes.

Example output:

```
Detected system RAM: 16.00 GB
Suggested max heap size (-Xmx): 12G

Enter max heap size in GB or press Enter to use 12G: 
Generated JVM arguments:
-Xmx12G -XX:+UnlockExperimentalVMOptions -XX:+UseG1GC -XX:G1NewSizePercent=20 -XX:G1ReservePercent=20 -XX:MaxGCPauseMillis=50 -XX:G1HeapRegionSize=32M
```

Copy the generated JVM arguments and paste them into your Minecraft launcher’s Java Arguments field.

---

## Notes

* The script caps the max heap size suggestion to 12 GB to maintain Minecraft stability.
* For systems with less than 2 GB RAM, the script will recommend a minimum of 1 GB heap.
* You can modify the `format_jvm_args()` function in the script to customize JVM arguments if needed.
* These JVM arguments are optimized for Java 8 and above, and are compatible with Minecraft Java Edition using modern Java versions.

---


## Contributions

Pull requests and suggestions are welcome! Please open an issue first to discuss what you would like to change.


