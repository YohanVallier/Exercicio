def criar_servidor(hostname, ram_total):
    dict_serv = {
        "hostname": hostname,
        "ram_total": ram_total,
        "ram_usada": 0,
        "historico": []
    }

def rodar_processo(servidor, nome_processo, ram_necessaria):
    if servidor["ram_usada"] + ram_necessaria <= servidor["ram_total"]:
        servidor["ram_usada"] += ram_necessaria

    if len(servidor["historico"]) < nome_processo:
        return print("Memória insuficiente")

    else:
        servidor["histórico"] += nome_processo

def exibir_status(servidor):
    return print(f"O hostname é {servidor["hostname"]} e o total de RAM usada é de {servidor["ram_total"]}")


criar_servidor("web_func", "16GB")
criar_servidor("db_func", "64GB")

class Servidor:
    def __init__(self, hostname, ram_total):
        self.hostname = hostname
        self.ram_total = ram_total
        self.ram_usada = 0
        self.historico = []

    def rodar_processo(self, nome_processo, ram_necessaria):
        self.ram_necessaria = ram_necessaria
        self.nome_processo = nome_processo

        if self.ram_usada + ram_necessaria <= self.ram_total:
                self.ram_usada += ram_necessaria
                self.historico.append(nome_processo)
        else:
            return print("Memória insuficiente")

    def exibir_status(self):
        print(f"Status {self.hostname}: {self.ram_usada}GB / {self.ram_total}GB | Processos: {self.historico}")

web_obj = Servidor("SRV-WEB-01", 16)
db_obj = Servidor("SRV-DB-02", 64)

web_obj.rodar_processo("nginx", 4)
web_obj.rodar_processo("python_etl", 14)   # Falha: 4 + 14 = 18 > 16
db_obj.rodar_processo("postgres", 32)

web_obj.exibir_status()
db_obj.exibir_status()