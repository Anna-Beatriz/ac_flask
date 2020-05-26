from banco import bd


class Presenca:
    def __init__(self, email, presenca, resposta, comentarios):
        self.email = email
        self.presenca = presenca
        self.resposta = resposta
        self.comentarios = comentarios


    def gravar_presenca(self):
        sql = '''insert into presenca (email, presenca, resposta, comentarios) values (?, ?, ?, ?)'''
        primeiro_interrogacao = self.email
        segundo_interrogacao = self.presenca
        terceiro_interrogacao = self.resposta
        quarto_interrogacao = self.comentarios
        bd().execute(sql, [primeiro_interrogacao, segundo_interrogacao, terceiro_interrogacao, quarto_interrogacao])
        bd().commit()

    @staticmethod
    def ler_presenca():
        sql = '''select email, presenca, resposta, comentarios from presenca order by id desc'''
        cur = bd().execute(sql)

        presencas = []
        for email_form, presenca_form, resposta_form, comentarios_form in cur.fetchall():
            pres = Presenca(email_form, presenca_form, resposta_form, comentarios_form)
            presencas.append(pres)
        return presencas
