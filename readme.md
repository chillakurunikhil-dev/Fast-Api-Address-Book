FastAPI Address Book – Minimal Assignment Project

This project is a small Address Book API built using FastAPI.
The idea is to keep everything simple and only cover what was clearly asked in the assignment.
Users can add an address, update it, delete it, view all addresses, and also find which addresses fall within a certain distance from a given location.

The addresses are stored in a local SQLite database, and all inputs (especially coordinates) are validated before saving.

⸻

What this project does
	•	Store basic address information (name, latitude, longitude)
	•	Let API users create, update, delete, and view addresses
	•	Validate coordinate values
	•	Save everything in SQLite
	•	Find addresses near a given location using a distance filter
	•	Provide a clean and simple Swagger documentation (no UI needed)


⸻

Tech used
	•	FastAPI
	•	SQLite
	•	SQLAlchemy
	•	Pydantic
	•	Uvicorn

⸻

How to run locally
	1.	Install dependencies: pip install -r requirements.txt

	2.	Start the server: uvicorn main:app --reload

	3.	After the server starts, open the API docs: http://127.0.0.1:8000/docs

Endpoints included

1. Create a new address

POST /addresses/

2. Get all saved addresses

GET /addresses/

3. Update an address

PUT /addresses/{id}

4. Delete an address

DELETE /addresses/{id}

5. Find nearby addresses

GET /addresses/nearby?lat=…&lon=…&distance_km=…