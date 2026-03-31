# 🛡️ Proof-of-Generation (PoG) Demo

An interactive, presentation-ready dashboard demonstrating **Proof-of-Generation (PoG)** — a cryptographic framework designed to ensure verifiable trust, authenticity, and tamper detection in AI-generated data within IoT networks.

> **"In the future, trust will not be assumed — it will be verified."**

---

## 🚀 The Core Concept
Current IoT systems rely on *Assumed Trust*—blindly accepting AI-generated data based on the reputation of the organization or centralized servers. This leaves networks vulnerable to deepfake sensor data, model poisoning, and data tampering.

**Proof-of-Generation (PoG)** shifts the paradigm to *Verifiable Trust* by integrating:
1. **Generative AI**
2. **IoT Data Streams**
3. **Zero-Knowledge Proofs (ZKP)**
4. **Blockchain Immutability**

---

## 🎛️ Demo Features
This application is built for live technical presentations, featuring a split-screen comparative analysis:

* 🟥 **Traditional Vulnerable System (Left):** Simulates how current architectures ingest tampered IoT data blindly without verification.
* 🟩 **PoG Framework (Right):** Generates a cryptographic SHA-256 fingerprint for the data, stores it on a simulated blockchain, and audits the ledger to catch tampering in real-time.
* 🌓 **Light/Dark Mode UI:** Seamless theme toggling for different presentation environments.
* ⏱️ **Simulated Processing:** Built-in UI delays to mimic the computational weight of ZKP generation and blockchain auditing during a live demo.

---

## ⚙️ Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone <your-repo-link>
   cd pog_demo
   ```

2. **Install requirements:**
   ```bash
   pip install flask
   ```

3. **Run the application:**
   ```bash
   python app.py
   ```
   The application will automatically launch your default browser to `http://127.0.0.1:5000/`.

---

## 🎤 Presentation Demo Flow
If you are presenting this dashboard, follow these steps to maximize impact:

1. **The Vulnerability:** Click *Fetch* on the Traditional side. Read the sensor data, then manually alter a value (e.g., change heart rate to a dangerous level). Click *Submit Data*. **Result:** The system blindly accepts the tampered data.
2. **The Solution:** Move to the PoG Framework side. Click *Fetch*, then *Generate Proof*. The UI will simulate the creation of a cryptographic hash and secure it on the blockchain.
3. **The Audit:** Alter the data slightly just as before. Click *Verify Data*. **Result:** The system audits the ledger and instantly flags the tampering, proving data authenticity is compromised.

---

## 👨‍💻 Authors
* Khurram Rashid

*Department of CSE, Amity University, Mumbai*
```