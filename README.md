# 🔐 Security Log Analyzer



<div align="center">



![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)

![Cybersecurity](https://img.shields.io/badge/Cybersecurity-Log%20Analysis-red)

![Regex](https://img.shields.io/badge/Regex-Pattern%20Matching-orange)

![Status](https://img.shields.io/badge/Status-Completed-success)



### Security Event Detection and Log Analysis System



A Python-based security monitoring tool that analyzes log files, detects suspicious activities, extracts security indicators, and generates actionable security insights.



</div>



---



# 📖 Overview



Security Log Analyzer is a cybersecurity-focused project designed to process and analyze security logs to identify potential threats and suspicious activities.



The system automatically extracts security-related information such as IP addresses, usernames, failed authentication attempts, and SQL Injection attacks from log files using advanced Regular Expression techniques.



This project demonstrates practical security monitoring concepts commonly used in Security Operations Centers (SOC) and incident response environments.



---



# ✨ Features



## 🔍 Security Event Detection



* Detect Failed Login Attempts

* Detect SQL Injection Attacks

* Identify Suspicious Activities

* Validate Security Log Entries



## 🌐 Threat Intelligence Extraction



* Extract Source IP Addresses

* Extract Usernames

* Analyze Authentication Events

* Track Security Incidents



## 🛡️ Data Protection



* IP Address Masking

* Sensitive Information Sanitization

* Secure Log Processing



## 📊 Security Reporting



* Generate Security Summaries

* Count Failed Authentication Attempts

* Report Detected Attacks

* Display Security Statistics



---



# 🏗️ System Architecture



```text

Security Log File

        │

        ▼

   Log Parser

        │

        ▼

 Regular Expressions

        │

        ▼

 Event Detection Engine

        │

        ▼

 Security Analysis

        │

        ▼

 Security Report

```



---



# 🛠️ Technology Stack



### Programming Language



* Python 3



### Libraries



* re (Regular Expressions)



### Cybersecurity Concepts



* Security Log Analysis

* Threat Detection

* Event Correlation

* Authentication Monitoring

* Incident Detection

* Data Sanitization



---



# 📂 Project Structure



```text

Security-Log-Analyzer/

│

├── index.py

├── log.txt

└── README.md

```



---



# 📄 Sample Security Logs



```text

2026-05-15 10:15:32 FAILED LOGIN user:admin IP:192.168.1.5

2026-05-15 10:16:11 SUCCESS LOGIN user:ahmed IP:192.168.1.8

2026-05-15 10:17:45 FAILED LOGIN user:root IP:10.0.0.7

2026-05-15 10:18:20 SQL Injection detected from IP:172.16.0.3

```



---



# 🚀 Installation



## Clone Repository



```bash

git clone https://github.com/abdullhamar/Security-Log-Analyzer.git

cd Security-Log-Analyzer

```



## Run the Analyzer



```bash

python index.py

```



---



# 🔬 How It Works



1. Load the security log file.

2. Parse each log entry.

3. Extract IP addresses and usernames.

4. Detect failed login attempts.

5. Identify SQL Injection attacks.

6. Mask sensitive IP information.

7. Generate a security analysis report.



---



# 📊 Example Output



```text

========================================

Security Log Analysis Results

========================================



Number of failed login attempts: 3



Detected IP addresses:

192.168.1.XXX

10.0.0.XXX

172.16.0.XXX



User names:

admin

ahmed

root



Number of SQL Injection attacks: 1



========================================

```



---



# 🎯 Learning Outcomes



This project demonstrates:



* Cybersecurity Fundamentals

* Security Monitoring Techniques

* Log Analysis Methodologies

* Threat Detection Concepts

* Regular Expressions in Security

* Python for Cybersecurity

* Security Event Processing



---



# 🚀 Future Improvements



* Real-Time Log Monitoring

* Brute Force Attack Detection

* Email Alert System

* CSV & PDF Report Export

* Dashboard Visualization

* Multi-Source Log Support

* SIEM Integration

* Threat Intelligence Enrichment



---



# 🎓 Academic Project



This project was developed as part of cybersecurity and Python programming studies to explore practical approaches for security monitoring and threat detection through automated log analysis.



---



# 👨‍💻 Author



### Abdullah Hamar



Cybersecurity & Software Development Enthusiast



GitHub: https://github.com/abdullhamar



---



# ⭐ Support



If you found this project useful, consider giving it a star ⭐.



It helps support future development and encourages open-source contributions.



---



<div align="center">



### Securing Systems Through Intelligent Log Analysis 🔐



</div>
