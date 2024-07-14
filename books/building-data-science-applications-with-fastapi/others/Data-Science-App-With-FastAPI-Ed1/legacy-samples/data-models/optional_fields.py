from datetime import datetime
from typing import Optional
from pydantic import BaseModel
import time


# class UserProfile(BaseModel):
#     nickname: str
#     location: Optional[str] = None
#     # subscribed_newsletter: bool = True
#     subscribed_newsletter: Optional[bool] = None


# user = UserProfile(nickname="jdoe")
# print(user)  # nickname='jdoe' location=None subscribed_newsletter=True


class Model(BaseModel):
    # Don't do this.
    # This example shows you why it doesn't work.
    d: datetime = datetime.now()


o1 = Model()
print(o1.d)

time.sleep(1)  # Wait for a second

o2 = Model()
print(o2.d)

print(o1.d < o2.d)  # False
