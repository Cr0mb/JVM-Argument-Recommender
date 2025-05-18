![image](https://github.com/user-attachments/assets/2fce159a-94a7-40ba-bbc3-c0e64e938daf)


# JVM Argument Recommender

A lightweight Python script that recommends optimized JVM (Java Virtual Machine) launch arguments based on your system's hardware specs (CPU, RAM, architecture). Ideal for tuning performance for Minecraft servers, Java apps, or any JVM-based workload.

---

## What It Does

This script analyzes:
- Your **total RAM**
- Your **CPU cores and threads**
- Your **system architecture (32-bit or 64-bit)**

And based on that, it prints a set of recommended JVM arguments, optimized for performance using the G1 Garbage Collector (`G1GC`).

---

## Features

- Detects RAM and suggests appropriate `-Xmx` and `-Xms` heap sizes
- Enables G1GC tuning options:
  - `G1NewSizePercent`
  - `G1ReservePercent`
  - `MaxGCPauseMillis`
  - `G1HeapRegionSize`
- Adds `-d64` if you're on a 64-bit system
- Outputs detected system specs

---

## Usage

1. **Clone this repo or download the script:**

```bash
git clone https://github.com/Cr0mb/JVM-Argument-Recommender.git
cd JVM-Argument-Recommender
````

2. **Run the script:**

```bash
python jvm.py
```

> Requires Python 3.x and the `psutil` module.

---

## Installation

Install dependencies (only `psutil` is needed):

```bash
pip install psutil
```

---

## Recommended For

* Minecraft Server Optimization
* Java Application Performance Tuning
* JVM Debugging
* DevOps/Systems Engineers working with JVM environments

---


## Contributions

Pull requests and suggestions are welcome! Please open an issue first to discuss what you would like to change.


