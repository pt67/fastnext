# MyApp: Authentication System

A modern **authentication system** built with **Next.js 13**, **FastAPI**, and **Supabase**.
Includes Login, Signup, Dashboard, and Home pages with clean UI, SPA navigation, and secure authentication.

---

## **Table of Contents**

* [Demo](#demo)
* [Features](#features)
* [Tech Stack](#tech-stack)
* [Getting Started](#getting-started)
* [Environment Variables](#environment-variables)
* [Project Structure](#project-structure)
* [License](#license)

---

## **Demo**

* Home Page: `http://localhost:3000/`
* Login: `http://localhost:3000/login`
* Signup: `http://localhost:3000/signup`
* Dashboard: `http://localhost:3000/dashboard`

---

## **Features**

* Full **Login & Signup** system
* **Supabase** authentication and user management
* **Dashboard** with protected routes
* Responsive **Home page** with hero and features section
* SPA navigation with **Next.js App Router**
* Auto reload of Home page to fix layout issues
* Custom CSS styling
* Environment variables support

---

## **Tech Stack**

* **Frontend**: Next.js 13, React, CSS
* **Backend**: FastAPI
* **Database / Auth**: Supabase
* **Other**: Python, Node.js

---

## **Getting Started**

### **Prerequisites**

* Node.js >= 18
* Python >= 3.10
* Supabase account
* npm or yarn

### **Install Dependencies**

```bash
# Frontend
cd nextjs-app
npm install
# or
yarn install

# Backend
cd fastapi-app
pip install -r requirements.txt
```

### **Run Development Servers**

```bash
# Frontend
npm run dev
# Backend
uvicorn main:app --reload
```

Visit: `http://localhost:3000/`

---

## **Environment Variables**

Create a `.env` file in your project root:

```env
SUPABASE_URL=your_supabase_url
SUPABASE_KEY=your_supabase_anon_key
```

**Never commit your `.env` file.**

---

## **Project Structure**

```
nextjs-app/
├─ app/
│  ├─ page.js       # Home
│  ├─ login/page.js # Login page
│  ├─ signup/page.js# Signup page
│  ├─ dashboard/page.js
├─ globals.css      # Global styles
├─ package.json
├─ ...
fastapi-app/
├─ main.py          # FastAPI server
├─ requirements.txt
├─ ...
.env                # Environment variables (ignored)
.gitignore
```

---

## **License**

This project is licensed under the MIT License.

---

### **Notes**

* Home page automatically reloads once per visit to fix layout issues caused by SPA navigation.
* Supabase email confirmation may go to spam; consider using a verified domain or test emails.
