import strawberry
from typing import List
from .api_utils import fetch_company_data
from .models import Lead, Deal

@strawberry.django.type(Deal)
class DealType:
    id: strawberry.ID
    name: str
    value: float
    status: str

@strawberry.django.type(Lead)
class LeadType:
    id: strawberry.ID
    first_name: str
    last_name: str
    company_id: int

    @strawberry.field
    def company_name(self) -> str:
        data = fetch_company_data(self.company_id)
        return data.get('name', 'Unknown') if data else 'Unknown'

    @strawberry.field
    def company_domain(self) -> str:
        data = fetch_company_data(self.company_id)
        return data.get('domain', 'N/A') if data else 'N/A'

    deals: List[DealType]

@strawberry.type
class Query:
    @strawberry.field
    def all_leads(self) -> List[LeadType]:
        return Lead.objects.all()

@strawberry.type
class Mutation:
    @strawberry.mutation
    def create_lead(self, first_name: str, last_name: str, company_id: int) -> LeadType:
        lead = Lead.objects.create(
            first_name=first_name, 
            last_name=last_name, 
            company_id=company_id
        )
        return lead

    @strawberry.mutation
    def create_deal(self, name: str, value: float, lead_id: int) -> DealType:
        try:
            lead = Lead.objects.get(id=lead_id)
            
            deal = Deal.objects.create(
                name=name, 
                value=value, 
                lead=lead, 
                company_id=lead.company_id,
                status="OPEN"
            )

            # IMPORTANT: If your Kafka code fails here, the function returns None 
            # and triggers the "Cannot return null" error.
            try:
                # Replace this with your actual Kafka producer call
                print(f"Sending deal {deal.id} to Kafka...") 
            except Exception as e:
                print(f"Kafka failed but deal was saved: {e}")

            return deal # <-- Ensure this is outside any inner try/except blocks

        except Lead.DoesNotExist:
            raise Exception(f"Lead with ID {lead_id} does not exist")

# REGISTER BOTH HERE
schema = strawberry.Schema(query=Query, mutation=Mutation)