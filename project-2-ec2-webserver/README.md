# Project 2: Launching a Web Server on EC2 🚀

In this project, we move from "Storage" (S3) to "Compute" (EC2). You will launch a Virtual Server in the cloud and set it up to be a real Web Server. This helps you understand how Infrastructure-as-a-Service (IaaS) works.

![AWS EC2 Architecture](image_052cda.jpg)

### 🎯 What You Will Learn
* **EC2 (Elastic Compute Cloud):** How to start a virtual machine (Linux) in the cloud.
* **Security Groups:** Understanding cloud firewalls. You will open Port 80 (HTTP) to let people visit your website.
* **Linux Basics:** Using basic commands to install the Apache web server software.

---

### 🚀 Step-by-Step Guide

We will use **Amazon Linux** and install the **Apache Web Server**.

#### Step 1: Launch EC2 Instance
1. Go to the **AWS Console**.
2. Search for the **EC2** service and click it.
3. Click the orange **"Launch instance"** button.
4. In the **Name** field, enter: `My-First-Web-Server`.
5. In **Application and OS Images (AMI)**, select **Amazon Linux** (leave it as default).
6. In **Instance type**, make sure it's **t2.micro** or **t3.micro** (Free tier eligible).

#### Step 2: Create Key Pair
You need this "key" to connect to your server safely.
1. In the **Key pair (login)** section, click **"Create new key pair"**.
2. In **Key pair name**, enter: `myserver-key`.
3. Set **Type** to **RSA** and **Format** to **.pem**.
4. Click **"Create key pair"**. (A file will download to your computer. Save it safely!)

#### Step 3: Configure Firewall (Network Settings)
This is very important. We must open the "door" for web traffic.
1. Click **"Edit"** next to **Network settings**.
2. Under **Inbound security groups rules**, you will see SSH (Port 22).
3. Click **"Add security group rule"**.
4. For **Type**, select **HTTP**. (The port will automatically become **80**).
5. For **Source**, select **Anywhere (0.0.0.0/0)**.

#### Step 4: Launch the Server
1. Click the **"Launch instance"** button on the right side.
2. Click **"View all instances"**.
3. When the **Instance State** becomes **Running**, your server is ready!

#### Step 5: Connect and Install (Linux Commands)
1. Select your instance and click **"Connect"** at the top.
2. Under the **"EC2 Instance Connect"** tab, click **"Connect"**.
3. A black screen (Terminal) will appear. Copy and paste these commands one by one:

**Install Apache:**
```bash
sudo yum update -y
sudo yum install httpd -y
```

**Start the Web Server:**
```bash
sudo systemctl start httpd
sudo systemctl enable httpd
```

**Create your website page:**
```bash
sudo su
cat > /var/www/html/index.html << 'EOF'
<!DOCTYPE html>
<html>
<head>
    <title>My AWS EC2 Server</title>
    <style>
        body { font-family: Arial; text-align: center; padding: 50px; background-color: #f0f0f0; }
        h1 { color: #FF9900; }
        .container { background: white; padding: 30px; border-radius: 10px; max-width: 800px; margin: 0 auto; }
    </style>
</head>
<body>
    <div class="container">
        <h1>🚀 Welcome to My AWS EC2 Server!</h1>
        <p>This web server is running on Amazon Linux with Apache</p>
    </div>
</body>
</html>
EOF
```

#### Step 6: Testing
1. Go back to the EC2 Console.
2. Find your **Public IPv4 address** (Example: `54.123.45.67`).
3. Paste that IP address into your web browser.
4. If you see your "Welcome" page, you have succeeded! 🎉

---

### 💻 Bonus: Automation with User Data
Instead of typing commands, you can paste the script below into the **"Advanced Details > User Data"** box when you first launch the instance. AWS will run it automatically!

```bash
#!/bin/bash
yum update -y
yum install httpd -y
systemctl start httpd
systemctl enable httpd
# (Your HTML code goes here)
```

---
[⬅️ Back to Main Menu](../README.md)
