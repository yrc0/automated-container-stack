# **Automated Microservices Stack: From vSphere to Container Orchestration**

## **🚀 Project Overview**

This project demonstrates a full-lifecycle DevOps workflow, transitioning from traditional virtualization (VMware vSphere) to modern automated container orchestration. I have engineered a 3-tier microservices application deployed via **Ansible** onto an **Ubuntu VM**, featuring **Multi-stage Docker builds** for optimization and **Zabbix** for enterprise-grade observability.

### **Key Objectives:**

* **Infrastructure as Code (IaC):** Automate the provisioning and configuration of a Linux server.  
* **Microservices Architecture:** Deploy a decoupled stack (Nginx, Flask, Redis).  
* **Security & Optimization:** Implement Ansible Vault for secrets and Multi-stage Dockerfiles for lean production images.  
* **Observability:** Integrate real-time monitoring via Zabbix Agent.

## **🏗️ Architecture**

The deployment follows a "Command Center" pattern where a MacBook (Control Node) orchestrates the remote Ubuntu VM.

1. **Control Node:** MacBook Pro (Ansible)  
2. **Target Node:** Ubuntu 24.04 VM (IP: 172.30.30.230) running on VMware vSphere.  
3. **Application Stack:**  
   * **Reverse Proxy:** Nginx (Container) \- Entry point for Port 80\.  
   * **Backend:** Python Flask (Container) \- Logic & API layer.  
   * **Database:** Redis (Container) \- State management & visit counter.  
4. **Monitoring:** Zabbix Agent (System) reporting to Zabbix Server (172.30.30.229).

## **🛠️ Tech Stack**

| Category | Tools |
| :---- | :---- |
| **Virtualization** | VMware vSphere / ESXi |
| **Automation** | Ansible (Playbooks, Vault, Inventory) |
| **Containerization** | Docker, Docker Compose |
| **Backend** | Python 3.11, Flask |
| **Data Store** | Redis (Alpine) |
| **Reverse Proxy** | Nginx |
| **Monitoring** | Zabbix 7.0 |

## **🛡️ Implementation Highlights**

### **1\. Multi-Stage Docker Build**

To ensure production security and performance, I utilized a multi-stage Dockerfile. This reduced the final image size significantly by excluding build-time compilers and only including the necessary Python binaries.

### **2\. Infrastructure Automation (Ansible)**

I developed two modular playbooks:

* deploy-stack.yml: Handles OS hardening, Docker installation, and application deployment.  
* zabbix-agent.yml: Automates the installation of the official Zabbix repository and configures the agent to communicate with my Zabbix Server.

### **3\. Secrets Management**

Sensitive data (SSH passwords, Zabbix Server IPs) are encrypted using **Ansible Vault**, ensuring that no credentials are ever hardcoded in plain text within the repository.

## **📸 Screenshots & Proof of Work**

*(Place your screenshots in an assets/ folder in this repository and link them below)*

#### **1\. Automated Deployment (Ansible) -- Live Web Application -- Container Status**
 ![Alt Text](assets/deployment.png)
#### **2\. Zabbix Monitoring Dashboard**
 ![Alt Text](assets/zabbix.png)

## **🚦 How to Run**

1. Clone the repository.  
2. Create your .ansible\_vault\_pass locally (ensure it is in your .gitignore).  
3. Configure your inventory.ini with your VM IP.  
4. Execute the deployment:  
   ansible-playbook \-i ansible/inventory.ini ansible/deploy-stack.yml \--vault-password-file .ansible\_vault\_pass

