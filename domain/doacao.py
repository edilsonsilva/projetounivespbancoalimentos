from flask.json import jsonify
import traceback

import pymysql


class Doacao:
    def __init__(self, idproduto=None, iddoador=None, quantidade=None):
        self.idproduto = idproduto
        self.iddoador = iddoador
        self.quantidade = quantidade

        self.conn = pymysql.connect(host='x8autxobia7sgh74.cbetxkdyhwsb.us-east-1.rds.amazonaws.com',
                                    user='uno1istjd900u7yk',
                                    password='igwvpvp6i7xfmrsk',
                                    database='fvr0dnbv5n7s7oip',
                                    charset='utf8mb4',
                                    cursorclass=pymysql.cursors.DictCursor)

    def cadastroDoacao(self):
        try:
            with self.conn.cursor() as cur:
                sql = "INSERT INTO `doacao`(`idproduto`, `iddoador`, `quantidade`)VALUES(%s, %s, %s)"
                cur.execute(sql, (self.idproduto, self.iddoador,
                            self.quantidade))
                self.conn.commit()
        except:
            print("Erro ao tentar cadastrar os dados")
            traceback.print_exc()
        finally:
            self.conn.close()

        self.conn = pymysql.connect(host='localhost',
                                    user='root',
                                    password='',
                                    database='bancoalimentos',
                                    charset='utf8mb4',
                                    cursorclass=pymysql.cursors.DictCursor)

    def cadastroDoacao(self):
        try:
            with self.conn.cursor() as cur:
                sql = "INSERT INTO `doacao` (`idproduto`, `iddoador`, `quantidade`)VALUES(%s, %s, %s)"
                cur.execute(
                    sql, (self.idproduto, self.iddoador, self.quantidade))
                self.conn.commit()
                nome = cur.execute(
                    "select nomeproduto from produto where idproduto=%s", self.idproduto)
                cur.execute("call atualizar_estoque(?,?,?)",
                            self.idproduto, nome, self.quantidade)
                self.conn.commit()
        except:
            print("Erro ao tentar cadastrar os dados")
            traceback.print_exc()
        finally:
            self.conn.close()

    def listarDoacao(self):
        try:
            with self.conn.cursor() as cur:
                cur.execute("SELECT * FROM doacao")
                result = cur.fetchall()
                return jsonify(result)
        except:
            print("Erro ao tentar listar doacoes")
        finally:
            self.conn.close()

    def totalDoacaoInicio(self):
        try:
            with self.conn.cursor() as cur:
                cur.execute(
                    "select sum(quantidade) as total from doacao")
                result = cur.fetchall()
                return jsonify(result)
        except:
            print("Erro ao tentar calcular o total de doacoes")
        finally:
            self.conn.close()

    def totalDoacao24(self):
        try:
            with self.conn.cursor() as cur:
                cur.execute(
                    "select sum(quantidade) as total from doacao where date(datadoacao) = curdate()-1")
                result = cur.fetchall()
                return jsonify(result)
        except:
            print("Erro ao tentar calcular o total de doacoes")
        finally:
            self.conn.close()
