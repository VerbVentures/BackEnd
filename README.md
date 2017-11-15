# BackEnd
Back-End Web API for Verb Ventures

## Set Up
1. Install Python 3 (including pip)
2. Create a Virtual Environment for the project.
3. Install requirements into virtual environment from requirments.txt file. `pip install -r requirements.txt`
4. Change directories into `verb_ventures_api`
5. Run the following command `python manage.py runserver`


## JSON Examples

### Admin
```
{
    "accountKitId": "152373558829319",
    "email": "nlglover9@gmail.com",
    "user": {
        "userId": "fb030ad8-f411-4f9b-b34b-56cc8f3b6b65",
        "firstName": "Nathan",
        "lastName": "Glover"
    }
}
```

### Student
```
{
    "studentId": "815fddbe-ff38-45ae-a825-66f5233945d1",
    "user": {
        "userId": "d067bb07-3b6c-4846-ace9-0b71fc4f567a",
        "firstName": "Bob",
        "lastName": "Joe"
    },
    "admin": "1513371865405634"
}
```

### Verb
```
{
    "verbId": "ae43e485-4363-402b-a727-62f39287230f",
    "verb": "run",
    "definition": "move at a speed faster than a walk, never having both or all the feet on the ground at the same time",
    "admin": null
}
```

### VerbPack
```
{
    "verbPackId": "24f3e614-92a2-48fc-80c3-126aa3ad7831",
    "title": "Movement",
    "admin": "1513371865405634",
    "verbPackVerbs": [
        "42f29886-f9ae-4c49-8470-b87267d6133a",
        "7b207d82-1823-4d2c-9bcc-2df0ecf9a3da"
    ],
    "userVerbPacks": [
        "001d895a-a81e-41ba-aa2d-dcb45816c98c"
    ]
}
```

### Session
```
{
    "sessionId": "4a1c690e-872c-4bf6-91f5-a76e6e2c41f4",
    "sessionDt": "2017-06-11",
    "admin": "152373558829319",
    "sessionStudents": [
        "4179bc4d-49cb-435b-87ee-b64013251fe6",
        "a292c975-2c97-4eb4-80aa-cd7510b90d68"
    ]
}
```

### Get Random Verb
```
{
    "selectedVerb": {
        "verbId": "42f29886-f9ae-4c49-8470-b87267d6133a",
        "verb": "walk",
        "definition": "move at a regular and fairly slow pace by lifting and setting down each foot in turn, never having both feet off the ground at once"
    },
    "correctAnimation": {
        "animationId": "338b6fe4-1333-410a-aa09-cf505980449b",
        "imageAddress": "https://media.giphy.com/media/omHPYZttAVAAw/giphy.gif"
    },
    "invalidAnimations": [
        {
            "animationId": "dfce5e7b-9e82-4d87-97e4-50bbcbb903f1",
            "imageAddress": "https://media.giphy.com/media/kXRxVesdY8dwI/giphy.gif"
        },
        {
            "animationId": "66e00b1b-172e-43af-ab36-a11a7dfe3d8c",
            "imageAddress": "https://media.giphy.com/media/26u3ZSuG6TiKeZczu/giphy.gif"
        },
        {
            "animationId": "2b10d681-62d2-4631-be52-5c091a424884",
            "imageAddress": "https://media.giphy.com/media/3o6Ztroynp3WpqLD1u/giphy.gif"
        }
    ]
}
```
