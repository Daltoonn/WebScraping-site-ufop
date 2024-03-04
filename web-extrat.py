import requests
from bs4 import BeautifulSoup

#DECSI

class WebScraper: #abstrair o processo de web scraping
    def __init__(self, url):
        self.url = url
        self.page = requests.get(url)  # Encapsulamento
        self.soup = BeautifulSoup(self.page.content, "html.parser")  # Encapsulamento

    def extract_data(self):
        pass

#classes filhas
class NameScraper(WebScraper):
    def extract_data(self): #Polimorfismo
        names = []
        name_elements = self.soup.find_all('span', {'style': 'color:#800000;'})
        for name_element in name_elements:
            names.append(name_element.text)
        return names

class EmailScraper(WebScraper):
    def extract_data(self): #Polimorfismo
        emails = []
        emails_elements = self.soup.find_all('a')
        for emails_element in emails_elements:
             if '@' in emails_element.text:
                emails.append(emails_element.text)
        return emails

class LinhaPesquisaScraper(WebScraper):
    def extract_data(self): #Polimorfismo
        linhapesq = []
        linhapesq_elements = self.soup.find_all('span')
        for linhapesq_element in linhapesq_elements:
           if 'Linha' in linhapesq_element.text:
            linhapesq.append(linhapesq_element.text)
        return linhapesq

#DEENP

class NameScraperr(WebScraper):
    def extract_data(self):
        names = []
        name_elements = self.soup.find_all('td')
        for name_element in name_elements:
          if "Prof" in name_element.text:
            names.append(name_element.text)
        return names

class EmailScraperr(WebScraper):
    def extract_data(self):
        emails = []
        emails_elements = self.soup.find_all('a')
        for emails_element in emails_elements:
             if '@' in emails_element.text:
                emails.append(emails_element.text)
        return emails

class LinhaPesquisaScraperr(WebScraper):
    def extract_data(self):
        linhapesq = []
        linhapesq_elements = self.soup.find_all('span', {'style' : 'font-size:9px;'})
        for linhapesq_element in linhapesq_elements:
            linhapesq.append(linhapesq_element.text)
        return linhapesq

class SalaScraperr(WebScraper):
    def extract_data(self):
        sala = []
        sala_elements = self.soup.find_all('td')
        for sala_element in sala_elements:
           if 'A2' in sala_element.text:
            sala.append(sala_element.text)
        return sala

class RamalScraperr(WebScraper):
    def extract_data(self):
        ramal = []
        ramal_elements = self.soup.find_all('td', {'style' : 'text-align: center;'})
        for ramal_element in ramal_elements:
           if '0' in ramal_element.text:
            ramal.append(ramal_element.text)
        return ramal



# Exemplo de uso da classe
if __name__ == "__main__":


    #decsi
    url = "https://decsi.ufop.br/docentes"
    name_scraper = NameScraper(url) # Herança: NameScraperr herda de WebScraperr
    email_scraper = EmailScraper(url)
    linhapesq_scraper = LinhaPesquisaScraper(url)

    # Extração de dados usando polimorfismo ele pode fazer coisas diferentes em cada classe.
    extracted_names = name_scraper.extract_data()
    extracted_emails = email_scraper.extract_data()
    extracted_linhapesq = linhapesq_scraper.extract_data()

    print("--------------PROFESSORES DO DECSI--------------")

    print("Nomes Extraídos:")
    print(extracted_names)
    print("Emails Extraídos:")
    print(extracted_emails)
    print("Linha de pesquisa:")
    print(extracted_linhapesq)


    #deenp
    urll = "https://deenp.ufop.br/corpo-docente"
    namee_scraper = NameScraperr(urll)
    emaill_scraper = EmailScraperr(urll)
    linhapesqq_scraper = LinhaPesquisaScraperr(urll)
    sala_scraper = SalaScraperr(urll)
    ramal_scraper = RamalScraperr(urll)

    extracted_namess = namee_scraper.extract_data()
    extracted_emailss = emaill_scraper.extract_data()
    extracted_linhapesqq = linhapesqq_scraper.extract_data()
    extracted_sala = sala_scraper.extract_data()
    extracted_ramal = ramal_scraper.extract_data()

    print("\n");
    print("--------------PROFESSORES DO DEENP--------------")
    print("Nomes Extraídos:")
    print(extracted_namess)
    print("Emails Extraídos:")
    print(extracted_emailss)
    print("Linha de pesquisa:")
    print(extracted_linhapesqq)
    print("Sala:")
    print(extracted_sala)
    print("Ramal:")
    print(extracted_ramal)

    area = input("Digite a área (DECSI ou DEENP): ").upper()
    if area == "DECSI":
        url = "https://decsi.ufop.br/docentes"
    elif area == "DEENP":
        url = "https://deenp.ufop.br/corpo-docente"
    else:
        print("Área não reconhecida.")
        exit()

     # Criando instância da classe relevante
    if area == "DECSI":
        scraper = NameScraper(url)
    else:
        scraper = LinhaPesquisaScraper(url)

    # Extração de dados
    extracted_data = scraper.extract_data()

    # Exibindo dados extraídos
    print("--------------PROFESSORES--------------")
    for data in extracted_data:
        print(data)

