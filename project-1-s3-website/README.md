# Project 1: Host a Simple Website on Amazon S3 🚀

If you are new to cloud computing, managing servers can feel very hard. But did you know you can put a website on the internet without managing a single server? 

Welcome to Project 1! Today, we will learn the easiest and cheapest way to host a website using **Amazon S3 (Simple Storage Service)**. 

Instead of using servers, we will use S3 to save your static files (like HTML) and turn them into a real website that anyone in the world can visit.

![AWS S3 Architecture](image_04c03c.png)

### 🎯 What You Will Learn
* **AWS S3 Basics:** How to make a "Bucket" and upload files (called "Objects").
* **Static Website Hosting:** How to set up your S3 bucket to act like a web server.
* **Permissions & Security:** How to use Bucket Policies. By default, S3 buckets are private. You will learn how to safely open your bucket so people can see your website.

---

### 🛠️ What You Need First: Create Your Website File

Before we go to AWS, let's make a simple HTML file. We will save this as `index.html` inside this project folder.

```html
<html>
	<head>
		<title>Static Website Project</title>
	</head>
	<body>
		<h1>Congratulations!!! 🎉</h1>
		<h2>Welcome to my AWS S3 Static Website</h2>
	</body>
</html>
