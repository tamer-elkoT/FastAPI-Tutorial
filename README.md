# FastAPI Full Course Reference 🚀

This repository contains my progress and code samples from the [FastAPI - A python framework | Full Course](https://www.youtube.com/watch?v=7t2alSnE2-I) by Bitfumes. Each milestone is documented with Git tags for easy navigation between different stages of the application.

---

## 🛠 Project Roadmap & Progress

### Phase 1: Foundations & Basics
- [ ] **Tutorial 01: Setup & First API** - Installation, Uvicorn, and the first GET request.
- [ ] **Tutorial 02: Path & Query Parameters** - Handling dynamic routing and URL parameters.
- [ ] **Tutorial 03: Request Body & Pydantic** - Defining data structures with Pydantic schemas.
- [ ] **Tutorial 04: Debugging** - Setting up the VS Code debugger for FastAPI.

### Phase 2: Database (SQLAlchemy ORM)
- [ ] **Tutorial 05: SQLAlchemy Setup** - Connection, Engine, and Session configuration.
- [ ] **Tutorial 06: Models & Migrations** - Creating database tables from Python classes.
- [ ] **Tutorial 07: CRUD Operations** - Implementing Create, Read, Update, and Delete logic.
- [ ] **Tutorial 08: Status Codes & Exceptions** - Proper HTTP response handling and error messages.

### Phase 3: Advanced Features
- [ ] **Tutorial 09: Response Models** - Filtering outgoing data for security and clarity.
- [ ] **Tutorial 10: User Management** - Creating users and hashing passwords with Bcrypt.
- [ ] **Tutorial 11: Relationships** - Linking Blogs to Users (One-to-Many).
- [ ] **Tutorial 12: Refactoring (APIRouter)** - Cleaning up `main.py` using modular routing.
- [ ] **Tutorial 13: Repository Pattern** - Decoupling database logic from path operations.

### Phase 4: Security & Deployment
- [ ] **Tutorial 14: JWT Authentication** - Generating and verifying JSON Web Tokens.
- [ ] **Tutorial 15: Route Protection** - Implementing OAuth2 password bearer flow.
- [ ] **Tutorial 16: Deployment** - Finalizing and deploying the API.

---

## 🔖 How to use this Repository

You can jump to the state of the code at any specific lesson by checking out the corresponding tag:

```bash
# To see the list of available tags
git tag

# To switch to a specific tutorial (e.g., Tutorial 5)
git checkout tutorial-05



To Start the server we use this command

``` bash 
uvicorn main:app --reload
```
# How to [tag] your progress

We set a tag for each lesson in the course
``` bash
git add .
git commit -m "your comment"
git tag -a tag-name -m "comment"
git push origin tag-name
```
