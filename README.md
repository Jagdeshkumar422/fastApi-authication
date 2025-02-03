**Interview Task: Implement a RESTful Authentication API Using FastAPI and JWT**

**Objective:**

Develop a RESTful API that handles user authentication using FastAPI and JSON Web Tokens (JWT). The API should support user registration, login, and access to a protected route that requires valid JWT authentication.

**Task Requirements:**

1. **User Registration Endpoint (`/register`):**
   - Accepts `username` and `password` in the request body.
   - Hashes the password before storing it to ensure security.
   - Stores the user credentials securely.
   - Returns a success message upon successful registration.

2. **User Login Endpoint (`/login`):**
   - Accepts `username` and `password` in the request body.
   - Verifies the credentials against the stored data.
   - Upon successful authentication, generates a JWT token with an expiration time.
   - Returns the JWT token to the client.

3. **Protected Endpoint (`/protected`):**
   - Accessible only to users with a valid JWT token.
   - Returns a message confirming access to the protected route.

**Implementation Details:**

- **Password Hashing:** Use the `passlib` library with the Bcrypt algorithm to hash and verify passwords.

- **JWT Handling:** Utilize the `PyJWT` library to encode and decode JWT tokens. Ensure that tokens are signed with a secret key and have an appropriate expiration time.

- **Security:** Implement OAuth2 password flow with JWT token authentication using FastAPI's `OAuth2PasswordBearer`.

**Instructions:**

1. **Project Setup:**
   - Initialize a new FastAPI project.
   - Set up the necessary dependencies, including `passlib` and `PyJWT`.

2. **Database (Optional):**
   - For simplicity, you can use an in-memory data structure to store user credentials.
   - Ensure that the data structure is thread-safe if the application is run with multiple workers.

3. **Environment Variables:**
   - Store sensitive information, such as the JWT secret key, in environment variables.

4. **Testing:**
   - Provide examples of how to test each endpoint using `curl` or any API testing tool.
   - Ensure that the protected endpoint is accessible only with a valid JWT token.

**Evaluation Criteria:**

- Correctness: The API should meet all specified requirements.
- Security: Passwords must be hashed, and JWT tokens should be securely generated and validated.
- Code Quality: The code should be well-organized, readable, and follow best practices.
- Documentation: Clear instructions on how to set up, run, and test the application.
- Optionl Task: Good to have but not necessary to have databae integrated.
