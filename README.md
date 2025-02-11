# URL Shortener Microservice Application 🚀

A simple **URL Shortener** app built with a **microservice architecture** 🛠️, split into **Frontend** and **Backend** components.

## 🖥️ **Architecture**

- **VM1 (Frontend - Ubuntu Desktop)**:
  - **Nginx** serves `index.html` and acts as a reverse proxy 🌐.
  - **Port 80** for serving the UI and API requests.

- **VM2 (Backend - Ubuntu Server)**:
  - **Flask** handles the URL shortening & retrieval logic.
  - **Port 5000** for API endpoints `/shorten` and `/get_original`.

## 🔧 **Installation & Setup**

### Step 1: VM Setup 🖥️

1. **VM1** (Frontend - Ubuntu Desktop):
   - Install **Nginx** to serve the `index.html` file and proxy requests.
   - Set a static IP for **VM1** (e.g., `192.168.56.102`).

2. **VM2** (Backend - Ubuntu Server):
   - Install **Flask** to run the backend microservice that handles URL shortening and retrieval.
   - Set a static IP for **VM2** (e.g., `192.168.56.103`).

### Step 2: Network Configuration 🌐

- Ensure **VM1** and **VM2** can communicate over a private network (Bridged or Internal Networking).
- Test connectivity between the VMs using `ping`:
  ```bash
  ping 192.168.56.103  # From VM1 to VM2
  ping 192.168.56.102  # From VM2 to VM1
