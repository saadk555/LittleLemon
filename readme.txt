NOTE:
Since databases are limited to local envoriment in this course, please enter your own database details, create users and tokens manually or through apis as decribed in the coursera's previous modules and then use the respective API where token authorization is required.


PLEASE DON'T FORGOT TO CHANGE THE DETAILS WHICH ARE SPECIFIC TO YOUR SYSTEM SUCH AS PORT OR IP IF YOU ARE USING OTHER THAN WHAT ARE MENTIONED BELOW

(authorization is required in some of them. You will know through response where it will be required)
 

Following are the API URL

http://127.0.0.1:8000/restaurant/menu/       
http://127.0.0.1:8000/restaurant/menu/2/     (change the id with your newly created ID)
http://127.0.0.1:8000/restaurant/api-token-auth/ (POST METHOD)
http://127.0.0.1:8000/restaurant/booking/ 



Djoser:
http://127.0.0.1:8000/auth/users/   (users can also be registered through post method)
http://127.0.0.1:8000/auth/users/me/
http://127.0.0.1:8000/auth/users/confirm/
http://127.0.0.1:8000/auth/users/resend_activation/
http://127.0.0.1:8000/auth/users/set_password/
http://127.0.0.1:8000/auth/users/reset_password/
http://127.0.0.1:8000/auth/users/reset_password_confirm/
http://127.0.0.1:8000/auth/users/set_username/
http://127.0.0.1:8000/auth/users/reset_username/
http://127.0.0.1:8000/auth/users/reset_username_confirm/

Djoser TOKEN:
http://127.0.0.1:8000/auth/token/login/

