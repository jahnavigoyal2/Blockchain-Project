# Blockchain-Project

A Flask-based web app that simulates blockchain technology for secure rental agreement management. Users can create, verify, and view agreements stored as blockchain blocks with proof-of-work, ensuring transparency, integrity, and trust in property rental records.

---

## 👩‍💻 Team Members

| Name           | Roll No | Department | Semester | Specialization |
|----------------|---------|------------|----------|----------------|
| Jahnavi Goyal  | 14045   | BTech CE   | 5th      | CS             |
| Mahi Patel     | 14053   | BTech CE   | 5th      | SE             |
| Het Kansagara  | 14105   | BTech CE   | 5th      | SE             |

---
## 🎯 Project Background

Traditional rental systems often rely on paper-based or centralized records, which can be altered or lost, leading to trust issues between landlords and tenants. This project uses blockchain technology to ensure transparency and security in managing rental agreements. By storing each agreement as a block linked through cryptographic hashes, the system prevents data tampering and ensures every record remains verifiable, creating a reliable and transparent digital rental management solution.

---

## 🛠️ Tech Stack Used

- Frontend: HTML, CSS, Bootstrap 5
- Backend: Python, Flask Framework
- Blockchain Logic: Custom Python implementation using SHA-256 hashing and Proof of Work
- Database: In-memory storage (simulated blockchain ledger)
- Tools & Environment: VS Code, Virtual Environment (venv), Flask Server
- Version Control: Git & GitHub

---

## 🚀 Features
- 🔐 Blockchain Simulation – Each rental agreement is stored as a transaction and linked to a cryptographically hashed block.
- 🧾 Create Rental Agreements – Easily add new agreements including landlord, tenant, property address, rent, and duration.
- ⛓️ View Blockchain – Inspect every block with its details, timestamp, proof, and hash connections.
- 🌐 Flask Web Interface – Interactive web app built with Python Flask and Bootstrap for an elegant user experience.
- ⚡ Proof of Work (PoW) – Ensures blocks are mined before being added to the chain, mimicking real blockchain validation.

---

## 💡 How It Works
1. User fills out a form to create a new rental agreement.
2. The backend generates a unique block containing the agreement details.
3. The block is hashed and added to the blockchain using a proof-of-work mechanism.
4.The blockchain ledger can be viewed at any time to verify the sequence and integrity of records.
