from pydantic import BaseModel, Field, ValidationError, model_validator
from datetime import datetime
from typing import List
from enum import Enum


class Rank(Enum):
    cadet = "cadet"
    officer = "officer"
    lieutenant = "lieutenant"
    captain = "captain"
    commander = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(..., min_length=3,
                           max_length=10,
                           description="Unique alphanumeric "
                           "identifier for the crew personnel")

    name: str = Field(..., min_length=2,
                      max_length=50,
                      description="Full legal name of the crew member")

    rank: Rank = Field(...,
                       description="The official"
                       "hierarchy level of the crew member")

    age: int = Field(...,
                     ge=18,
                     le=80,
                     description="Age of the member "
                     "in years (must be within flight-ready range)")

    specialization: str = Field(...,
                                min_length=3, max_length=30,
                                description="Primary technical expertise "
                                "(e.g., Pilot, Engineer, Biologist)")

    years_experience: int = Field(..., ge=0, le=50,
                                  description="Total number "
                                  "of years active in "
                                  "space-related industries")

    is_active: bool = Field(True, description="Status flag indicating "
                            "if the member is currently cleared for duty")


class SpaceMission(BaseModel):
    mission_id: str = Field(..., min_length=5, max_length=15,
                            description="Unique reference "
                            "code for the specific space mission")

    mission_name: str = Field(..., min_length=3, max_length=100,
                              description="The formal public "
                              "name of the exploration mission")

    destination: str = Field(..., min_length=3, max_length=50,
                             description="Target celestial "
                             "body or orbital coordinate")

    launch_date: datetime = Field(..., description="The "
                                  "scheduled date and time"
                                  "for mission departure")

    duration_days: int = Field(..., ge=1, le=3650,
                               description="Estimated length "
                               "of the mission in Earth days")

    crew: List[CrewMember] = Field(..., min_length=1, max_length=12,
                                   description="List of personnel "
                                   "assigned to this specific mission")

    mission_status: str = Field("planned",
                                description="Current operational phase "
                                "of the mission (e.g., planned, in-progress)")

    budget_millions: float = Field(..., ge=1.0, le=10000.0,
                                   description="Total allocated financial "
                                   "resources in millions of credits/dollars")

    @model_validator(mode='after')
    def validation_mission(self) -> "SpaceMission":
        if not self.mission_id.startswith('M'):
            raise ValueError("Mission ID Must Start With 'M'")
        if self.duration_days > 365:
            for rank in self.crew:
                if rank.years_experience < 5:
                    raise ValueError("Mission Denied: A Mission of "
                                     "+365 days need experienced "
                                     "crew member [ +5 Years ]")
                if not rank.is_active:
                    raise ValueError(f"The {rank.rank} is Not Active - All "
                                     "Crew Members Must Be Active")
        missing = False
        for member in self.crew:
            if member.rank.value in ['captain', 'commander']:
                missing = True
                break

        if not missing:
            raise ValueError("Mission must have at "
                             "least one Commander or Captain")
        return self


def Main() -> None:
    print("Space Mission Crew Validation")
    print("=========================================")
    try:
        connor = CrewMember(member_id="C-7451", name="Sarah Connor",
                            rank=Rank.commander, age=49,
                            specialization="Mission Command",
                            years_experience=24, is_active=True)
        smith = CrewMember(member_id="L-6231", name="John Smith",
                           rank=Rank.lieutenant, age=41,
                           specialization="Navigation",
                           years_experience=19, is_active=True)
        johnson = CrewMember(member_id="O-3451", name="Alice Johnson",
                             rank=Rank.officer, age=24,
                             specialization="Engineering",
                             years_experience=6, is_active=True)

        invalid_officer = CrewMember(member_id="O-3657",
                                     name="carlos morgan",
                                     rank=Rank.officer, age=24,
                                     specialization="Engineering",
                                     years_experience=6, is_active=True)

        crew_members = [connor, smith, johnson]

        valid_mission = SpaceMission(mission_name="Mars Colony Establishment",
                                     mission_id="M2024_MARS",
                                     mission_status="planned",
                                     destination="Mars", duration_days=900,
                                     budget_millions=2500.0, crew=crew_members,
                                     launch_date=datetime.now())

        print("Valid mission created:")
        print("Mission", valid_mission.mission_name)
        print("ID:", valid_mission.mission_id)
        print("Destination:", valid_mission.destination)
        print("Duration:", valid_mission.duration_days, "days")
        print(f"Budget: ${valid_mission.budget_millions}M")
        print("Crew size:", len(crew_members))
        print("Crew members:")

        for member in crew_members:
            print(f"- {member.name} ({member.rank.value}) - "
                  f"{member.specialization}")

        print("\n=========================================")

        print("Expected validation error:")

        invalid_crews = [johnson, invalid_officer, smith]
        invalid_mission = SpaceMission(mission_name="Moon Crew - 51",
                                       mission_id="M2025_MOON",
                                       mission_status="planned",
                                       destination="Moon", duration_days=650,
                                       budget_millions=2600.0,
                                       crew=invalid_crews,
                                       launch_date=datetime.now())
        invalid_mission.mission_name

    except ValidationError as e:
        for error in e.errors():
            if 'Value error' in error['msg']:
                valid = error['msg'].split(',')
                print(valid[1].strip())
            else:
                print(error['msg'])


if __name__ == "__main__":
    Main()
