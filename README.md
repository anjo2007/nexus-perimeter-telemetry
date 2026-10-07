# NEXUS DYNAMICS // PERIMETER TELEMETRY & CAMERA RELAY

**System Node:** PERIMETER-GATE-B-DAEMON  
**Subnet:** 10.14.8.0/24  
**Classification:** PHYSICAL SECURITY ACCESS ARCHIVE  
**Preserved By:** Cyber Crime Task Force × FOSS GECT Cell  

---

## 1. NODE OVERVIEW

This repository archives raw optical, audio, and ANPR sensor telemetry from the perimeter security network surrounding Building B of the Nexus Dynamics campus.

During the incident on the night of October 1–2, 2026, security relay camera CAM-04 recorded unauthorized vehicle movement at Gate B. Multiple peripheral sensors and audio channels were captured to this node.

Investigators must identify the suspect vehicle, retrieve the registration plate, and decrypt the forensic vault before the 2-hour server wipe timer expires.

---

## 2. REPOSITORY ASSETS

| Artifact | Type | Description |
| :--- | :--- | :--- |
| `cam04_frame.png` | CCTV Capture | Raw high-resolution capture from Gate B camera at 01:42:18 IST. |
| `phone_log.txt` | VoIP Transcript | Audio wiretap log from Gate B VoIP bridge. |
| `stage2_vault.zip` | Encrypted Vault | Encrypted archive containing acoustic signal telemetry (Password = License Plate). |
| `camera_01_gate_a.log` | Gate Log | Decoy log: Routine visitor and delivery vehicle records at Gate A. |
| `camera_02_visitor_lobby.log` | Access Log | Decoy log: Interior lobby biometric swipes and badge attempts. |
| `camera_03_loading_dock.log` | Cargo Log | Decoy log: Supply chain loading dock security records. |
| `camera_04_gate_b.log` | Gate Log | **Primary incident log:** Ingress/egress records for Gate B. |
| `malayalam_cinema_radio_intercept.txt` | Audio Transcript | Guard shack FM radio intercept discussing investigative cinema alibis. |
| `sensor_calibration_matrix.csv` | Telemetry Data | Optical and thermal sensor wavelength matrices. |
| `vault_extractor.py` | Utility Script | Open-source CLI decryption tool to unlock `stage2_vault.zip`. |

---

## 3. HOW TO UNLOCK THE VAULT

Contestants can extract `stage2_vault.zip` using any standard archive tool or run the python extractor:

```bash
python vault_extractor.py
```

Enter the vehicle license plate identified in `phone_log.txt` and `cam04_frame.png` (Format: `KL-08-CC-4912`).

Inside the vault, you will recover:
1. `recordings/chime_transmission.wav` — The harmonic chime audio transmission.
2. `chime_cipher_grid.txt` — The 5×5 acoustic decryption grid.
3. `audio_spectrogram_hint.txt` — Spectrum frequency readings.
4. `stage3_dossier.txt` — Instructions linking to the secret safehouse node:
   [`https://github.com/anjo2007/aether-safehouse-node`](https://github.com/anjo2007/aether-safehouse-node)

---
*FOSS GECT (Free and Open Source Software Cell) × GECT FILM SOCIETY*
