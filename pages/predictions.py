# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
from joblib import load

# Imports from this application
from app import app

# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout

origin_dict = {2: 'TPA', 3: 'BUR', 4: 'LGA', 5: 'DEN', 6: 'MDW', 7: 'SJC', 8: 'CLT', 9: 'JFK', 10: 'IAH', 11: 'CVG', 12: 'PHL', 13: 'FLL', 14: 'ATL', 15: 'SJU', 16: 'SFB', 17: 'MSP', 18: 'PIA', 19: 'OKC', 20: 'ORD', 21: 'PHX', 22: 'BWI', 23: 'AUS', 24: 'OAK', 25: 'RSW', 26: 'MCO', 27: 'MSY', 28: 'SLC', 29: 'LAX', 30: 'MKE', 31: 'LAS', 32: 'PIT', 33: 'SAN', 34: 'DTW', 35: 'EWR', 36: 'ABQ', 37: 'MCI', 38: 'BNA', 39: 'SFO', 40: 'BDL', 41: 'SMF', 42: 'IAD', 43: 'HNL', 44: 'BOS', 45: 'MIA', 46: 'PIE', 47: 'HOU', 48: 'PVU', 49: 'RIC', 50: 'ANC', 51: 'PBI', 52: 'SEA', 53: 'DCA', 54: 'OGG', 55: 'SAV', 56: 'SAT', 57: 'SNA', 58: 'IND', 59: 'ATW', 60: 'JAC', 61: 'BQN', 62: 'ONT', 63: 'CLE', 64: 'JAX', 65: 'FAI', 66: 'ICT', 67: 'DAL', 68: 'ROC', 69: 'LGB', 70: 'DAB', 71: 'PDX', 72: 'AZA', 73: 'MEM', 74: 'SGF', 75: 'RDU', 76: 'ECP', 77: 'PWM', 78: 'GSO', 79: 'SMX', 80: 'HPN', 81: 'MHT', 82: 'EUG', 83: 'CMH', 84: 'CAE', 85: 'BIL', 86: 'MYR', 87: 'ELP', 88: 'SBN', 89: 'PSP', 90: 'DSM', 91: 'OMA', 92: 'STL', 93: 'KOA', 94: 'GRI', 95: 'VPS', 96: 'GRR', 97: 'FSD', 98: 'PGD', 99: 'BUF', 100: 'GEG', 101: 'AVL', 102: 'SCK', 103: 'TTN', 104: 'LIH', 105: 'ORF', 106: 'TUS', 107: 'RNO', 108: 'CHS', 109: 'CAK', 110: 'BMI', 111: 'BLV', 112: 'JNU', 113: 'CID', 114: 'MSN', 115: 'PBG', 116: 'MFE', 117: 'SWF', 118: 'BOI', 119: 'TRI', 120: 'ISP', 121: 'TOL', 122: 'EVV', 123: 'FWA', 124: 'SDF', 125: 'TUL', 126: 'LBB', 127: 'HDN', 128: 'USA', 129: 'MOB', 130: 'ELM', 131: 'STT', 132: 'BGR', 133: 'PVD', 134: 'RFD', 135: 'EGE', 136: 'ADQ', 137: 'SRQ', 138: 'PSE', 139: 'LIT', 140: 'COS', 141: 'LFT', 142: 'PNS', 143: 'FAT', 144: 'MLI', 145: 'BZN', 146: 'ALB', 147: 'ABE', 148: 'BHM', 149: 'STX', 150: 'MLB', 151: 'HRL', 152: 'GSP', 153: 'MSO', 154: 'KTN', 155: 'IDA', 156: 'SYR', 157: 'ORH', 158: 'SPI', 159: 'SIT', 160: 'OGD', 161: 'BET', 162: 'IAG', 163: 'SBA', 164: 'CRW', 165: 'PSC', 166: 'BIS', 167: 'OME', 168: 'GTF', 169: 'ITO', 170: 'MAF', 171: 'TYS', 172: 'BTR', 173: 'ACY', 174: 'BTV', 175: 'DAY', 176: 'BRW', 177: 'LCK', 178: 'AGS', 179: 'FNT', 180: 'MTJ', 181: 'SPN', 182: 'STC', 183: 'ACK', 184: 'MDT', 185: 'MOT', 186: 'CHA', 187: 'AMA', 188: 'CKB', 189: 'CRP', 190: 'TVC', 191: 'PHF', 192: 'BLI', 193: 'LEX', 194: 'JAN', 195: 'FAR', 196: 'FAY', 197: 'HTS', 198: 'GPT', 199: 'SCC', 200: 'EYW', 201: 'MVY', 202: 'PSM', 203: 'FCA', 204: 'GJT', 205: 'GFK', 206: 'RAP', 207: 'MRY', 208: 'MFR', 209: 'LBE', 210: 'XNA', 211: 'AVP', 212: 'LRD', 213: 'SHV', 214: 'GRB', 215: 'TLH', 216: 'ROA', 217: 'GUM', 218: 'GNV', 219: 'BKG', 220: 'HGR', 221: 'ILM', 222: 'CHO', 223: 'OTZ', 224: 'DLH', 225: 'GUC', 226: 'OWB', 227: 'HSV', 228: 'OGS', 229: 'ADK', 230: 'PPG', 231: 'CDV', 232: 'YAK', 233: 'PSG', 234: 'ABI', 235: 'WRG', 236: 'HYA', 237: 'AKN', 238: 'STS', 239: 'SPS', 240: 'DLG', 241: 'GST', 242: 'SGU', 243: 'YNG', 244: 'SLN', 245: 'SHD', 246: 'FLG', 247: 'JHM', 248: 'RKS', 249: 'BFL', -2: 'nan', 249: 'BFL'}
dest_dict = {2: 'ISP', 3: 'SEA', 4: 'CLT', 5: 'JAX', 6: 'TPA', 7: 'MCO', 8: 'MDW', 9: 'DTW', 10: 'MSY', 11: 'LAX', 12: 'DEN', 13: 'MCI', 14: 'BQN', 15: 'LGA', 16: 'BWI', 17: 'PSM', 18: 'AZA', 19: 'PHX', 20: 'DFW', 21: 'EWR', 22: 'ONT', 23: 'MKE', 24: 'SAT', 25: 'BOS', 26: 'ELM', 27: 'JFK', 28: 'LIH', 29: 'PBI', 30: 'MSP', 31: 'LAS', 32: 'DAL', 33: 'RIC', 34: 'ANC', 35: 'OAK', 36: 'CVG', 37: 'SAN', 38: 'CHS', 39: 'ELP', 40: 'MIA', 41: 'LGB', 42: 'HNL', 43: 'FLL', 44: 'IAD', 45: 'PVD', 46: 'OGG', 47: 'CHA', 48: 'SLC', 49: 'BUR', 50: 'PWM', 51: 'ATL', 52: 'PDX', 53: 'FAT', 54: 'SFO', 55: 'SMF', 56: 'AUS', 57: 'RSW', 58: 'STL', 59: 'CLE', 60: 'MEM', 61: 'PHL', 62: 'SJC', 63: 'HOU', 64: 'PNS', 65: 'SAV', 66: 'DCA', 67: 'IAH', 68: 'SNA', 69: 'SJU', 70: 'TUL', 71: 'BNA', 72: 'CMH', 73: 'SDF', 74: 'PSP', 75: 'MAF', 76: 'RNO', 77: 'TUS', 78: 'GFK', 79: 'ALB', 80: 'KOA', 81: 'ABQ', 82: 'BGR', 83: 'GTF', 84: 'RDU', 85: 'FSD', 86: 'BOI', 87: 'GRR', 88: 'OMA', 89: 'PIT', 90: 'SIT', 91: 'HPN', 92: 'IND', 93: 'BUF', 94: 'PGD', 95: 'PIE', 96: 'GEG', 97: 'BRW', 98: 'BDL', 99: 'SGF', 100: 'SFB', 101: 'PBG', 102: 'DSM', 103: 'STX', 104: 'ITO', 105: 'MLI', 106: 'ATW', 107: 'JAC', 108: 'MYR', 109: 'COS', 110: 'LCK', 111: 'CAK', 112: 'JAN', 113: 'BIL', 114: 'BHM', 115: 'ORF', 116: 'SRQ', 117: 'FWA', 118: 'OME', 119: 'PVU', 120: 'VPS', 121: 'MHT', 122: 'PIA', 123: 'MLB', 124: 'MTJ', 125: 'HRL', 126: 'MDT', 127: 'SYR', 128: 'OKC', 129: 'ROC', 130: 'STT', 131: 'SCK', 132: 'EUG', 133: 'CID', 134: 'BLI', 135: 'EYW', 136: 'SWF', 137: 'ORH', 138: 'AMA', 139: 'GSO', 140: 'AVL', 141: 'RFD', 142: 'LIT', 143: 'SBN', 144: 'ILM', 145: 'EGE', 146: 'FNT', 147: 'HDN', 148: 'CDV', 149: 'SPI', 150: 'SBA', 151: 'BIS', 152: 'AVP', 153: 'RAP', 154: 'ECP', 155: 'ABE', 156: 'LBB', 157: 'ACK', 158: 'TTN', 159: 'JNU', 160: 'HYA', 161: 'ICT', 162: 'GPT', 163: 'ACY', 164: 'ROA', 165: 'PSE', 166: 'BZN', 167: 'CRP', 168: 'DAY', 169: 'TYS', 170: 'CAE', 171: 'SHV', 172: 'IAG', 173: 'MSN', 174: 'BTR', 175: 'DAB', 176: 'MFE', 177: 'ADQ', 178: 'FAI', 179: 'TLH', 180: 'USA', 181: 'GJT', 182: 'GUC', 183: 'BLV', 184: 'MSO', 185: 'GUM', 186: 'BTV', 187: 'FAR', 188: 'KTN', 189: 'TOL', 190: 'BET', 191: 'EVV', 192: 'HTS', 193: 'GSP', 194: 'CKB', 195: 'STC', 196: 'IDA', 197: 'LBE', 198: 'LEX', 199: 'GRI', 200: 'GST', 201: 'OGS', 202: 'PSC', 203: 'MFR', 204: 'BMI', 205: 'OGD', 206: 'AGS', 207: 'FCA', 208: 'XNA', 209: 'LFT', 210: 'SPN', 211: 'MOT', 212: 'HGR', 213: 'TVC', 214: 'AKN', 215: 'PSG', 216: 'SMX', 217: 'MOB', 218: 'STS', 219: 'LRD', 220: 'MVY', 221: 'OTZ', 222: 'HSV', 223: 'MRY', 224: 'PHF', 225: 'BKG', 226: 'WRG', 227: 'SCC', 228: 'CHO', 229: 'OWB', 230: 'TRI', 231: 'YAK', 232: 'PPG', 233: 'DLH', 234: 'GNV', 235: 'FAY', 236: 'CRW', 237: 'YNG', 238: 'GRB', 239: 'DLG', 240: 'ADK', 241: 'LNK', 242: 'ASE', 243: 'DRO', 244: 'MKG', 245: 'SGU', 246: 'BFL', 247: 'OTH', 248: 'CPR', 249: 'ITH', 250: 'SBP', 251: 'SCE', 252: 'RST', -2: 'nan', 252: 'RST'}

pipeline = load('assets/pipeline.joblib')

column1 = dbc.Col(
    [
        dcc.Markdown(
            """

            # **PREDICTIONS**

            To predict the price of your airline ticket(s), simply make selections from the options below:

            """
        ),
        html.Br(),
        dcc.Markdown('##### **AIRLINE COMPANY**'),
        dcc.Dropdown(
            id='AirlineCompany',
            options = [
                {'label': 'Southwest Airline Co. (WN)', 'value': 2},
                {'label': 'Delta Air Lines Inc. (DL)', 'value': 4},
                {'label': 'American Airlines Inc. (AA)', 'value': 1},
                {'label': 'United Air Lines Inc. (UA)', 'value': 5},
                {'label': 'Jetblue Airways (B6)', 'value': 7},
                {'label': 'Alaskan Airlines Inc. (AS)', 'value': 3},
                {'label': 'Spirit Airlines (NK)', 'value': 9},
                {'label': 'Allegiant Air (G4)', 'value': 8},
                {'label': 'Frontier Airlines Inc. (F9)', 'value': 6},
                {'label': 'Hawaiian Airlines Inc. (HA)', 'value': 10},
                {'label': 'Sun Country Airlines (SY)', 'value': 12},
                {'label': 'Virgin America (VX)', 'value': 11},
            ],
            value = 4,
            className='mb-3',
            placeholder='Select your Airline Company...'
        ),
        dcc.Markdown('##### **ORIGIN CITY/AIRPORT**'),
        dcc.Dropdown(
            id='Origin',
            options = [
                {'label': 'TPA', 'value': 2}, {'label': 'BUR', 'value': 3}, {'label': 'LGA', 'value': 4}, {'label': 'DEN', 'value': 5}, {'label': 'MDW', 'value': 6}, {'label': 'SJC', 'value': 7}, {'label': 'CLT', 'value': 8}, {'label': 'JFK', 'value': 9}, {'label': 'IAH', 'value': 10}, {'label': 'CVG', 'value': 11}, {'label': 'PHL', 'value': 12}, {'label': 'FLL', 'value': 13}, {'label': 'ATL', 'value': 14}, {'label': 'SJU', 'value': 15}, {'label': 'SFB', 'value': 16}, {'label': 'MSP', 'value': 17}, {'label': 'PIA', 'value': 18}, {'label': 'OKC', 'value': 19}, {'label': 'ORD', 'value': 20}, {'label': 'PHX', 'value': 21}, {'label': 'BWI', 'value': 22}, {'label': 'AUS', 'value': 23}, {'label': 'OAK', 'value': 24}, {'label': 'RSW', 'value': 25}, {'label': 'MCO', 'value': 26}, {'label': 'MSY', 'value': 27}, {'label': 'SLC', 'value': 28}, {'label': 'LAX', 'value': 29}, {'label': 'MKE', 'value': 30}, {'label': 'LAS', 'value': 31}, {'label': 'PIT', 'value': 32}, {'label': 'SAN', 'value': 33}, {'label': 'DTW', 'value': 34}, {'label': 'EWR', 'value': 35}, {'label': 'ABQ', 'value': 36}, {'label': 'MCI', 'value': 37}, {'label': 'BNA', 'value': 38}, {'label': 'SFO', 'value': 39}, {'label': 'BDL', 'value': 40}, {'label': 'SMF', 'value': 41}, {'label': 'IAD', 'value': 42}, {'label': 'HNL', 'value': 43}, {'label': 'BOS', 'value': 44}, {'label': 'MIA', 'value': 45}, {'label': 'PIE', 'value': 46}, {'label': 'HOU', 'value': 47}, {'label': 'PVU', 'value': 48}, {'label': 'RIC', 'value': 49}, {'label': 'ANC', 'value': 50}, {'label': 'PBI', 'value': 51}, {'label': 'SEA', 'value': 52}, {'label': 'DCA', 'value': 53}, {'label': 'OGG', 'value': 54}, {'label': 'SAV', 'value': 55}, {'label': 'SAT', 'value': 56}, {'label': 'SNA', 'value': 57}, {'label': 'IND', 'value': 58}, {'label': 'ATW', 'value': 59}, {'label': 'JAC', 'value': 60}, {'label': 'BQN', 'value': 61}, {'label': 'ONT', 'value': 62}, {'label': 'CLE', 'value': 63}, {'label': 'JAX', 'value': 64}, {'label': 'FAI', 'value': 65}, {'label': 'ICT', 'value': 66}, {'label': 'DAL', 'value': 67}, {'label': 'ROC', 'value': 68}, {'label': 'LGB', 'value': 69}, {'label': 'DAB', 'value': 70}, {'label': 'PDX', 'value': 71}, {'label': 'AZA', 'value': 72}, {'label': 'MEM', 'value': 73}, {'label': 'SGF', 'value': 74}, {'label': 'RDU', 'value': 75}, {'label': 'ECP', 'value': 76}, {'label': 'PWM', 'value': 77}, {'label': 'GSO', 'value': 78}, {'label': 'SMX', 'value': 79}, {'label': 'HPN', 'value': 80}, {'label': 'MHT', 'value': 81}, {'label': 'EUG', 'value': 82}, {'label': 'CMH', 'value': 83}, {'label': 'CAE', 'value': 84}, {'label': 'BIL', 'value': 85}, {'label': 'MYR', 'value': 86}, {'label': 'ELP', 'value': 87}, {'label': 'SBN', 'value': 88}, {'label': 'PSP', 'value': 89}, {'label': 'DSM', 'value': 90}, {'label': 'OMA', 'value': 91}, {'label': 'STL', 'value': 92}, {'label': 'KOA', 'value': 93}, {'label': 'GRI', 'value': 94}, {'label': 'VPS', 'value': 95}, {'label': 'GRR', 'value': 96}, {'label': 'FSD', 'value': 97}, {'label': 'PGD', 'value': 98}, {'label': 'BUF', 'value': 99}, {'label': 'GEG', 'value': 100}, {'label': 'AVL', 'value': 101}, {'label': 'SCK', 'value': 102}, {'label': 'TTN', 'value': 103}, {'label': 'LIH', 'value': 104}, {'label': 'ORF', 'value': 105}, {'label': 'TUS', 'value': 106}, {'label': 'RNO', 'value': 107}, {'label': 'CHS', 'value': 108}, {'label': 'CAK', 'value': 109}, {'label': 'BMI', 'value': 110}, {'label': 'BLV', 'value': 111}, {'label': 'JNU', 'value': 112}, {'label': 'CID', 'value': 113}, {'label': 'MSN', 'value': 114}, {'label': 'PBG', 'value': 115}, {'label': 'MFE', 'value': 116}, {'label': 'SWF', 'value': 117}, {'label': 'BOI', 'value': 118}, {'label': 'TRI', 'value': 119}, {'label': 'ISP', 'value': 120}, {'label': 'TOL', 'value': 121}, {'label': 'EVV', 'value': 122}, {'label': 'FWA', 'value': 123}, {'label': 'SDF', 'value': 124}, {'label': 'TUL', 'value': 125}, {'label': 'LBB', 'value': 126}, {'label': 'HDN', 'value': 127}, {'label': 'USA', 'value': 128}, {'label': 'MOB', 'value': 129}, {'label': 'ELM', 'value': 130}, {'label': 'STT', 'value': 131}, {'label': 'BGR', 'value': 132}, {'label': 'PVD', 'value': 133}, {'label': 'RFD', 'value': 134}, {'label': 'EGE', 'value': 135}, {'label': 'ADQ', 'value': 136}, {'label': 'SRQ', 'value': 137}, {'label': 'PSE', 'value': 138}, {'label': 'LIT', 'value': 139}, {'label': 'COS', 'value': 140}, {'label': 'LFT', 'value': 141}, {'label': 'PNS', 'value': 142}, {'label': 'FAT', 'value': 143}, {'label': 'MLI', 'value': 144}, {'label': 'BZN', 'value': 145}, {'label': 'ALB', 'value': 146}, {'label': 'ABE', 'value': 147}, {'label': 'BHM', 'value': 148}, {'label': 'STX', 'value': 149}, {'label': 'MLB', 'value': 150}, {'label': 'HRL', 'value': 151}, {'label': 'GSP', 'value': 152}, {'label': 'MSO', 'value': 153}, {'label': 'KTN', 'value': 154}, {'label': 'IDA', 'value': 155}, {'label': 'SYR', 'value': 156}, {'label': 'ORH', 'value': 157}, {'label': 'SPI', 'value': 158}, {'label': 'SIT', 'value': 159}, {'label': 'OGD', 'value': 160}, {'label': 'BET', 'value': 161}, {'label': 'IAG', 'value': 162}, {'label': 'SBA', 'value': 163}, {'label': 'CRW', 'value': 164}, {'label': 'PSC', 'value': 165}, {'label': 'BIS', 'value': 166}, {'label': 'OME', 'value': 167}, {'label': 'GTF', 'value': 168}, {'label': 'ITO', 'value': 169}, {'label': 'MAF', 'value': 170}, {'label': 'TYS', 'value': 171}, {'label': 'BTR', 'value': 172}, {'label': 'ACY', 'value': 173}, {'label': 'BTV', 'value': 174}, {'label': 'DAY', 'value': 175}, {'label': 'BRW', 'value': 176}, {'label': 'LCK', 'value': 177}, {'label': 'AGS', 'value': 178}, {'label': 'FNT', 'value': 179}, {'label': 'MTJ', 'value': 180}, {'label': 'SPN', 'value': 181}, {'label': 'STC', 'value': 182}, {'label': 'ACK', 'value': 183}, {'label': 'MDT', 'value': 184}, {'label': 'MOT', 'value': 185}, {'label': 'CHA', 'value': 186}, {'label': 'AMA', 'value': 187}, {'label': 'CKB', 'value': 188}, {'label': 'CRP', 'value': 189}, {'label': 'TVC', 'value': 190}, {'label': 'PHF', 'value': 191}, {'label': 'BLI', 'value': 192}, {'label': 'LEX', 'value': 193}, {'label': 'JAN', 'value': 194}, {'label': 'FAR', 'value': 195}, {'label': 'FAY', 'value': 196}, {'label': 'HTS', 'value': 197}, {'label': 'GPT', 'value': 198}, {'label': 'SCC', 'value': 199}, {'label': 'EYW', 'value': 200}, {'label': 'MVY', 'value': 201}, {'label': 'PSM', 'value': 202}, {'label': 'FCA', 'value': 203}, {'label': 'GJT', 'value': 204}, {'label': 'GFK', 'value': 205}, {'label': 'RAP', 'value': 206}, {'label': 'MRY', 'value': 207}, {'label': 'MFR', 'value': 208}, {'label': 'LBE', 'value': 209}, {'label': 'XNA', 'value': 210}, {'label': 'AVP', 'value': 211}, {'label': 'LRD', 'value': 212}, {'label': 'SHV', 'value': 213}, {'label': 'GRB', 'value': 214}, {'label': 'TLH', 'value': 215}, {'label': 'ROA', 'value': 216}, {'label': 'GUM', 'value': 217}, {'label': 'GNV', 'value': 218}, {'label': 'BKG', 'value': 219}, {'label': 'HGR', 'value': 220}, {'label': 'ILM', 'value': 221}, {'label': 'CHO', 'value': 222}, {'label': 'OTZ', 'value': 223}, {'label': 'DLH', 'value': 224}, {'label': 'GUC', 'value': 225}, {'label': 'OWB', 'value': 226}, {'label': 'HSV', 'value': 227}, {'label': 'OGS', 'value': 228}, {'label': 'ADK', 'value': 229}, {'label': 'PPG', 'value': 230}, {'label': 'CDV', 'value': 231}, {'label': 'YAK', 'value': 232}, {'label': 'PSG', 'value': 233}, {'label': 'ABI', 'value': 234}, {'label': 'WRG', 'value': 235}, {'label': 'HYA', 'value': 236}, {'label': 'AKN', 'value': 237}, {'label': 'STS', 'value': 238}, {'label': 'SPS', 'value': 239}, {'label': 'DLG', 'value': 240}, {'label': 'GST', 'value': 241}, {'label': 'SGU', 'value': 242}, {'label': 'YNG', 'value': 243}, {'label': 'SLN', 'value': 244}, {'label': 'SHD', 'value': 245}, {'label': 'FLG', 'value': 246}, {'label': 'JHM', 'value': 247}, {'label': 'RKS', 'value': 248}, {'label': 'BFL', 'value': 249}, {'label': 'nan', 'value': -2}, {'label': 'BFL', 'value': 249}
            ],
            value = 2,
            className='mb-3',
            placeholder='Select your Origin Location...'
        ),
        dcc.Markdown('##### **DESTINATION CITY/AIRPORT**'),
        dcc.Dropdown(
            id='Dest',
            options = [
                {'label': 'ISP', 'value': 2}, {'label': 'SEA', 'value': 3}, {'label': 'CLT', 'value': 4}, {'label': 'JAX', 'value': 5}, {'label': 'TPA', 'value': 6}, {'label': 'MCO', 'value': 7}, {'label': 'MDW', 'value': 8}, {'label': 'DTW', 'value': 9}, {'label': 'MSY', 'value': 10}, {'label': 'LAX', 'value': 11}, {'label': 'DEN', 'value': 12}, {'label': 'MCI', 'value': 13}, {'label': 'BQN', 'value': 14}, {'label': 'LGA', 'value': 15}, {'label': 'BWI', 'value': 16}, {'label': 'PSM', 'value': 17}, {'label': 'AZA', 'value': 18}, {'label': 'PHX', 'value': 19}, {'label': 'DFW', 'value': 20}, {'label': 'EWR', 'value': 21}, {'label': 'ONT', 'value': 22}, {'label': 'MKE', 'value': 23}, {'label': 'SAT', 'value': 24}, {'label': 'BOS', 'value': 25}, {'label': 'ELM', 'value': 26}, {'label': 'JFK', 'value': 27}, {'label': 'LIH', 'value': 28}, {'label': 'PBI', 'value': 29}, {'label': 'MSP', 'value': 30}, {'label': 'LAS', 'value': 31}, {'label': 'DAL', 'value': 32}, {'label': 'RIC', 'value': 33}, {'label': 'ANC', 'value': 34}, {'label': 'OAK', 'value': 35}, {'label': 'CVG', 'value': 36}, {'label': 'SAN', 'value': 37}, {'label': 'CHS', 'value': 38}, {'label': 'ELP', 'value': 39}, {'label': 'MIA', 'value': 40}, {'label': 'LGB', 'value': 41}, {'label': 'HNL', 'value': 42}, {'label': 'FLL', 'value': 43}, {'label': 'IAD', 'value': 44}, {'label': 'PVD', 'value': 45}, {'label': 'OGG', 'value': 46}, {'label': 'CHA', 'value': 47}, {'label': 'SLC', 'value': 48}, {'label': 'BUR', 'value': 49}, {'label': 'PWM', 'value': 50}, {'label': 'ATL', 'value': 51}, {'label': 'PDX', 'value': 52}, {'label': 'FAT', 'value': 53}, {'label': 'SFO', 'value': 54}, {'label': 'SMF', 'value': 55}, {'label': 'AUS', 'value': 56}, {'label': 'RSW', 'value': 57}, {'label': 'STL', 'value': 58}, {'label': 'CLE', 'value': 59}, {'label': 'MEM', 'value': 60}, {'label': 'PHL', 'value': 61}, {'label': 'SJC', 'value': 62}, {'label': 'HOU', 'value': 63}, {'label': 'PNS', 'value': 64}, {'label': 'SAV', 'value': 65}, {'label': 'DCA', 'value': 66}, {'label': 'IAH', 'value': 67}, {'label': 'SNA', 'value': 68}, {'label': 'SJU', 'value': 69}, {'label': 'TUL', 'value': 70}, {'label': 'BNA', 'value': 71}, {'label': 'CMH', 'value': 72}, {'label': 'SDF', 'value': 73}, {'label': 'PSP', 'value': 74}, {'label': 'MAF', 'value': 75}, {'label': 'RNO', 'value': 76}, {'label': 'TUS', 'value': 77}, {'label': 'GFK', 'value': 78}, {'label': 'ALB', 'value': 79}, {'label': 'KOA', 'value': 80}, {'label': 'ABQ', 'value': 81}, {'label': 'BGR', 'value': 82}, {'label': 'GTF', 'value': 83}, {'label': 'RDU', 'value': 84}, {'label': 'FSD', 'value': 85}, {'label': 'BOI', 'value': 86}, {'label': 'GRR', 'value': 87}, {'label': 'OMA', 'value': 88}, {'label': 'PIT', 'value': 89}, {'label': 'SIT', 'value': 90}, {'label': 'HPN', 'value': 91}, {'label': 'IND', 'value': 92}, {'label': 'BUF', 'value': 93}, {'label': 'PGD', 'value': 94}, {'label': 'PIE', 'value': 95}, {'label': 'GEG', 'value': 96}, {'label': 'BRW', 'value': 97}, {'label': 'BDL', 'value': 98}, {'label': 'SGF', 'value': 99}, {'label': 'SFB', 'value': 100}, {'label': 'PBG', 'value': 101}, {'label': 'DSM', 'value': 102}, {'label': 'STX', 'value': 103}, {'label': 'ITO', 'value': 104}, {'label': 'MLI', 'value': 105}, {'label': 'ATW', 'value': 106}, {'label': 'JAC', 'value': 107}, {'label': 'MYR', 'value': 108}, {'label': 'COS', 'value': 109}, {'label': 'LCK', 'value': 110}, {'label': 'CAK', 'value': 111}, {'label': 'JAN', 'value': 112}, {'label': 'BIL', 'value': 113}, {'label': 'BHM', 'value': 114}, {'label': 'ORF', 'value': 115}, {'label': 'SRQ', 'value': 116}, {'label': 'FWA', 'value': 117}, {'label': 'OME', 'value': 118}, {'label': 'PVU', 'value': 119}, {'label': 'VPS', 'value': 120}, {'label': 'MHT', 'value': 121}, {'label': 'PIA', 'value': 122}, {'label': 'MLB', 'value': 123}, {'label': 'MTJ', 'value': 124}, {'label': 'HRL', 'value': 125}, {'label': 'MDT', 'value': 126}, {'label': 'SYR', 'value': 127}, {'label': 'OKC', 'value': 128}, {'label': 'ROC', 'value': 129}, {'label': 'STT', 'value': 130}, {'label': 'SCK', 'value': 131}, {'label': 'EUG', 'value': 132}, {'label': 'CID', 'value': 133}, {'label': 'BLI', 'value': 134}, {'label': 'EYW', 'value': 135}, {'label': 'SWF', 'value': 136}, {'label': 'ORH', 'value': 137}, {'label': 'AMA', 'value': 138}, {'label': 'GSO', 'value': 139}, {'label': 'AVL', 'value': 140}, {'label': 'RFD', 'value': 141}, {'label': 'LIT', 'value': 142}, {'label': 'SBN', 'value': 143}, {'label': 'ILM', 'value': 144}, {'label': 'EGE', 'value': 145}, {'label': 'FNT', 'value': 146}, {'label': 'HDN', 'value': 147}, {'label': 'CDV', 'value': 148}, {'label': 'SPI', 'value': 149}, {'label': 'SBA', 'value': 150}, {'label': 'BIS', 'value': 151}, {'label': 'AVP', 'value': 152}, {'label': 'RAP', 'value': 153}, {'label': 'ECP', 'value': 154}, {'label': 'ABE', 'value': 155}, {'label': 'LBB', 'value': 156}, {'label': 'ACK', 'value': 157}, {'label': 'TTN', 'value': 158}, {'label': 'JNU', 'value': 159}, {'label': 'HYA', 'value': 160}, {'label': 'ICT', 'value': 161}, {'label': 'GPT', 'value': 162}, {'label': 'ACY', 'value': 163}, {'label': 'ROA', 'value': 164}, {'label': 'PSE', 'value': 165}, {'label': 'BZN', 'value': 166}, {'label': 'CRP', 'value': 167}, {'label': 'DAY', 'value': 168}, {'label': 'TYS', 'value': 169}, {'label': 'CAE', 'value': 170}, {'label': 'SHV', 'value': 171}, {'label': 'IAG', 'value': 172}, {'label': 'MSN', 'value': 173}, {'label': 'BTR', 'value': 174}, {'label': 'DAB', 'value': 175}, {'label': 'MFE', 'value': 176}, {'label': 'ADQ', 'value': 177}, {'label': 'FAI', 'value': 178}, {'label': 'TLH', 'value': 179}, {'label': 'USA', 'value': 180}, {'label': 'GJT', 'value': 181}, {'label': 'GUC', 'value': 182}, {'label': 'BLV', 'value': 183}, {'label': 'MSO', 'value': 184}, {'label': 'GUM', 'value': 185}, {'label': 'BTV', 'value': 186}, {'label': 'FAR', 'value': 187}, {'label': 'KTN', 'value': 188}, {'label': 'TOL', 'value': 189}, {'label': 'BET', 'value': 190}, {'label': 'EVV', 'value': 191}, {'label': 'HTS', 'value': 192}, {'label': 'GSP', 'value': 193}, {'label': 'CKB', 'value': 194}, {'label': 'STC', 'value': 195}, {'label': 'IDA', 'value': 196}, {'label': 'LBE', 'value': 197}, {'label': 'LEX', 'value': 198}, {'label': 'GRI', 'value': 199}, {'label': 'GST', 'value': 200}, {'label': 'OGS', 'value': 201}, {'label': 'PSC', 'value': 202}, {'label': 'MFR', 'value': 203}, {'label': 'BMI', 'value': 204}, {'label': 'OGD', 'value': 205}, {'label': 'AGS', 'value': 206}, {'label': 'FCA', 'value': 207}, {'label': 'XNA', 'value': 208}, {'label': 'LFT', 'value': 209}, {'label': 'SPN', 'value': 210}, {'label': 'MOT', 'value': 211}, {'label': 'HGR', 'value': 212}, {'label': 'TVC', 'value': 213}, {'label': 'AKN', 'value': 214}, {'label': 'PSG', 'value': 215}, {'label': 'SMX', 'value': 216}, {'label': 'MOB', 'value': 217}, {'label': 'STS', 'value': 218}, {'label': 'LRD', 'value': 219}, {'label': 'MVY', 'value': 220}, {'label': 'OTZ', 'value': 221}, {'label': 'HSV', 'value': 222}, {'label': 'MRY', 'value': 223}, {'label': 'PHF', 'value': 224}, {'label': 'BKG', 'value': 225}, {'label': 'WRG', 'value': 226}, {'label': 'SCC', 'value': 227}, {'label': 'CHO', 'value': 228}, {'label': 'OWB', 'value': 229}, {'label': 'TRI', 'value': 230}, {'label': 'YAK', 'value': 231}, {'label': 'PPG', 'value': 232}, {'label': 'DLH', 'value': 233}, {'label': 'GNV', 'value': 234}, {'label': 'FAY', 'value': 235}, {'label': 'CRW', 'value': 236}, {'label': 'YNG', 'value': 237}, {'label': 'GRB', 'value': 238}, {'label': 'DLG', 'value': 239}, {'label': 'ADK', 'value': 240}, {'label': 'LNK', 'value': 241}, {'label': 'ASE', 'value': 242}, {'label': 'DRO', 'value': 243}, {'label': 'MKG', 'value': 244}, {'label': 'SGU', 'value': 245}, {'label': 'BFL', 'value': 246}, {'label': 'OTH', 'value': 247}, {'label': 'CPR', 'value': 248}, {'label': 'ITH', 'value': 249}, {'label': 'SBP', 'value': 250}, {'label': 'SCE', 'value': 251}, {'label': 'RST', 'value': 252}, {'label': 'nan', 'value': -2}, {'label': 'RST', 'value': 252}
            ],
            value = 2,
            className='mb-3',
            placeholder='Select your Destination Location...'
        ),
        dcc.Markdown('##### **MONTH OF FLIGHT**'),
        dcc.Dropdown(
            id='Quarter',
            options = [
                {'label': 'January', 'value': 1},
                {'label': 'February', 'value': 1},
                {'label': 'March', 'value': 1},
                {'label': 'April', 'value': 2},
                {'label': 'May', 'value': 2},
                {'label': 'June', 'value': 2},
                {'label': 'July', 'value': 3},
                {'label': 'August', 'value': 3},
                {'label': 'September', 'value': 3},
                {'label': 'October', 'value': 4},
                {'label': 'November', 'value': 4},
                {'label': 'December', 'value': 4},
            ],
            value = 1,
            className='mb-3',
            placeholder='Select your Month of Flight...'
        ),
        dcc.Markdown('##### **QTY OF TICKETS TO ORDER**'),
        dcc.Slider(
            id='NumTicketsOrdered',
            min=1,
            max=20,
            step=1,
            value=1,
            marks={n: str(n) for n in range(1,21,1)},
            className='mb-3',
        ),
    ],
    md=4,
)

column2 = dbc.Col(
    [
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    #html.Img(src='assets/Shapley Force Plots used for explaining decision tree outcome of individual instances -- Ryan Zernach Zernach.com -- Airline Price Predictions.png', className='img-fluid', height=500, width=750),
    html.H2('Predicted Flight Price', className= 'mb-3'),
    html.Div(id='prediction-content', className='lead')
    ]
    #md=6,
)

layout = dbc.Row([column1, column2])

@app.callback(
    Output('prediction-content', 'children'),
    [Input('AirlineCompany', 'value'),
    Input('Origin', 'value'),
    Input('Dest', 'value'),
    Input('Quarter', 'value'),
    Input('NumTicketsOrdered', 'value')]
)


def predict(Quarter, Origin, Dest, NumTicketsOrdered, AirlineCompany):

    #miles_check_str = f'{origin_dict[Origin]} -> {dest_dict[Dest]}'
    #Miles = miles_dict[miles_check_str]

    df = pd.DataFrame(
        data=[[Quarter, Origin, Dest, NumTicketsOrdered, AirlineCompany]],
        columns=['Quarter', 'Origin', 'Dest', 'NumTicketsOrdered', 'AirlineCompany']
    )

    PricePerTicket = str(pipeline.predict(df)[0])[0:6]
    PricePerTicket = f"${PricePerTicket}"

    return PricePerTicket
