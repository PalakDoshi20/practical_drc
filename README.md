# practical_drc
Authentication system

1. Create a virtualenv and run requirements.txt
2. Go to project folder and run
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
3. To test the authentication apis:

  Register - http://127.0.0.1:8000/register/

  Payload = 
  {
    "username": "palak20",
    "email": "palak12@gmail.com",
    "mobile": "8511093538",
    "password": "palak12"
}

Login - http://127.0.0.1:8000/login/

  Payload = 
  {
    "mobile": "8511093538"
  }

verify opt - http://127.0.0.1:8000/verifyotp/1/
{
    "otp": "0000"
}