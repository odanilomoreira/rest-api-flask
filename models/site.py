from sql_alchemy import banco

class siteModel(banco.Model):
    __tablename__ = 'sites'

    site_id = banco.Column(banco.Integer, primary_key=True)
    descricao = banco.Column(banco.String(80))

    hoteis = banco.relationship('hotelModel') # lista de hoteis

    def __init__(self,site_id,descricao):
        self.site_id = site_id
        self.descricao = descricao

    def json(self):
        return {"site_id": self.site_id,
                "descricao": self.descricao,
                "hoteis": self.hoteis # temos que ter os hoteis para exibir
                }

    @classmethod
    def find_site(cls, site_id):
        site = cls.query.filter_by(site_id=site_id).first()
        if site:
            return site
        return None

    def save_site(self):
        banco.session.add(self)
        banco.session.commit()

    def update_site(self, descricao):
        self.descricao = descricao

    def delete_site(self):
        banco.session.delete(self)
        banco.session.commit()
