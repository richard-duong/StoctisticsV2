# WaifuGrabber
The python flask api for grabbing waifu images and text

## Setup
1. Install brew if you haven't already check out brew.sh

2. Install Python@3.11
`brew install Python@3.11`

3. Install the virtual environment
`python3 -m venv .venv`

4. Activate the virtual environment
`source .venv/bin/activate`

5. Upgrade pip
`pip install --upgrade pip`

6. Install the requirements
`pip install -r requirements.txt`

7. Run the server (from the WaifuGrabber directory)
`python -m src.app`

## Endpoints

### Get waifu image

**Request**
```
@app.route("/get_waifu_image/<string:gender>/<int:age>")
```

**Response**
```
{
  "image_id": 6348,
  "image_url": "https://cdn.nekosapi.com/images/original/538e4de9-2972-40e8-a6fb-3bbb3b2a521c.webp"
}
```