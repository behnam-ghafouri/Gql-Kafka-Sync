import strawberry
from strawberry import relay
from typing import List, Optional
from .models import Company, User



@strawberry.federation.type(keys=["id"])
class CompanyType:
    id: strawberry.ID
    name: str

    @strawberry.field
    def parent(self) -> Optional["CompanyType"]:
        return Company.objects.get(id=self.parent_id) if self.parent_id else None


@strawberry.federation.type(keys=["id"])
class UserType:
    id: strawberry.ID
    username: str
    role: str

    @strawberry.field
    def company(self) -> CompanyType:
        return self.company


@strawberry.type
class Query:
    @strawberry.field
    def me(self) -> Optional[UserType]:
        # This will be used by the frontend to check login state
        return None

    @strawberry.field
    def companies(self) -> List[CompanyType]:
        return Company.objects.all()



@strawberry.type
class Mutation:
    @strawberry.mutation
    def create_user(
        self, 
        username: str, 
        email: str, 
        password: str,  # Add this!
        role: str = "USER" # Default role so it's not strictly required
    ) -> UserType:
        user = User.objects.create_user( # .create_user handles password hashing
            username=username, 
            email=email, 
            password=password,
            role=role
        )
        return user


schema = strawberry.federation.Schema(query=Query, mutation=Mutation)