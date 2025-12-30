import random
import string
from models import User, get_session

def lambda_handler(event, context):
    session = get_session()
    
    # Note: Creating the table here for simplicity in this MVE.
    # In a production environment, this should be handled separately.
    User.__table__.create(session.get_bind(), checkfirst=True)
    
    name = "".join(random.choices(string.ascii_letters, k=8))
    user = User(name=name, email=f"{name}@example.com")
    
    session.add(user)
    session.commit()
    
    print(f"User {name} created successfully!")
    return {"status": "success", "user": name}
