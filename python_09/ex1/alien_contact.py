from pydantic import BaseModel, model_validator, Field, ValidationError
from datetime import datetime
from typing import Optional
from enum import Enum


class ContactType(Enum):
    radio = "radio"
    visual = "visual"
    physical = "physical"
    telepathic = "telepathic"


class AlienContact(BaseModel):
    contact_id: str = Field(...,
                            min_length=5,
                            max_length=15,
                            description="Unique alphanumeric identifier"
                            "for the contact event")

    timestamp: datetime = Field(...,
                                description="UTC date and time"
                                "when the contact was initiated")

    location: str = Field(...,
                          min_length=3,
                          max_length=100,
                          description="Geographic coordinates or "
                          "named location of the encounter")

    contact_type: ContactType = Field(...,
                                      description="The classification of"
                                      " the alien encounter")

    signal_strength: float = Field(..., ge=0.0, le=10.0,
                                   description="Measured intensity of the "
                                   "transmission or presence on a 0-10 scale")

    duration_minutes: int = Field(...,
                                  ge=1,
                                  le=1440,
                                  description="Total length of the "
                                  "encounter in minutes (max 24 hours)")

    witness_count: int = Field(...,
                               ge=1,
                               le=100,
                               description="Number of individuals who"
                               "observed the event")

    message_received: Optional[str] = Field(None,
                                            max_length=500,
                                            description="Transcribed content "
                                            "of any communication received")

    is_verified: bool = Field(False,
                              description="Official status flag "
                              "indicating if the event has been authenticated")

    @model_validator(mode='after')
    def validation_custom(self) -> 'AlienContact':
        if not self.contact_id.startswith('AC'):
            raise ValueError("The Contact ID Must Start With 'AC'")
        if not self.is_verified:
            raise ValueError("Refused : Inverified Contact !")
        if self.witness_count < 3:
            raise ValueError("Telepathic contact requires "
                             "at least 3 witnesses")
        if self.signal_strength <= 7.0:
            raise ValueError("Recieved Signal is Weak !")
        return self


def main() -> None:
    print("Alien Contact Log Validation")
    print("======================================")
    try:
        alien_contact = AlienContact(contact_id="AC_2024_001",
                                     contact_type=ContactType.radio,
                                     location="Area 51, Nevada",
                                     signal_strength=8.5,
                                     duration_minutes=45, witness_count=5,
                                     timestamp=datetime.now(),
                                     is_verified=True,
                                     message_received="'Greetings from "
                                     "Zeta Reticuli'")

        print("Valid contact report:")
        print("ID:", alien_contact.contact_id)
        print("Type:", alien_contact.contact_type.value)
        print("Location:", alien_contact.location)
        print(f"Signal: {alien_contact.signal_strength}/10")
        print(f"Duration: {alien_contact.duration_minutes} minutes")
        print("Witnesses:", alien_contact.witness_count)
        print("Message:", alien_contact.message_received)

    except ValidationError as e:
        print(f"Unexpected error in valid data: {e}")

    print("\n======================================")

    print("Expected validation error:")
    try:
        invalid_contact = AlienContact(contact_id="AC_2024_001",
                                       contact_type=ContactType.radio,
                                       location="Area 51, Nevada",
                                       signal_strength=8.5,
                                       duration_minutes=45,
                                       witness_count=1,
                                       timestamp=datetime.now(),
                                       is_verified=True,
                                       message_received="'Greetings from "
                                       "Zeta Reticuli'")
        invalid_contact.contact_id
    except ValidationError as e:
        for error in e.errors():
            if 'Value error' in error['msg']:
                valid = error['msg'].split(',')
                print(valid[1].strip())
            else:
                print(error['msg'])


if __name__ == "__main__":
    main()
