from app.services.ProfileService import ProfileServices
from app import ProfileApp
from app.utils.response import Response

class ProfileControllers:
    def __init__(self):
        self.sessios = ProfileApp().get_session

    def create_profile_controller(self, id, data):
        
        with self.sessios() as session:
            services = ProfileServices(session)
            try:
                profile = services.create_profile_services(id, data)
                if profile:
                    return Response.success(200, "Profile created successfully", data=profile.to_dict())
                else:
                    return Response.error(400, "Profile not created")
            except RuntimeError as e:
                return Response.error(400, "Profile not created", errors=e)
        
    def get_profile_controller(self, id):
        with self.sessios() as session:
            services = ProfileServices(session)
            try:
                profile = services.get_profile_services(id)
                if profile:
                    data = {
                        "id": profile.id,
                        "f_name": profile.f_name,
                        "l_name": profile.l_name,
                        "address": profile.address,
                        "phone_number": profile.phone_number,
                        "pfp": profile.pfp,
                        "username": profile.user.username,
                        "email": profile.user.email,
                    }
                    return Response.success(200, "Profile fetched successfully", data=data)
                else:
                    return Response.error(404, "Profile not found")
            except RuntimeError as e:
                return Response.error(400, "Profile not fetches", errors=e)