# SvelteKit-Python-Sklearn-Demo

It's as simple as that.

## How to set up

### Step 1: Clone the repository

Open a terminal and run the commands

```
git clone https://github.com/shahank42/sveltekit-python-sklearn-demo
cd sveltekit-python-sklearn-demo
```

### Step 2: Initialize the backend

In the same terminal run

```
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python backend/server.py
```

Note: If you use the FISH shell, then the second command should be `source .venv/bin/activate.fish`

Note: If you use Windows, then the second command should be `.venv/Scripts/activate.bat` for CMD and `.venv/Scripts/Activate.ps1` for Powershell

### Step 3: Initialize the frontend

Open a new terminal and navigate to the root project directory.
Then run

```
npm install
npm run dev

```

### Step 4: Profit??

Go to http://localhost:5173 and look at the gloriousness of a web app running a Python-trained model.


### (Step 5: Re-train the model)

This is a super duper uber simple ML model trained using scikit-learn.

You can check out the `backend/ai` folder for deets.

But if you wanna retrain the model, simply run:

```
python ai/xor_problem.py
```

from inside the `backend` folder.


---

made by shahank one fine afternoon.
