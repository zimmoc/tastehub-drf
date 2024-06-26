# TasteHub

TasteHub wants to bring food lovers together to share and find new recipes. It's here to make cooking fun and social. You can explore different recipes, like your favorites, and connect with others who love to cook. By letting you like, comment, and follow other users, TasteHub makes it easy to learn and enjoy cooking more.


##### [Live demo page](https://tastehub-c1a3a811ccbe.herokuapp.com/)


![Responsive Mockup](/readme/all-devices-black.png)

## General

This is the API for the TasteHub backend application. This readme will only contain documentation related to the models, database, and testing of them. More detailed information about the full application can be found in the frontend readme, which is much more extensive.

- The TasteHub [frontend repository](https://github.com/zimmoc/tastehub)

## Database and Model

In the development environment, TasteHub utilizes SQLite, which is easy to set up and perfect for development and testing purposes. For the production environment, PostgreSQL is employed because of its robustness, scalability, and advanced features, making it well-suited for managing a live web application.


__Recipe Model__
- **Fields**: owner, created_at, updated_at, title, description, image, ingredients, instructions
- **Purpose**: Stores recipes created by users.
- **Usage**: Central to the application's content, allowing users to share and manage their recipes.


__Comment Model__
- **Fields**: owner, recipe, created_at, updated_at, content
- **Purpose**: Stores comments made by users on recipes.
- **Usage**: Allows users to engage with recipes by commenting.

__Follower Model__
- **Fields**: owner, followed, created_at
- **Purpose**: Manages follower relationships between users.
- **Usage**: Enables users to follow each other, creating a personalized feed.

__Like Model__
- **Fields**: owner, recipe, created_at
- **Purpose**: Stores likes on recipes by users.
- **Usage**: Allows users to express appreciation for recipes.

__Profile Model__
- **Fields**: owner, created_at, updated_at, bio, name, image
- **Purpose**: Stores user profile information.
- **Usage**: Allows users to customize their profiles with bio, name, and profile picture.

__Rating Model__
- **Fields**: owner, created_at, updated_at, recipe, value
- **Purpose**: Stores ratings given by users to recipes (currently unused).
- **Usage**: Prepared for future implementation to allow users to rate recipes.


#### Entity-Relationship Diagram

The final database schema is essentially the same, but with some changes to the types of fields due to the limitations of the website I used.

![erd](/readme/erd.png)

## Technologies

### Language

- [Python](https://www.python.org/): Serves as the back-end programming language.

### Framework

- [Django Rest Framework (DRF)](https://www.django-rest-framework.org/): Used to create the API.


<details>
<summary>Tools and Services</summary>
<br>


- **[Git](https://git-scm.com/)**: Utilized for version control, enabling you to track changes and collaborate on code effectively.
- **[GitHub](https://github.com/)**: Essential for hosting repositories, facilitating version control, collaboration, and secure online code storage.
- **[Gitpod](https://gitpod.io/)**: Streamlines the development process with a pre-configured, cloud-based development environment that's ready for coding instantly.
- **[Google Dev Tools](https://developers.google.com/web/tools)**: Used for testing, debugging, and styling during development.
- **[Heroku](https://www.heroku.com/)**: A platform for deploying and hosting web applications, ensuring your app is accessible online.
- **[PostgreSQL](https://dbs.ci-dbs.net/)**: Provided by Code Institute, this database system is used for its robustness and compatibility with Django.

</details>
<br>

## Testing

### Automated testing

<details>
<summary>comments</summary>

### Summary

These tests cover the essential functionalities of the Comment model in the application. They ensure that users can create, retrieve, update, and delete comments, as well as prevent unauthorized users from modifying or deleting comments. The tests also validate that the application's data integrity is maintained by ensuring that only the comment owner can perform update and delete operations.

<hr />

**test_create_comment**
- **Purpose**: To verify that a comment can be successfully created.
- **What was tested**: 
  - Posting a new comment to the comments endpoint.
  - Checking the response status code.
  - Ensuring the comment is correctly added to the database.
  - Verifying the content, recipe, and owner of the newly created comment.
- **Why**: To ensure that the comment creation functionality works as expected and stores the comment details correctly.

<hr />

**test_retrieve_comments_list**
- **Purpose**: To verify that a list of comments can be retrieved.
- **What was tested**: 
  - Sending a GET request to retrieve all comments.
  - Checking the response status code.
  - Ensuring the correct number of comments is returned.
  - Verifying the content of the retrieved comments.
- **Why**: To ensure that the comments list endpoint returns the correct data.

<hr />

**test_retrieve_comment_detail**
- **Purpose**: To verify that a specific comment can be retrieved by its ID.
- **What was tested**: 
  - Sending a GET request to retrieve a specific comment by ID.
  - Checking the response status code.
  - Verifying the content of the retrieved comment.
- **Why**: To ensure that the comment detail endpoint returns the correct data for a given comment ID.

<hr />

**test_update_comment**
- **Purpose**: To verify that a comment can be updated by its owner.
- **What was tested**: 
  - Sending a PUT request to update the content of a comment.
  - Checking the response status code.
  - Ensuring the comment content is updated in the database.
- **Why**: To ensure that the comment update functionality works as expected and only the owner can update the comment.

<hr />

**test_delete_comment**
- **Purpose**: To verify that a comment can be deleted by its owner.
- **What was tested**: 
  - Sending a DELETE request to delete a comment.
  - Checking the response status code.
  - Ensuring the comment is removed from the database.
- **Why**: To ensure that the comment deletion functionality works as expected and only the owner can delete the comment.

<hr />

**test_non_owner_cannot_update_comment**
- **Purpose**: To verify that a comment cannot be updated by a user who is not the owner.
- **What was tested**: 
  - Attempting to update a comment by a non-owner.
  - Checking the response status code.
  - Ensuring the comment content is not changed in the database.
- **Why**: To ensure that only the comment owner can update the comment, maintaining data integrity and security.

<hr />

**test_non_owner_cannot_delete_comment**
- **Purpose**: To verify that a comment cannot be deleted by a user who is not the owner.
- **What was tested**: 
  - Attempting to delete a comment by a non-owner.
  - Checking the response status code.
  - Ensuring the comment is not removed from the database.
- **Why**: To ensure that only the comment owner can delete the comment, maintaining data integrity and security.

<hr />

</details>

<details>
<summary>followers</summary>

### Summary

These tests cover the essential functionalities of the Follower model in the application. They ensure that users can follow and unfollow other users, retrieve lists and details of followers, and that the application maintains data integrity by preventing duplicate follower relationships and unauthorized deletions.

<hr />

**test_create_follower**
- **Purpose**: To verify that a user can successfully follow another user.
- **What was tested**:
  - Posting a new follower relationship to the followers endpoint.
  - Checking the response status code.
  - Ensuring the follower relationship is correctly added to the database.
  - Verifying the owner and followed user of the newly created follower relationship.
- **Why**: To ensure that the follower creation functionality works as expected and stores the follower details correctly.

<hr />

**test_retrieve_followers_list**
- **Purpose**: To verify that a list of followers can be retrieved.
- **What was tested**:
  - Sending a GET request to retrieve all followers.
  - Checking the response status code.
  - Ensuring the correct number of followers is returned.
  - Verifying the owner of the retrieved followers.
- **Why**: To ensure that the followers list endpoint returns the correct data.

<hr />

**test_retrieve_follower_detail**
- **Purpose**: To verify that a specific follower can be retrieved by its ID.
- **What was tested**:
  - Sending a GET request to retrieve a specific follower by ID.
  - Checking the response status code.
  - Verifying the owner of the retrieved follower.
- **Why**: To ensure that the follower detail endpoint returns the correct data for a given follower ID.

<hr />

**test_delete_follower**
- **Purpose**: To verify that a user can unfollow another user.
- **What was tested**:
  - Sending a DELETE request to delete a follower relationship.
  - Checking the response status code.
  - Ensuring the follower relationship is removed from the database.
- **Why**: To ensure that the follower deletion functionality works as expected and allows users to unfollow others.

<hr />

**test_cannot_follow_twice**
- **Purpose**: To verify that a user cannot follow the same user twice.
- **What was tested**:
  - Attempting to create a duplicate follower relationship.
  - Checking the response status code.
  - Ensuring the follower relationship is not duplicated in the database.
- **Why**: To ensure that the follower creation functionality prevents duplicates, maintaining data integrity.

<hr />

**test_non_owner_cannot_delete_follower**
- **Purpose**: To verify that a user cannot delete another user's follower relationship.
- **What was tested**:
  - Attempting to delete a follower relationship by a non-owner.
  - Checking the response status code.
  - Ensuring the follower relationship is not removed from the database.
- **Why**: To ensure that only the follower relationship owner can delete the follower relationship, maintaining data integrity and security.

<hr />

</details>

<details>
<summary>likes</summary>

### Summary
These tests cover the essential functionalities of the Like model in the application. They ensure that users can like and unlike recipes, retrieve lists and details of likes, and that the application maintains data integrity by preventing duplicate likes and unauthorized deletions.

<hr />

**test_create_like**
- **Purpose**: To verify that a new like can be created for a recipe by a different user.
- **What was tested**:
  - Creating a like for a recipe by a different user.
  - Checking the response status code.
  - Ensuring the like is added to the database with the correct owner and recipe.
- **Why**: To confirm that users can like recipes, ensuring the like functionality works as intended.

<hr />

**test_retrieve_likes_list**
- **Purpose**: To verify that the list of likes can be retrieved correctly.
- **What was tested**:
  - Retrieving the list of likes for a user.
  - Checking the response status code.
  - Ensuring the correct number of likes and their details are returned.
- **Why**: To ensure the API returns the correct list of likes, facilitating the display of liked recipes.

<hr />

**test_retrieve_like_detail**
- **Purpose**: To verify that the details of a single like can be retrieved correctly.
- **What was tested**:
  - Retrieving the details of a specific like.
  - Checking the response status code.
  - Ensuring the correct details of the like are returned.
- **Why**: To confirm that users can view details of their likes, providing necessary information about who liked a recipe and when.

<hr />

**test_delete_like**
- **Purpose**: To verify that a like can be deleted by its owner.
- **What was tested**:
  - Deleting a like.
  - Checking the response status code.
  - Ensuring the like is removed from the database.
- **Why**: To confirm that users can remove their likes, giving them control over their interactions with recipes.

<hr />

**test_cannot_like_twice**
- **Purpose**: To verify that a user cannot like the same recipe more than once.
- **What was tested**:
  - Attempting to like a recipe twice within a transaction block.
  - Checking the response status code.
  - Ensuring no duplicate like is added to the database.
- **Why**: To maintain data integrity by preventing duplicate likes, ensuring accurate like counts.

<hr />

**test_non_owner_cannot_delete_like**
- **Purpose**: To verify that a user cannot delete another user's like.
- **What was tested**:
  - Attempting to delete a like by a non-owner.
  - Checking the response status code.
  - Ensuring the like is not removed from the database.
- **Why**: To ensure that only the owner of the like can delete it, preserving the authenticity of user interactions.

</details>

<details>
<summary>profiles</summary>

### Summary
These tests cover the essential functionalities of the Profile model in the application. They ensure that profiles are created upon user registration, users can retrieve and update their profiles, and that data integrity is maintained by preventing unauthorized users from updating profiles they do not own. This is crucial for maintaining user privacy and ensuring that profile data is accurate and secure.

<hr />

**test_create_profile**
- **Purpose**: To verify the creation of a profile upon user registration.
- **What was tested**:
  - Fetching profiles list to ensure profiles are created.
  - Checking the response status code.
  - Ensuring the correct number of profiles is returned.
- **Why**: To ensure that profiles are correctly created for new users.

<hr />

**test_retrieve_profiles_list**
- **Purpose**: To verify that the list of profiles can be retrieved.
- **What was tested**:
  - Retrieving the list of profiles.
  - Checking the response status code.
  - Ensuring the correct number of profiles and correct data is returned.
- **Why**: To ensure that profiles can be listed, which is essential for displaying user information.

<hr />

**test_retrieve_profile_detail**
- **Purpose**: To verify that a specific profile can be retrieved.
- **What was tested**:
  - Retrieving a specific profile's details.
  - Checking the response status code.
  - Ensuring the correct profile data is returned.
- **Why**: To ensure that individual profile details can be fetched, which is necessary for viewing user profiles.

<hr />

**test_update_profile**
- **Purpose**: To verify that a user can update their profile.
- **What was tested**:
  - Updating profile details.
  - Checking the response status code.
  - Ensuring the profile data is updated in the database.
- **Why**: To ensure that users can modify their profile information.

<hr />

**test_non_owner_cannot_update_profile**
- **Purpose**: To verify that users cannot update profiles they do not own.
- **What was tested**:
  - Attempting to update another user's profile.
  - Checking the response status code.
  - Ensuring the profile data is not updated in the database.
- **Why**: To maintain data integrity and security by ensuring that only profile owners can update their profiles.

<hr />

</details>

<details>
<summary>recipes</summary>

### Summary
These tests cover the core functionalities of the Recipe model in the application. They ensure that users can create, retrieve, update, and delete recipes, while also enforcing permissions so that only the recipe owner can make modifications or deletions.

<hr />

**test_create_recipe**
- **Purpose**: To verify that a user can create a new recipe.
- **What was tested**:
  - Creating a new recipe with valid data.
  - Checking the response status code.
  - Ensuring the new recipe is added to the database.
- **Why**: To confirm that the recipe creation functionality works as intended.

<hr />

**test_retrieve_recipes_list**
- **Purpose**: To ensure the recipes list can be retrieved.
- **What was tested**:
  - Retrieving the list of recipes.
  - Checking the response status code.
  - Verifying the correct number of recipes is returned.
- **Why**: To verify that the recipe listing functionality works correctly.

<hr />

**test_retrieve_recipe_detail**
- **Purpose**: To ensure that a specific recipe's details can be retrieved.
- **What was tested**:
  - Retrieving a specific recipe's details.
  - Checking the response status code.
  - Verifying the returned recipe details are correct.
- **Why**: To confirm that the recipe detail retrieval functionality works as expected.

<hr />

**test_update_recipe**
- **Purpose**: To verify that a user can update their own recipe.
- **What was tested**:
  - Updating a recipe's details.
  - Checking the response status code.
  - Ensuring the recipe details are updated in the database.
- **Why**: To ensure that the recipe update functionality works correctly.

<hr />

**test_delete_recipe**
- **Purpose**: To verify that a user can delete their own recipe.
- **What was tested**:
  - Deleting a recipe.
  - Checking the response status code.
  - Ensuring the recipe is removed from the database.
- **Why**: To confirm that the recipe deletion functionality works as intended.

<hr />

**test_non_owner_cannot_update_recipe**
- **Purpose**: To ensure that a user cannot update another user's recipe.
- **What was tested**:
  - Attempting to update another user's recipe.
  - Checking the response status code.
  - Ensuring the recipe details are not changed in the database.
- **Why**: To maintain data integrity and security by preventing unauthorized updates.

<hr />

**test_non_owner_cannot_delete_recipe**
- **Purpose**: To ensure that a user cannot delete another user's recipe.
- **What was tested**:
  - Attempting to delete another user's recipe.
  - Checking the response status code.
  - Ensuring the recipe is not removed from the database.
- **Why**: To maintain data integrity and security by preventing unauthorized deletions.

<hr />

</details>

### Manual testing

<details>
  <summary>comments</summary>

  <hr />
  
  **Test: Create Comment**
  - **Purpose**: To verify that a logged-in user can create a comment on a recipe.
  - **Expected Result**: The comment should be successfully created and associated with the correct recipe and user.
  - **Method**:
    1. Log in as a test user.
    2. Send a POST request to `/comments/` with the recipe ID and comment content.
    3. Check the response status and data.
  - **Result**:
    - Status code: 201 Created
    - Response contains the new comment data with correct recipe and user IDs.

    <hr />
  
  **Test: Retrieve Comments List**
  - **Purpose**: To verify that the comments list can be retrieved.
  - **Expected Result**: A list of comments is retrieved and displayed.
  - **Method**:
    1. Log in as a test user.
    2. Send a GET request to `/comments/`.
    3. Check the response status and data.
  - **Result**:
    - Status code: 200 OK
    - Response contains a list of comments.

    <hr />
  
  **Test: Update Comment**
  - **Purpose**: To verify that a user can update their own comment.
  - **Expected Result**: The comment is successfully updated.
  - **Method**:
    1. Log in as the comment owner.
    2. Send a PUT request to `/comments/{id}` with the updated content.
    3. Check the response status and data.
  - **Result**:
    - Status code: 200 OK
    - Response contains the updated comment data.

    <hr />
  
  **Test: Delete Comment**
  - **Purpose**: To verify that a user can delete their own comment.
  - **Expected Result**: The comment is successfully deleted.
  - **Method**:
    1. Log in as the comment owner.
    2. Send a DELETE request to `/comments/{id}`.
    3. Check the response status.
  - **Result**:
    - Status code: 204 No Content
    - Comment is removed from the database.

    <hr />
  
</details>



<details>
  <summary>followers</summary>

  <hr />

**Test: Follow User**
- **Purpose**: To verify that a user can follow another user.
- **Expected Result**: The user is successfully followed.
- **Method**:
  1. Log in as a test user.
  2. Send a POST request to `/followers/` with the followed user ID.
  3. Check the response status and data.
- **Result**: 
  - Status code: 201 Created
  - Response contains the new follower data.

  <hr />

**Test: Unfollow User**
- **Purpose**: To verify that a user can unfollow another user.
- **Expected Result**: The user is successfully unfollowed.
- **Method**:
  1. Log in as a test user.
  2. Send a DELETE request to `/followers/{id}`.
  3. Check the response status.
- **Result**: 
  - Status code: 204 No Content
  - Follower relationship is removed from the database.

  <hr />

  </details>


<details>
  <summary>likes</summary>

  <hr />

**Test: Like Recipe**
- **Purpose**: To verify that a user can like a recipe.
- **Expected Result**: The recipe is successfully liked.
- **Method**:
  1. Log in as a test user.
  2. Send a POST request to `/likes/` with the recipe ID.
  3. Check the response status and data.
- **Result**: 
  - Status code: 201 Created
  - Response contains the new like data.

  <hr />

**Test: Unlike Recipe**
- **Purpose**: To verify that a user can unlike a recipe.
- **Expected Result**: The recipe is successfully unliked.
- **Method**:
  1. Log in as a test user.
  2. Send a DELETE request to `/likes/{id}`.
  3. Check the response status.
- **Result**: 
  - Status code: 204 No Content
  - Like is removed from the database.

  <hr />

  </details>

<details>
  <summary>profiles</summary>

  <hr />

**Test: View Profile**
- **Purpose**: To verify that a user can view their profile and other users' profiles.
- **Expected Result**: The profile information is displayed correctly.
- **Method**:
  1. Send a GET request to `/profiles/{id}`.
  2. Check the response status and data.
- **Result**: 
  - Status code: 200 OK
  - Response contains the profile information.

  <hr />

**Test: Edit Profile**
- **Purpose**: To verify that a user can edit their profile information.
- **Expected Result**: The profile is successfully updated.
- **Method**:
  1. Log in as a test user.
  2. Send a PUT request to `/profiles/{id}` with updated profile data.
  3. Check the response status and data.
- **Result**: 
  - Status code: 200 OK
  - Response contains the updated profile data.

  <hr />

  </details>

<details>
  <summary>recipes</summary>

  <hr />

**Test: Create Recipe**
- **Purpose**: To verify that a user can create a new recipe.
- **Expected Result**: The recipe is successfully created and listed.
- **Method**:
  1. Log in as a test user.
  2. Send a POST request to `/recipes/` with the recipe data.
  3. Check the response status and data.
- **Result**: 
  - Status code: 201 Created
  - Response contains the new recipe data.

  <hr />

**Test: View Recipe**
- **Purpose**: To verify that a user can view a recipe's details.
- **Expected Result**: The recipe details are displayed correctly.
- **Method**:
  1. Send a GET request to `/recipes/{id}`.
  2. Check the response status and data.
- **Result**: 
  - Status code: 200 OK
  - Response contains the recipe details.

  <hr />

**Test: Edit Recipe**
- **Purpose**: To verify that a user can edit their own recipe.
- **Expected Result**: The recipe is successfully updated.
- **Method**:
  1. Log in as the recipe owner.
  2. Send a PUT request to `/recipes/{id}` with updated recipe data.
  3. Check the response status and data.
- **Result**: 
  - Status code: 200 OK
  - Response contains the updated recipe data.

  <hr />

**Test: Delete Recipe**
- **Purpose**: To verify that a user can delete their own recipe.
- **Expected Result**: The recipe is successfully deleted.
- **Method**:
  1. Log in as the recipe owner.
  2. Send a DELETE request to `/recipes/{id}`.
  3. Check the response status.
- **Result**: 
  - Status code: 204 No Content
  - Recipe is removed from the database.

  <hr />

  </details>


## Deployment

#### Heroku Deployment
The site was deployed to Heroku. The steps to deploy are as follows:

Prerequisites:
- Create 'Procfile' in your project folder(Note caps and no file tag)
- Add this

```bash
release: python manage.py makemigrations && python manage.py migrate
web: gunicorn tastehub_drf.wsgi
```
- Freeze and export our installed libraries
    - pip freeze --local > requirements.txt

<hr>

- Navigate to heroku and create an account
- Click the new button in the top right corner
- Select create new app
- Enter app name
- Select region and click create app
- Go to the settings tab and then click reveal config vars
- Make sure the following config vars exist:
  - SECRET_KEY: (Your secret key)
  - DATABASE_URL: (Database url)
  - CLOUDINARY_URL: (cloudinary api url)
  - ALLOWED_HOST: (url of heroku app you just created)
  - CLIENT_ORIGIN: (Frontend url)
  - CLIENT_ORIGIN_DEV: (frontend url when running the server in your dev env.)
- Click the deploy tab
- Scroll down to Connect to GitHub and sign in / authorize when prompted
- In the search box, find the repositoy you want to deploy and click connect
- Scroll down to Manual deploy and choose the main branch
- Click deploy
- Double check that the worker(Dyno) is enabled under resources

The app should now be deployed.


# Run Locally
Note that you need your own Postgres database and Cloudinary api.

Clone the project

```bash
  git clone https://github.com/zimmoc/tastehub-drf.git
```

Install dependencies
- Recommended to do this in a virtual python env


```bash
  pip install -r requirements.txt
```

Set environment variables in env.py file

```bash
import os

os.environ['CLOUDINARY_URL']= ""
os.environ['DEV'] = '1' // # Debug mode on
os.environ['DATABASE_URL'] = ""
os.environ.setdefault("SECRET_KEY", "YOUR_KEY_GOES_HERE")
os.environ['CLIENT_ORIGIN'] = "http://localhost"
os.environ['CLIENT_ORIGIN_DEV'] = "http://localhost"
```

Start the server

```bash
  python3 manage.py runserver
```
