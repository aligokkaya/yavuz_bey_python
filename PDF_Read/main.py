# import PyPDF2

# Nom=''
# Tel=''
# Client=''
# Prenom=''
# date=''
# marqua=''
# Lieu=''
# couleur=''


# json_data={}


# def data(array):
#     # print(array)
#     for i in array:
#         if i.find('Tél bureau:')>=0:
#             json_data['Tel']=i[3:]
#         if i.find('Nom')>=0:
#             json_data['Nom']=i[3:]
#         if i.find('Prénom')>=0:
#             json_data['Prenom']=i[6:]
#         if i.find('Client')>=0:
#             json_data['Client']=i[6:]
#         if i.find('de:')>=0:
#             json_data['de']=i[2:]
#         if i.find('date:')>=0:
#             json_data['date']=i[5:]
#         if i.find('marque/type')>=0:
#             json_data['marque']=i[6:]
#         if i.find('C.P./Lieu:')>=0:
#             json_data['Lieu']=i[4:]
#         if i.find('couleur')>=0:
#             json_data['couleur']=i[7:]
#     print(json_data)
#     return json_data

# file = open('1084280.pdf', 'rb')
# fileReader = PyPDF2.PdfFileReader(file)

# pageObj = fileReader.getPage(0)
# text=pageObj.extractText().split("\n")
# print(text)
# # dt=data(text)
# # print((dt))






# ['@@Betreff J- 1084280 , Auftrag an SVP Garage SA@@Nummer Swiss DLC AG', 'Industriestr. 12', 'CH-8305 Dietlikon', 'Tel  +41 44 908 64 60', 'Fax +41 44 908 64 66www.swissdlc.ch', 'info@swissdlc.ch', 'ordre/confirmation de dépannage', "GomesTaà l'entreprise:", 'date: 01.09.22 10:45:46', 'de: Swiss DLC AG; ', 'no de Journale:SVP Garage SA', 'Merci pour votre collaboration', 'Avec nos meilleurs salutationsClient:', 'Nom: Cangiano', 'Prénom: Marino', 'C.P./Lieu: 1205 GenèveTél  privé', 'Tél bureau: +41 (0)22   8001414', 'mobil:', 'Problème:', 'Le véhicule ne démarre plus', "si l'aide sur place n'est pas possible, le ", "transport jusqu'à l'agence de la marque est ", 'couvert.rue route de soulmoulin 4Blieu de la panne chêne-Bourg', 'GE 649356 ', 'type de véhicule Personenwagen', 'marque/type: RENAULT KANGOO EX', '1ère mise en ci. 12.15', 'couleur:No. de châssis:', 'VF1FW51H154242 chang. de vitesse Automat', 'véhicule roulable?Kilomètres: 68300', 'remarques véhiculevéhiculeÉvénement', 'remarques:Tél actuel 076 553 13 18', 'description du lieuordre en nom: Auto-Interleasing', 'Si pas encore fait, nous vous prions de nous rappeller ', 'aprés la réalisation du dépannage au numéro de tel:', '+41 44 908 64 60 !!!No de Fax. :', 'No de membre: Police: 5519420066Kreutzer & Cie SA', 'réponse dépanneur', 'No. plaquecorrect Correction', '1. ère mise en c.', 'Kilomètres', 'problème', 'réparation', 'réparation définitive réparation provisoire', "remorqué jusque'à", 'avec chariot transport avec câbleArrivée', 'Terminé', 'Km faits', 'Prix selon tarif', 'suppléments', 'Prix total4 x 41084280 AI', 'Garantie ou mois']


from pdfminer3.layout import LAParams, LTTextBox
from pdfminer3.pdfpage import PDFPage
from pdfminer3.pdfinterp import PDFResourceManager
from pdfminer3.pdfinterp import PDFPageInterpreter
from pdfminer3.converter import PDFPageAggregator
from pdfminer3.converter import TextConverter
import io

resource_manager = PDFResourceManager()
fake_file_handle = io.StringIO()
converter = TextConverter(resource_manager, fake_file_handle, laparams=LAParams())
page_interpreter = PDFPageInterpreter(resource_manager, converter)

with open('1084280.pdf', 'rb') as fh:

    for page in PDFPage.get_pages(fh,
                                  caching=True,
                                  check_extractable=True):
        page_interpreter.process_page(page)

    text = fake_file_handle.getvalue()

# close open handles
converter.close()
fake_file_handle.close()

print(text)
# print(convert_pdf_to_txt('1084280.pdf'))

# import tabula

# # Read pdf into a list of DataFrame
# dfs = tabula.read_pdf("1084280.pdf", pages='all')

# # Read remote pdf into a list of DataFrame
# # dfs2 = tabula.read_pdf("1084280.pdf")

# # convert PDF into CSV
# tabula.convert_into("1084280.pdf", "output.csv", output_format="csv", pages='all')

# # convert all PDFs in a directory
# # tabula.convert_into_by_batch("input_directory", output_format='csv', pages='all')