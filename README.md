## Django Web App for Institution Level Verification for Scholarships
[Institution Level Verification Web App](https://example.com)
This web app allows Indian students to get institution level verification done for scholarships in their home states when they are studying in another state within India. It is built using Django, PostgreSQL, and Tailwind CSS.

**Features:**

* Students can create an account and register their institution and scholarship details.
* Students can request verification from their institution.
* Institutions are verified by State Government users to ease the process.
* Institutions can log in and verify student requests.
* Students can download their verification certificate once it is approved.

**Benefits:**

* This web app saves students the time and hassle of having to travel to their home state to get their verification done.
* It helps student avail scholarships, they previously were't able to apply.
* It also makes the verification process more efficient and transparent.

**How to use:**

1. Create an account and register your details.
2. Apply for a scholarship and request verification from your institution.
3. Once your verification request is approved, download your verification certificate.

**Requirements:**

* Python 3.6 or higher
* Django 3.2 or higher
* PostgreSQL 12 or higher
* Tailwind CSS 3.0 or higher

**Installation:**

1. Clone this repository:

    ```
    git clone https://github.com/CSE5cectl/iLevelScholarship.git
    ```

2. Install the required dependencies:

    ```
    pip install -r requirements.txt
    ```

3. Create a database and configure Django to use it:

    ```
    python manage.py migrate
    ```

4. Start the development server:

    ```
    python manage.py runserver
    

5. Open your web browser and go to http://localhost:8000/ to start using the app.

**Deployment:**

This app is currently deployed on Vercel and its database is hosted on Supabase. For bigger scale purposes, it can be deployed to any production-ready web server.

**Contributing:**

If you have any suggestions or bug reports, please feel free to create an issue on GitHub.

**License:**

This app is licensed under the MIT License.