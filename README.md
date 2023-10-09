# Cloud Resume Challenge

![Architecture](\front-end\images\cloud-resume-architecture.png)

This repository contains the code and infrastructure as code (IaC) scripts for my cloud-hosted resume. The application is hosted on AWS, leveraging services such as S3, CloudFront, and Lambda.
This project was done as part of a challenge to test my abilities using AWS cloud resources as a newly certified AWS Solutions Architect Associate and practice creating a practical infrastructure.

[Website Link](https://justinwright-engineering.com)

## Table of Contents

- [Challenge Overview](#challenge-overview)
- [Challenge Stages](#challenge-stages)
  - [Certification](#1-certification)
  - [Frontend](#2-frontend)
  - [API & Backend](#3-api--backend)
  - [CI/CD and Automation](#4-cicd-and-automation)

## Challenge Overview

The Cloud Resume Challenge is a popular cloud architect/engineer challenge aimed at showcasing and improving typical cloud architecture skills while also improving resume visibility.
The Cloud Resume Challenge serves as a platform for individuals to practice, demonstrate, and improve their cloud skills through the following methods:

#### Hands-on Experience
The challenge is designed as a hands-on project to build and demonstrate skills essential for a career as an AWS Cloud Engineer. Participants are required to construct a personal resume or portfolio website and include a visitor counter on the site. The project must be entirely deployed using various AWS services, providing a practical learning experience in handling cloud resources

#### Skill Development
It aids participants in developing crucial cloud skills, including setting up serverless applications, CI/CD pipelines, networking, and ensuring security. This aspect of the challenge is vital as it provides a real-world scenario for applying theoretical knowledge obtained from cloud certifications

#### Resume Enhancement
By participating in the challenge, individuals have the opportunity to enhance their resumes. The challenge allows them to present their resumes using cloud technologies, which not only showcases their technical skills but also makes their resumes more publicly and easily accessible.


## Challenge Stages

### 1. Certification

The first part of the challenge is to complete the AWS Cloud Practitioner certification exam. I decided to take this one step further and I successfully passed the [AWS Cloud Architect - Associate](https://www.credly.com/badges/70a3664d-e78e-4ed6-9357-fa81fbb3c0e1/public_url) certification exam on 09/28/2023.

### 2. Frontend

This section is about building the visual design of the resume using HTML, CSS, and JavaScript. It doesn't need to be fancy, but it should have some styling rather than a raw HTML page.

#### 2.1  HTML & CSS

For the HTML portion of the website, I created [`front-end/index.html`](front-end/index.html) and based it on the sections of my normal resume with CSS styling to provide a somewhat modern design with some visual transitions.
Prior to this I had little to no experience writing HTML or CSS code, so I started with a template and made adjustments where needed for the basics. Then I made larger design changes to fit my overall design view.

The website contains separated sections that would typically be seen on a resume such as personal information, skills, work experience, education, certification, and personal projects. I also included links to my relevant socials as well as a link to download a copy of my official resume in pdf format.

#### 2.2  JavaScript

JavaScript was used to tackle one of the challenge tasks which was to create a visitor counter for the website. This was added to the index file and works with an AWS API and DynamoDB table on the backend to preserve the visitor count.

More on this in the Backend and Integration section.

#### 2.4  Static Asset Hosting

The html code along with all supporting files are hosted on an AWS S3 bucket with static hosting enabled and public read-only permission. Because S3 static website hosting doesnt offer HTTPS functionality, I used CLoudFront to provide HTTPS functionality.

More on that in the following section.

#### 2.4  CloudFront

In order to provide HTTPS functionality, I created a CloudFront distribution. By using CloudFront, I was able to set the S3 bucket as the origin and assign an SSL certificate obtained using ACM.

#### 2.5  Route 53

In order to access the website, I registered a domain using Route 53 which points the DNS domain name at the CloudFront distribution.

### 3. API & Backend

The API serves as an intermediary between the websites frontend (the JS running in the browser) and the backend infrastructure, which for this project is Lambda and DynamoDB.
Its primary purpose is to allow the frontend to retrieve and update the visitor count without directly accessing the database, ensuring a greater level of security and scalability (if needed).

#### 3.1  DynamoDB

I set up a table in DynamoDB called VisitorCount with a single item called myWebsite which tracks the number of site visits.

#### 3.2  Lambda

Using [`backend/IncrementVisitorCount.py`](backend/IncrementVisitorCount.py), I created a Lambda function that fetches the current visitor count from DynamoDB, increments it, and then returns the updated count to the API Gateway.

#### 3.3  API Gateway

The purpose of the API Gateway is to provide an endpoint for the JavaScript to call to get or update the visitor count. This call triggers the Lambda function.

### 4. CI/CD and Automation

#### 4.1 CI/CD

To automate any code or configuration changes to the frontend, GitHub Actions were used along with a dedicated pipeline workflow. All steps and stages can be seen in the [`.github/workflows/front-end-cicd.yml`](.github/workflows/front-end-cicd.yml)

Whenever a change is pushed to any frontend files in this GitHub repo, the workflow will run and automatically update the files in the S3 Bucket.

#### 4.2 Infrastructure as Code (IaC)

***IN PROGRESS***

The last step of this project is to manage the AWS resources using an IaC solutions such as SAM or Terraform. I've started a Terraform project and I have most of the AWS infrastructure imported. I need to fix a few things and test a full deployment before adding it here. 