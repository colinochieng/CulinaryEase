# CulinaryEase - Your Culinary Journey Starts Here

Welcome to CulinaryEase, a vibrant platform that brings together culinary enthusiasts, home cooks, and aspiring chefs from around the world. Whether you're a seasoned chef or a kitchen novice, CulinaryEase is your go-to destination for sharing, discovering, and mastering the art of cooking.

## About CulinaryEase

CulinaryEase is designed to foster a community of food lovers who are passionate about exploring new cuisines, experimenting with recipes, and connecting with fellows. Our platform empowers you to share your culinary creations, browse a diverse collection of recipes, and learn from the experiences of others.

## Features

- **Recipe Sharing:** Showcase your culinary expertise by sharing your favorite recipes, complete with detailed instructions and captivating images.

- **Interactive Community:** Engage with a vibrant community of food enthusiasts, exchange ideas, and get inspired by others' creations.

- **Personalized Meal Planning:** Craft personalized meal plans effortlessly, tailored to your preferences and dietary requirements.

- **Comprehensive Recipe Library:** Browse an extensive collection of recipes spanning various cuisines, categories, and cooking techniques.

- **Video Inspiration:** Gain insights from video tutorials shared by members, enabling you to master complex dishes with ease.

- **Nutritional Insights:** Access nutritional information for recipes, making informed choices about your meals.

## Getting Started

1. **Sign Up or Log In:** Create an account or log in to start your culinary journey.

2. **Explore Recipes:** Dive into our recipe library and discover a world of flavors. Filter by cuisine, category, and more.

3. **Share Your Creations:** Share your recipes, complete with images and step-by-step instructions.

4. **Connect and Interact:** Engage with other members, leave comments, and exchange tips and tricks.
5. **Plan Your Meals:** Use our intuitive meal planner to organize your weekly meals effortlessly.
## Contributing

We welcome contributions from passionate developers who want to enhance the CulinaryEase experience. Feel free to fork this repository, make improvements.
## Feedback

Your feedback is crucial in shaping the CulinaryEase platform. If you have suggestions, encounter issues, or want to share your excitement, please reach out to us via the contact information provided.

### Staring the program
```
PS C:\Users\user\Documents\GitHub\CulinaryEase> python -m app.Ver1.app
C:\Users\user\Documents\GitHub\CulinaryEase\app\Ver1\static
 * Serving Flask app 'app'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit   
 * Restarting with stat
```
## Connect via APIs

### Examples
#### `Create an Account`
```
C:\Users\user> curl -X POST "http://localhost:5000/api/register" -H "Content-Type: application/json" -d "{"username": "john_doe", "email": "john@example.com", "password": "secretpassword",  "bios": "Hello, I'm John! Passionate about flavors and innovation, I'm a culinary artist who concatinates creativity with tradition to craft unforgettable dishes. With a penchant for experimenting in the kitchen", "city": "New York",  "state": "NY", "country": "USA"}"
```

_`Return for success`_
```
{
  "Account": "creation complete"
}
```

_`Return for after sending the same data`_
```
C:\Users\user> curl -X POST "http://localhost:5000/api/register" -H "Content-Type: application/json" -d "{"username": "john_doe", "email": "john@example.com", "password": "secretpassword",  "bios": "Hello, I'm John! Passionate about flavors and innovation, I'm a culinary artist who concatinates creativity with tradition to craft unforgettable dishes. With a penchant for experimenting in the kitchen", "city": "New York",  "state": "NY", "country": "USA"}"


{
  "message": "Account with the email already exist",
  "status": "fail"
}
```

#### `Delete an Account`
```
C:\Users\user> curl -X DELETE http://localhost:5000/api/user/delete/ -H "Content-Type: application/json" -d "{"username": "john_doe", "password": "secretpassword"}"
```

#### `Change an password`

```
curl -X PUT http://192.168.0.15:5000/api/user/change-password/  -H "Content-Type: application/json" -d "{"username": "colin", "new_password": "2006@Dollar", "old_password": "okumu@254"}"
```

## Project Inspiration and Vision
![img](https://miro.medium.com/v2/resize:fit:720/format:webp/1*Fkkpst7WEimo77FTqbF8TA.jpeg)  

Creating CulinaryEase was a labor of love born from a deep passion for both technology and the culinary arts. The inspiration behind this project was to bridge the gap between food enthusiasts, making it easier for them to connect, share, and explore their love for cooking. As a developer, I wanted to challenge myself to build a platform that not only offered technical solutions but also fostered a vibrant community.
The technical challenge I set out to solve was to create a seamless and user-friendly platform where users could not only access a diverse array of recipes but also interact with each other through likes, comments, and personalized meal planning. This required mastering various technologies, from database design to front-end development, and implementing complex features like user authentication and recipe categorization.
I won't deny that there were moments of struggle and self-doubt, especially when tackling intricate technical issues or refining the user interface. However, these challenges have been instrumental in my growth as a developer. They remind me of the relentless pursuit of excellence and the importance of perseverance.
Looking ahead, I envision a next iteration of CulinaryEase that delves deeper into personalization, offering tailored recipe recommendations and enhanced user interactions. I also see room for integrating data analysis to analyze user preferences and suggest recipes based on their tastes.   

[For More](https://medium.com/@colinatjku/602cbd613b5b)  
[Author](https://www.linkedin.com/in/colin-okumu-a60729270/)