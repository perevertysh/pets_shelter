from .views import (OwnerViewSet,
                    PetShelteringRequestViewSet,
                    RegistrationViewSet)

routes = [
    (r'owner', OwnerViewSet),
    (r'pet_shelter_req', PetShelteringRequestViewSet),
    (r'registration', RegistrationViewSet)
]
