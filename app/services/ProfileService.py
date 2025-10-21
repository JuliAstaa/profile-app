from app.models.profile import Profile

class ProfileServices:
    def __init__(self, session):
        self.session = session
    
    def create_profile_services(self, id, data):
        try:
            profile = self.session.query(Profile).filter_by(id_user=id).first()
            if not profile:
                return None
            
            profile.f_name = data.get("f_name")
            profile.l_name = data.get("l_name")
            profile.address = data.get("address")
            profile.phone_number = data.get("phone_number")
            profile.pfp = data.get("pfp")

            self.session.commit()
            return profile
        except Exception as e:
            self.session.rollback()
            raise e

    
    def get_profile_services(self, id):
        try:
            profile = self.session.query(Profile).filter_by(id_user=id).first()
            return profile
        except Exception as e:
            self.session.rollback()
            raise e
    