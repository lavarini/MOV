# -*- coding: utf-8 -*-
###############################################################################
# Funções auxiliares utilizadas pelo views.py. Ao incluir algum código
# aqui, certifique-se de que não há um lugar melhor onde sua funcionalidade
# pode se encaixar.
# Geralmente os códigos aqui apenas manipulam os dados que vem de outros
# lugares, portanto fique atento se pequenas otimizações podem ser feitas nos
# métodos deste módulo.
#
# @author: Alexandre Lavarini Matoso
# @since: 26/04/2011
###############################################################################
#from crawler_lib.log import LogEntry
#log = LogEntry('eusou.utils')
from futebol.modules.localizacao.models import Continente, Pais,\
     Estado, Cidade
     
RELACAO_PAIS = {'BD': 'BGD', 'BE': 'BEL', 'BF': 'BFA', 'BG': 'BGR', 'BA': 'BIH', 'BB': 'BRB', 'WF': 'WLF', 'BL': 'BLM', 'BM': 'BMU', 'BN': 'BRN', 'BO': 'BOL', 'BH': 'BHR', 'BI': 'BDI', 'BJ': 'BEN', 'BT': 'BTN', 'JM': 'JAM', 'BV': 'BVT', 'BW': 'BWA', 'WS': 'WSM', 'BQ': 'BES', 'BR': 'BRA', 'BS': 'BHS', 'JE': 'JEY', 'BY': 'BLR', 'BZ': 'BLZ', 'RU': 'RUS', 'RW': 'RWA', 'RS': 'SRB', 'TL': 'TLS', 'RE': 'REU', 'TM': 'TKM', 'TJ': 'TJK', 'RO': 'ROU', 'TK': 'TKL', 'GW': 'GNB', 'GU': 'GUM', 'GT': 'GTM', 'GS': 'SGS', 'GR': 'GRC', 'GQ': 'GNQ', 'GP': 'GLP', 'JP': 'JPN', 'GY': 'GUY', 'GG': 'GGY', 'GF': 'GUF', 'GE': 'GEO', 'GD': 'GRD', 'GB': 'GBR', 'GA': 'GAB', 'SV': 'SLV', 'GN': 'GIN', 'GM': 'GMB', 'GL': 'GRL', 'GI': 'GIB', 'GH': 'GHA', 'OM': 'OMN', 'TN': 'TUN', 'JO': 'JOR', 'HR': 'HRV', 'HT': 'HTI', 'HU': 'HUN', 'HK': 'HKG', 'HN': 'HND', 'HM': 'HMD', 'VE': 'VEN', 'PR': 'PRI', 'PS': 'PSE', 'PW': 'PLW', 'PT': 'PRT', 'SJ': 'SJM', 'PY': 'PRY', 'IQ': 'IRQ', 'PA': 'PAN', 'PF': 'PYF', 'PG': 'PNG', 'PE': 'PER', 'PK': 'PAK', 'PH': 'PHL', 'PN': 'PCN', 'PL': 'POL', 'PM': 'SPM', 'ZM': 'ZMB', 'EH': 'ESH', 'EE': 'EST', 'EG': 'EGY', 'ZA': 'ZAF', 'EC': 'ECU', 'IT': 'ITA', 'VN': 'VNM', 'SB': 'SLB', 'ET': 'ETH', 'SO': 'SOM', 'ZW': 'ZWE', 'SA': 'SAU', 'ES': 'ESP', 'ER': 'ERI', 'ME': 'MNE', 'MD': 'MDA', 'MG': 'MDG', 'MF': 'MAF', 'MA': 'MAR', 'MC': 'MCO', 'UZ': 'UZB', 'MM': 'MMR', 'ML': 'MLI', 'MO': 'MAC', 'MN': 'MNG', 'MH': 'MHL', 'MK': 'MKD', 'MU': 'MUS', 'MT': 'MLT', 'MW': 'MWI', 'MV': 'MDV', 'MQ': 'MTQ', 'MP': 'MNP', 'MS': 'MSR', 'MR': 'MRT', 'IM': 'IMN', 'UG': 'UGA', 'TZ': 'TZA', 'MY': 'MYS', 'MX': 'MEX', 'IL': 'ISR', 'FR': 'FRA', 'IO': 'IOT', 'SH': 'SHN', 'FI': 'FIN', 'FJ': 'FJI', 'FK': 'FLK', 'FM': 'FSM', 'FO': 'FRO', 'NI': 'NIC', 'NL': 'NLD', 'NO': 'NOR', 'NA': 'NAM', 'VU': 'VUT', 'NC': 'NCL', 'NE': 'NER', 'NF': 'NFK', 'NG': 'NGA', 'NZ': 'NZL', 'NP': 'NPL', 'NR': 'NRU', 'NU': 'NIU', 'CK': 'COK', 'XK': 'XKX', 'CI': 'CIV', 'CH': 'CHE', 'CO': 'COL', 'CN': 'CHN', 'CM': 'CMR', 'CL': 'CHL', 'CC': 'CCK', 'CA': 'CAN', 'CG': 'COG', 'CF': 'CAF', 'CD': 'COD', 'CZ': 'CZE', 'CY': 'CYP', 'CX': 'CXR', 'CS': 'SCG', 'CR': 'CRI', 'CW': 'CUW', 'CV': 'CPV', 'CU': 'CUB', 'SZ': 'SWZ', 'SY': 'SYR', 'SX': 'SXM', 'KG': 'KGZ', 'KE': 'KEN', 'SR': 'SUR', 'KI': 'KIR', 'KH': 'KHM', 'KN': 'KNA', 'KM': 'COM', 'ST': 'STP', 'SK': 'SVK', 'KR': 'KOR', 'SI': 'SVN', 'KP': 'PRK', 'KW': 'KWT', 'SN': 'SEN', 'SM': 'SMR', 'SL': 'SLE', 'SC': 'SYC', 'KZ': 'KAZ', 'KY': 'CYM', 'SG': 'SGP', 'SE': 'SWE', 'SD': 'SDN', 'DO': 'DOM', 'DM': 'DMA', 'DJ': 'DJI', 'DK': 'DNK', 'VG': 'VGB', 'DE': 'DEU', 'YE': 'YEM', 'DZ': 'DZA', 'US': 'USA', 'UY': 'URY', 'YT': 'MYT', 'UM': 'UMI', 'LB': 'LBN', 'LC': 'LCA', 'LA': 'LAO', 'TV': 'TUV', 'TW': 'TWN', 'TT': 'TTO', 'TR': 'TUR', 'LK': 'LKA', 'LI': 'LIE', 'LV': 'LVA', 'TO': 'TON', 'LT': 'LTU', 'LU': 'LUX', 'LR': 'LBR', 'LS': 'LSO', 'TH': 'THA', 'TF': 'ATF', 'TG': 'TGO', 'TD': 'TCD', 'TC': 'TCA', 'LY': 'LBY', 'VA': 'VAT', 'VC': 'VCT', 'AE': 'ARE', 'AD': 'AND', 'AG': 'ATG', 'AF': 'AFG', 'AI': 'AIA', 'VI': 'VIR', 'IS': 'ISL', 'IR': 'IRN', 'AM': 'ARM', 'AL': 'ALB', 'AO': 'AGO', 'AN': 'ANT', 'AQ': 'ATA', 'AS': 'ASM', 'AR': 'ARG', 'AU': 'AUS', 'AT': 'AUT', 'AW': 'ABW', 'IN': 'IND', 'AX': 'ALA', 'AZ': 'AZE', 'IE': 'IRL', 'ID': 'IDN', 'UA': 'UKR', 'QA': 'QAT', 'MZ': 'MOZ'}

def normalizar_string(string, encode='utf-8'):
    """
    Limpa assentos e caracteres estranhos
    """
    from unicodedata import normalize
    try:
        return normalize('NFKD', string.decode('utf-8')).encode('ASCII', 'ignore')
    except UnicodeEncodeError:
        return normalize('NFKD', string).encode('ASCII', 'ignore')

def instanciar_banco():
    """
    Instancia a conexão com o banco
    """
    import MySQLdb
    
    con = MySQLdb.connect('192.168.0.174', 'eth1', 'redeinterna')
    con.select_db('futebol')

    cursor = con.cursor(cursorclass=MySQLdb.cursors.DictCursor)
    return cursor
    
def importar_paises():
    """
    """
    from time import sleep
    
    arquivo = open('paises.txt').read()
    # Pega um pais por linha de registro
    paises = arquivo.split('\n')
    dic_continentes = {}
    
    for pais in paises:
        if pais:
            # Pega um dado a cada tab em info de pais
            #Formato: ISO    ISO3    ISO-Numeric    fips    Country    Capital    
            #Area(in sq km)    Population    Continent    tld    
            #CurrencyCode    CurrencyName    Phone    Postal Code Format    
            #Postal Code Regex    Languages    geonameid    neighbours    EquivalentFipsCode
            dados = pais.split('\t')
            iso = dados[0]
            iso3 = dados[1]
            nome = dados[4]
            area = dados[6] 
            populacao = dados[7] 
            sigla_continente = dados[8]
            tld = dados[9]
            codigo_moeda = dados[10]
            nome_moeda = dados[11]
            telefone = dados[12]
            formado_codigo_postal = dados[13]
            regex_codigo_postal = dados[14]
            linguagens = dados[15]
            
            if not dic_continentes.has_key(sigla_continente):
                id_continente = Continente.objects.filter(sigla=sigla_continente)[0]
                dic_continentes[sigla_continente] = id_continente
            else:
                id_continente = dic_continentes[sigla_continente]
            
            
            
            # Criacao do Pais
            obj = Pais(id_continente=id_continente,nome_pt=nome,nome_en=nome,\
                          nome_es=nome,iso=iso,iso3=iso3)
            if area:
                obj.area = area
            if populacao:
                obj.populacao = populacao
            if tld:
                obj.tld = tld
            if codigo_moeda:
                obj.codigo_moeda = codigo_moeda
            if nome_moeda:
                obj.nome_moeda = nome_moeda
            if telefone:
                obj.telefone = telefone
            if formado_codigo_postal:
                obj.formado_codigo_postal = formado_codigo_postal
            if regex_codigo_postal:
                obj.regex_codigo_postal = regex_codigo_postal
            if linguagens:
                obj.linguagens = linguagens
                
            obj.save()

            
def importar_cidades():
    """
    """
    import os
    
    dirname = '/home/orkut/futebol/geonames/'
    lista_paises = [f for f in os.listdir(dirname) if os.path.isdir(os.path.join(dirname, f))]
    cont = 0
    for pais in lista_paises:
        arquivo = open(dirname + pais + '/' + pais + '.txt').read()
        #country code/postal code/place name/admin name1/
        #admin code1/admin name2/admin code2/admin name3/
        #admin code3/latitude/longitude/accuracy
        # Pega uma cidade por linha de registro
        cidades = arquivo.split('\n')
        dic_estados = {}
        
        
        lista_cidade = []
        if pais not in ('LT', 'MC', 'LI', 'RU', 'DK', 'SI',
                        'CZ', 'AS', 'GT', 'NL', 'AU', 'SM',
                        'GU', 'GP', 'TH', 'TR', 'MQ', 'IM',
                        'GF', 'DO', 'CA', 'NO', 'HR', 'HU',
                        'SE', 'US', 'GB', 'PK', 'NZ', 'FR',
                        'GL', 'MY', 'PL', 'MK', 'PM', 'YT',
                        'MD', 'AR', 'RE', 'AT', 'ZA', 'JP',
                        'BG', 'DE', 'BR', 'MX', 'ES', 'MH',
                        'JE', 'IT', 'PR', 'PH', 'BD', 'FO',
                        'GY', 'VA', 'VI', 'CH', 'SK', 'GG',
                        'IS', 'IN', 'MP', 'FI', 'BE', 'PT',
                        'LK', 'LU') and cont <= 5:
            cont += 1
            
            print '******************'
            print pais
            print '******************'
            
            for cidade in cidades:
                dados = cidade.split('\t')
                
                sigla_pais = dados[0]
                if sigla_pais:
                    
                    #nome = place name
                    nome = dados[2]
                    nome = nome.split('(')[0]
                    
                    nomes = nome.split(',')
                    for nome in nomes:
                        if nome not in lista_cidade:
                        
                            obj_pais = Pais.objects.get(iso=sigla_pais)
                            
                            #estado = admin name1
                            nome_estado = dados[3]
                            if not nome_estado:
                                #estado = admin name2
                                nome_estado = dados[5]
                                if not nome_estado:
                                    #estado = admin name3
                                    nome_estado = dados[7]
                            if not dic_estados.has_key(nome_estado):
                                estado = Estado.objects.filter(nome=nome_estado, id_pais=obj_pais)
                                if estado:
                                    obj_estado = estado[0]
                                else:
                                    obj_estado = Estado(id_pais=obj_pais, nome=nome_estado)
                                    obj_estado.save()
                                dic_estados[nome_estado] = obj_estado
                            else:
                                obj_estado = dic_estados[nome_estado]
                                
                            obj_cidade = Cidade(id_estado=obj_estado, nome=nome.title(), capital=1)
                            obj_cidade.save()
                            
                            lista_cidade.append(nome)
                        
            
            
            
        
if __name__ == "__main__":
    #importar_cidades()
    print '********************************END********************************'