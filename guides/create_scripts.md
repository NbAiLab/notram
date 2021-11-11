# Create scripts
These scripts are used for creating the json-files (2) from the source-files (1). 

## create_cc100.py
Process the CC100 corpus. Output is UTF-8 JSON lines
```
optional arguments:
  -h, --help            show this help message and exit
  --language_reported LANGUAGE_REPORTED
                        Language reported. Can be nob, nno, no or N/A
  --doc_type DOC_TYPE   For instance cc100_no
  --input_file INPUT_FILE
                        Input file
  --output_file OUTPUT_FILE
                        Output file
```

## create_facebook.py
Convert the WEB64 Facebook corpus to jsonl. This corpus is in json format. Output is a jsonl UTF-8 file with one post per line
```
optional arguments:
  -h, --help            show this help message and exit
  --language_reported LANGUAGE_REPORTED
                        Language reported. Can be nob, nno, no or N/A
  --doc_type DOC_TYPE   For instance government
  --output_file OUTPUT_FILE
                        Output file name. Will overwrite it exists
  --input_folder INPUT_FOLDER
                        Input folder. Will read all files in folder
```

## create_government.py
Process the corpus downloaded from the governments API. The corpus consists of multiple files in xhtml format. Output is an UTF-8 json-lines-file with one document per line
```
optional arguments:
  -h, --help            show this help message and exit
  --language_reported LANGUAGE_REPORTED
                        Language reported. Can be nob, nno, no or N/A
  --doc_type DOC_TYPE   For instance government
  --output_file OUTPUT_FILE
                        Output file name. Will overwrite it exists
  --input_folder INPUT_FOLDER
                        Input folder. Will read all files in folder
```

## create_lovdata_cd.py
Create jsonl from the Lovdata CD. This content does have double breaks between each artile. Some meta-info is collected from the file names. Output is an UTF-8 file with one article per line

```
optional arguments:
  -h, --help            show this help message and exit
  --language_reported LANGUAGE_REPORTED
                        Language reported. Can be nob, nno, no or N/A
  --doc_type DOC_TYPE   For instance cc100_no
  --input_folder INPUT_FOLDER
                        Input file
  --output_file OUTPUT_FILE
                        Output file
```

## create_lovdata_transfer.py
Process the transferred Lovdata corpus. Output is an UTF-8 JSON lines

```
optional arguments:
  -h, --help            show this help message and exit
  --language_reported LANGUAGE_REPORTED
                        Language reported
  --doc_type DOC_TYPE   Doctype
  --input_file INPUT_FILE
                        Input file
  --output_file OUTPUT_FILE
                        Output file
```

## create_maalfrid.py
Create jsonl from mupdf-created Maalfrid documents. Output is an UTF-8 JSON lines
```
optional arguments:
  -h, --help            show this help message and exit
  --language_reported LANGUAGE_REPORTED
                        Language reported. Can be nob, nno, no or N/A
  --doc_type DOC_TYPE   For instance maalfrid
  --input_folder INPUT_FOLDER
                        Input folder
  --meta_file META_FILE
                        Meta file from Språkbanken in csv format
  --output_file OUTPUT_FILE
                        Output file
```

## create_mc4.py
Convert the MC4 to our json-format. This corpus is in ascii json format. Output is an UTF-8 file with one document per line
```
optional arguments:
  -h, --help            show this help message and exit
  --language_reported LANGUAGE_REPORTED
                        Language reported. Can be nob, nno, no or N/A
  --doc_type DOC_TYPE   For instance government
  --output_file OUTPUT_FILE
                        Output file name. Will overwrite it exists
  --input_file INPUT_FILE
                        Input file name.
```

## create_newspapers_online.py
Processing the newspaper corpus published by Språkbanken. Output is an UTF-8 JSON lines
```
optional arguments:
  -h, --help            show this help message and exit
  -i INPUT_PATH, --input_path INPUT_PATH
                        Input path
  -o OUTPUT_FILE, --output_file OUTPUT_FILE
                        Output file
  --doc_type DOC_TYPE   Doc type
  -l LANGUAGE_REPORTED, --language_reported LANGUAGE_REPORTED
                        Language. nob, nno or . Folder names determine language.
```

## create_newspapers_pdf.py
Convert extracted plain text from mupdf to JSON lines
```
optional arguments:
  -h, --help            show this help message and exit
  --input_dir input_dir
                        Input directory
  --input_dir_glob input_dir_glob
                        Input directory glob
  --output_dir output_dir
                        Output directory
  --doc_type doc_type   Document type
  --pymupdf_version pymupdf_version
                        PyMuPDF version
  --report_parsing_error report_parsing_error
                        Report filename parsing errors
    
```

## create_opensubtitles.py
Process OpenSubtitles. Output is an UTF-8 JSON lines
```
optional arguments:
  -h, --help            show this help message and exit
  --language_reported LANGUAGE_REPORTED
                        Language reported. Can be nob, nno, no or N/A
  --doc_type DOC_TYPE   For instance government
  --output_file OUTPUT_FILE
                        Output file name. Will overwrite it exists
  --input_folder INPUT_FOLDER
                        Input folder. Will read all files in folder
```

## create_oscar.py
Process the OSCAR corpus. This corpus has one document per line. No paragraphs. Output is an UTF-8 JSON lines
```
optional arguments:
  -h, --help            show this help message and exit
  --language_reported LANGUAGE_REPORTED
                        Language reported
  --doc_type DOC_TYPE   Doctype
  --input_file INPUT_FILE
                        Input file
  --output_file OUTPUT_FILE
                        Output file
```

## create_parliament.py
Create corpus from parliament files! Output is an UTF-8 JSON lines
```
optional arguments:
  -h, --help            show this help message and exit
  --input_file INPUT_FILE
                        Input file
  --output_file OUTPUT_FILE
                        Output file
```

## create_publicreports.py
Create Public Report jsonl from downloaded text files. This corpus is formed as a document per line. No paragraphs.Output is an UTF-8 JSON lines

```
optional arguments:
  -h, --help            show this help message and exit
  --language_reported LANGUAGE_REPORTED
                        Language reported
  --doc_type DOC_TYPE   Doctype
  --input_file INPUT_FILE
                        Input file
  --output_file OUTPUT_FILE
                        Output file
```

## create_reddit.py
Create the Reddit corpus from the downloaded archive. Output is an UTF-8 JSON lines

```
optional arguments:
  -h, --help            show this help message and exit
  --language_reported LANGUAGE_REPORTED
                        Language reported. Can be nob, nno, no or N/A
  --doc_type DOC_TYPE   For instance government
  --year YEAR           Selects only one year
  -o OUTPUT_FILE, --output_file OUTPUT_FILE
                        Output file name. Will overwrite it exists
  -i INPUT_FOLDER, --input_folder INPUT_FOLDER
                        Input folder. Will read all files in folder
```

## create_twitter.py
Process the twitter corpus in json format. Output is an UTF-8 JSON lines

```
optional arguments:
  -h, --help            show this help message and exit
  --language_reported LANGUAGE_REPORTED
                        Language reported. Can be nob, nno, no or N/A
  --doc_type DOC_TYPE   For instance tweet
  -o OUTPUT_FILE, --output_file OUTPUT_FILE
                        Output file name. Will overwrite it exists
  -i INPUT_FOLDER, --input_folder INPUT_FOLDER
                        Input folder. Will read all files in folder
```

## create_vgdebatt.py
Convert vgdebatt to jsonl. This corpus is originally in json format. Output is an UTF-8 JSON lines

```
optional arguments:
  -h, --help            show this help message and exit
  --language_reported LANGUAGE_REPORTED
                        Language reported. Can be nob, nno, no or N/A
  --doc_type DOC_TYPE   For instance tweet
  --output_file OUTPUT_FILE
                        Output file name. Will overwrite it exists
  --input_folder INPUT_FOLDER
                        Input folder. Will read all files in folder
```

## create_wikipedia_download.py
Process the downloaded Wikipedia files. Output is an UTF-8 JSON lines

```
optional arguments:
  -h, --help            show this help message and exit
  --language_reported LANGUAGE_REPORTED
                        Language reported. Can be nob, nno, no, da, sv, is or N/A
  --doc_type DOC_TYPE   For instance wikipedia_download_no
  --year YEAR           Selects only one year
  -o OUTPUT_FILE, --output_file OUTPUT_FILE
                        Output file name. Will overwrite it exists
  -i INPUT_FILE, --input_file INPUT_FILE
                        Input file.
```

## create_wikipedia_huggingface_en.py
Create Wikipedia jsonl from Hugging Face. Output is an UTF-8 JSON lines

```
optional arguments:
  -h, --help            show this help message and exit
  --language_reported LANGUAGE_REPORTED
                        Language reported
  --doc_type DOC_TYPE   Doctype
  --output_file OUTPUT_FILE
                        Output file
```

## create_wikipedia_spraakbanken.py
Process the Wikipedia dump published by Språkbanken. Output is UTF-8 JSON lines

```
optional arguments:
  -h, --help            show this help message and exit
  --language_reported LANGUAGE_REPORTED
                        Language reported
  --doc_type DOC_TYPE   Doc type
  --input_file INPUT_FILE
                        Input file
  --output_file OUTPUT_FILE
                        Output file
```

## Statistics
### Document Types
| Source                                |     Words |   Documents |   Words/Document |
|:--------------------------------------|----------:|------------:|-----------------:|
| books                                 | 695706046 |       21863 |            31821 |
| newspaper_ocr                         | 539149808 |     2746578 |              196 |
| newspaper_pdf                         | 144735561 |      273296 |              529 |
| mc4                                   |  79147631 |      169261 |              467 |
| newspapers_online_nn                  |  30923957 |      114648 |              269 |
| vgdebatt                              |  19361061 |      589835 |               32 |
| wikipedia_download_nno                |  18704231 |      121834 |              153 |
| facebook                              |  15142291 |      482520 |               31 |
| maalfrid_regjeringen                  |  14232525 |       32959 |              431 |
| maalfrid_fylkesmannen                 |  11393633 |       38957 |              292 |
| twitter                               |  10852891 |      745034 |               14 |
| government_nn                         |   6869074 |         437 |            15718 |
| lovdata_transfer                      |   6039785 |      119179 |               50 |
| maalfrid_ssb                          |   4817258 |       15869 |              303 |
| maalfrid_nasjonalparkstyre            |   3738703 |       13575 |              275 |
| maalfrid_nve                          |   3253555 |       12684 |              256 |
| maalfrid_vegvesen                     |   2527519 |       10752 |              235 |
| oscar                                 |   2020760 |       47882 |               42 |
| maalfrid_hivolda                      |   1877160 |        5730 |              327 |
| lovdata_cd_odelsting_2005             |   1375894 |         122 |            11277 |
| maalfrid_uio                          |   1251268 |        5130 |              243 |
| maalfrid_vestlandfylke                |   1198943 |        4195 |              285 |
| maalfrid_sprakradet                   |   1196086 |        3479 |              343 |
| maalfrid_uib                          |   1088035 |        4149 |              262 |
| Published_article                     |    996765 |         540 |             1845 |
| twitter_news                          |    981550 |       68784 |               14 |
| maalfrid_ntnu                         |    731426 |        2588 |              282 |
| cc100                                 |    679347 |       35898 |               18 |
| maalfrid_distriktssenteret            |    618956 |        2176 |              284 |
| publicreports                         |    602612 |          30 |            20087 |
| government_nb                         |    541809 |          39 |            13892 |
| maalfrid_skatteetaten                 |    507828 |         934 |              543 |
| maalfrid_domstol                      |    477994 |        1507 |              317 |
| maalfrid_moreforsk                    |    455515 |        1475 |              308 |
| maalfrid_arkivverket                  |    377493 |        1160 |              325 |
| maalfrid_kulturradet                  |    362520 |        1085 |              334 |
| lovdata_cd_lokaleforskrifter_2005     |    355844 |        2339 |              152 |
| maalfrid_landbruksdirektoratet        |    324305 |        1272 |              254 |
| maalfrid_nlr                          |    314711 |        1149 |              273 |
| maalfrid_dsb                          |    305845 |         880 |              347 |
| maalfrid_hvl                          |    302309 |        1215 |              248 |
| maalfrid_difi                         |    262356 |         970 |              270 |
| maalfrid_nynorsksenteret              |    259849 |        1077 |              241 |
| maalfrid_banenor                      |    229943 |         974 |              236 |
| maalfrid_helsetilsynet                |    209825 |         540 |              388 |
| maalfrid_nav                          |    205651 |         706 |              291 |
| newspapers_online_nb                  |    202443 |        6774 |               29 |
| maalfrid_nmbu                         |    197047 |         708 |              278 |
| maalfrid_udir                         |    188548 |         765 |              246 |
| maalfrid_hi                           |    183558 |         603 |              304 |
| maalfrid_mattilsynet                  |    173384 |         518 |              334 |
| lovdata_cd_somb_rundskriv_2005        |    139159 |          86 |             1618 |
| maalfrid_fiskeridir                   |    130779 |         497 |              263 |
| maalfrid_norges-bank                  |    127351 |         417 |              305 |
| maalfrid_oslomet                      |    124734 |         299 |              417 |
| maalfrid_bioteknologiradet            |    120544 |         301 |              400 |
| maalfrid_forsvarsbygg                 |    112235 |         336 |              334 |
| maalfrid_lottstift                    |    108542 |         348 |              311 |
| maalfrid_dirmin                       |    106011 |         346 |              306 |
| maalfrid_custompublish                |    103563 |         359 |              288 |
| maalfrid_uis                          |    101192 |         288 |              351 |
| maalfrid_aasentunet                   |     98991 |         289 |              342 |
| maalfrid_dsa                          |     98757 |         412 |              239 |
| maalfrid_veiviseren                   |     95305 |         236 |              403 |
| maalfrid_nysgjerrigper                |     93767 |         423 |              221 |
| maalfrid_nokut                        |     93124 |         386 |              241 |
| maalfrid_kartverket                   |     82224 |         343 |              239 |
| maalfrid_ks                           |     76543 |         350 |              218 |
| wikipedia_download_nbo                |     73985 |        1703 |               43 |
| maalfrid_hiof                         |     72934 |         324 |              225 |
| maalfrid_riksrevisjonen               |     72733 |         218 |              333 |
| maalfrid_naturfag                     |     71884 |         434 |              165 |
| maalfrid_ngu                          |     69591 |         310 |              224 |
| maalfrid_medietilsynet                |     68375 |         289 |              236 |
| lovdata_cd_sentrale_forskrifter_2005  |     68149 |         205 |              332 |
| maalfrid_nfi                          |     66947 |         215 |              311 |
| lovdata_cd_norgeslover_2005           |     65947 |          67 |              984 |
| maalfrid_riksantikvaren               |     64512 |         227 |              284 |
| maalfrid_skrivesenteret               |     63926 |         325 |              196 |
| maalfrid_kystverket                   |     63760 |         279 |              228 |
| maalfrid_fhi                          |     63276 |         344 |              183 |
| maalfrid_forskningsradet              |     62887 |         194 |              324 |
| lovdata_cd_skatt_rundskriv_2005       |     61015 |          30 |             2033 |
| maalfrid_nibio                        |     56566 |         210 |              269 |
| maalfrid_khrono                       |     56090 |         210 |              267 |
| maalfrid_legemiddelverket             |     55521 |         214 |              259 |
| maalfrid_sdir                         |     55000 |         209 |              263 |
| maalfrid_dfo                          |     52909 |         216 |              244 |
| maalfrid_nbim                         |     52439 |         202 |              259 |
| maalfrid_udi                          |     52054 |         183 |              284 |
| maalfrid_polarhistorie                |     51486 |          62 |              830 |
| maalfrid_samordnaopptak               |     49505 |         117 |              423 |
| maalfrid_miljodirektoratet            |     48327 |         207 |              233 |
| maalfrid_barneombudet                 |     47881 |         136 |              352 |
| maalfrid_helsedirektoratet            |     46535 |         208 |              223 |
| maalfrid_helsenorge                   |     46110 |         150 |              307 |
| maalfrid_kompetansenorge              |     46081 |         234 |              196 |
| maalfrid_uia                          |     44364 |         146 |              303 |
| maalfrid_nhh                          |     43105 |         148 |              291 |
| maalfrid_samas                        |     42289 |         150 |              281 |
| maalfrid_klagenemndssekretariatet     |     37741 |         101 |              373 |
| maalfrid_politiet                     |     37680 |         152 |              247 |
| maalfrid_statsbygg                    |     36324 |         138 |              263 |
| maalfrid_konkurransetilsynet          |     36178 |         152 |              238 |
| maalfrid_toll                         |     35851 |         150 |              239 |
| maalfrid_matematikksenteret           |     35747 |         301 |              118 |
| maalfrid_imdi                         |     35624 |         111 |              320 |
| maalfrid_havarikommisjonen            |     32935 |         118 |              279 |
| maalfrid_husbanken                    |     32618 |         100 |              326 |
| maalfrid_dibk                         |     31616 |         210 |              150 |
| maalfrid_godeidrettsanlegg            |     31391 |         116 |              270 |
| maalfrid_nasjonalmuseet               |     28032 |          89 |              314 |
| maalfrid_nb                           |     26432 |         109 |              242 |
| maalfrid_nyemetoder                   |     26264 |         106 |              247 |
| maalfrid_himolde                      |     26166 |         251 |              104 |
| maalfrid_forskningsetikk              |     25749 |          61 |              422 |
| maalfrid_vetinst                      |     25562 |         100 |              255 |
| maalfrid_norad                        |     24786 |          48 |              516 |
| maalfrid_xn--miljlftet-o8ab           |     23812 |          94 |              253 |
| maalfrid_stami                        |     23377 |          49 |              477 |
| maalfrid_nsm                          |     22925 |          59 |              388 |
| maalfrid_patentstyret                 |     20715 |          98 |              211 |
| maalfrid_riksteatret                  |     20627 |          93 |              221 |
| maalfrid_naturfagsenteret             |     20486 |         132 |              155 |
| maalfrid_ptil                         |     20449 |          88 |              232 |
| maalfrid_nupi                         |     20035 |          91 |              220 |
| maalfrid_spk                          |     19768 |          67 |              295 |
| maalfrid_naku                         |     18936 |          47 |              402 |
| maalfrid_squarespace                  |     17409 |          60 |              290 |
| maalfrid_diku                         |     17247 |          79 |              218 |
| maalfrid_npe                          |     16935 |          73 |              231 |
| maalfrid_inn                          |     16531 |         133 |              124 |
| maalfrid_opplaringslovutvalget        |     15698 |          41 |              382 |
| maalfrid_nkom                         |     15130 |          64 |              236 |
| maalfrid_met                          |     13662 |          72 |              189 |
| maalfrid_forbrukerradet               |     13500 |          60 |              225 |
| maalfrid_diskrimineringsnemnda        |     13415 |          52 |              257 |
| maalfrid_luftfartstilsynet            |     13209 |          76 |              173 |
| maalfrid_ldo                          |     12836 |          71 |              180 |
| maalfrid_nynorskbok                   |     12656 |          61 |              207 |
| maalfrid_digidel                      |     12390 |          66 |              187 |
| maalfrid_bibliotekutvikling           |     11596 |          59 |              196 |
| maalfrid_helfo                        |     11048 |          72 |              153 |
| maalfrid_nord                         |     11038 |          63 |              175 |
| maalfrid_lokalhistorie                |     11012 |          40 |              275 |
| maalfrid_aho                          |     10881 |          39 |              279 |
| maalfrid_usn                          |     10605 |          56 |              189 |
| maalfrid_bufdir                       |     10321 |          51 |              202 |
| maalfrid_vinmonopolet                 |      9607 |          25 |              384 |
| maalfrid_khio                         |      9597 |          55 |              174 |
| maalfrid_aldringoghelse               |      8907 |          15 |              593 |
| maalfrid_matportalen                  |      8862 |          40 |              221 |
| maalfrid_forbrukertilsynet            |      8700 |          28 |              310 |
| maalfrid_beccle                       |      8491 |          30 |              283 |
| maalfrid_seniorporten                 |      7625 |          29 |              262 |
| maalfrid_sykkelbynettverket           |      7609 |          69 |              110 |
| maalfrid_forsvaret                    |      7394 |          24 |              308 |
| maalfrid_kunstkultursenteret          |      7148 |          25 |              285 |
| maalfrid_datatilsynet                 |      7144 |          21 |              340 |
| maalfrid_koro                         |      6957 |          30 |              231 |
| maalfrid_artsdatabanken               |      6812 |          23 |              296 |
| maalfrid_uit                          |      6532 |          18 |              362 |
| maalfrid_sismo                        |      6234 |          21 |              296 |
| maalfrid_vkm                          |      5852 |          19 |              308 |
| maalfrid_digdir                       |      5709 |          34 |              167 |
| lovdata_cd_rundskriv_lovavdeling_2005 |      5677 |           5 |             1135 |
| maalfrid_unknown                      |      5561 |          36 |              154 |
| maalfrid_okokrim                      |      5453 |          18 |              302 |
| maalfrid_mareano                      |      5360 |          12 |              446 |
| maalfrid_arbeidstilsynet              |      4896 |          18 |              272 |
| maalfrid_npd                          |      4883 |          14 |              348 |
| maalfrid_lektor2                      |      4846 |          30 |              161 |
| maalfrid_nodnett                      |      4471 |          29 |              154 |
| maalfrid_jernbanemagasinet            |      4206 |           9 |              467 |
| maalfrid_kjonnsforskning              |      4112 |          17 |              241 |
| maalfrid_brreg                        |      4054 |          23 |              176 |
| maalfrid_regionaleforskningsfond      |      3639 |          17 |              214 |
| maalfrid_natursekken                  |      3590 |          31 |              115 |
| maalfrid_yr                           |      3554 |          48 |               74 |
| maalfrid_jernbanedirektoratet         |      3536 |          36 |               98 |
| maalfrid_valgdirektoratet             |      3367 |          36 |               93 |
| maalfrid_lanekassen                   |      3349 |           9 |              372 |
| maalfrid_fellesstudentsystem          |      3211 |          35 |               91 |
| maalfrid_nlb                          |      3063 |          16 |              191 |
| maalfrid_informasjonskompetanse       |      3059 |          23 |              133 |
| maalfrid_unit                         |      3049 |          33 |               92 |
| maalfrid_fug                          |      3000 |           9 |              333 |
| maalfrid_varsom                       |      2958 |          27 |              109 |
| maalfrid_realfagsloyper               |      2830 |          12 |              235 |
| maalfrid_anskaffelser                 |      2730 |          25 |              109 |
| maalfrid_hjelpemiddeldatabasen        |      2651 |          52 |               50 |
| maalfrid_nih                          |      2644 |          26 |              101 |
| maalfrid_une                          |      2598 |          10 |              259 |
| maalfrid_giek                         |      2437 |          10 |              243 |
| maalfrid_fiskeridirektoratet          |      2341 |           8 |              292 |
| maalfrid_kulturminnefondet            |      2088 |          11 |              189 |
| maalfrid_politihogskolen              |      1937 |           7 |              276 |
| lovdata_cd_rtv_rundskriv_2005         |      1879 |          61 |               30 |
| maalfrid_arbeidsretten                |      1791 |           8 |              223 |
| maalfrid_ehelse                       |      1707 |          54 |               31 |
| maalfrid_denkulturelleskolesekken     |      1570 |           7 |              224 |
| reddit                                |      1499 |         132 |               11 |
| maalfrid_mhfa                         |      1464 |          17 |               86 |
| maalfrid_ovf                          |      1416 |           5 |              283 |
| maalfrid_htu                          |      1396 |           6 |              232 |
| maalfrid_dekom                        |      1357 |          26 |               52 |
| maalfrid_sjt                          |      1266 |          17 |               74 |
| maalfrid_nhn                          |      1161 |          12 |               96 |
| maalfrid_nasjonaleturistveger         |      1119 |           3 |              373 |
| maalfrid_unesco                       |      1093 |           4 |              273 |
| maalfrid_gjenopptakelse               |      1016 |           3 |              338 |
| maalfrid_pasientsikkerhetsprogrammet  |      1007 |          32 |               31 |
| maalfrid_energimerking                |       967 |           4 |              241 |
| maalfrid_ssn                          |       808 |           8 |              101 |
| maalfrid_sivilforsvaret               |       772 |           4 |              193 |
| maalfrid_laudim                       |       733 |           3 |              244 |
| maalfrid_helseklage                   |       708 |           4 |              177 |
| maalfrid_miljoklagenemnda             |       623 |           2 |              311 |
| maalfrid_spesialenheten               |       535 |           3 |              178 |
| maalfrid_hjorteviltregisteret         |       516 |           1 |              516 |
| maalfrid_russamtalen                  |       488 |           1 |              488 |
| maalfrid_kulturfag                    |       466 |           2 |              233 |
| maalfrid_radetfordyreetikk            |       461 |           2 |              230 |
| maalfrid_folketrygdfondet             |       400 |           3 |              133 |
| maalfrid_miljopakken                  |       321 |           8 |               40 |
| maalfrid_universell                   |       246 |           9 |               27 |
| maalfrid_skeivtarkiv                  |       171 |           1 |              171 |
| maalfrid_yrkesfisker                  |       161 |           4 |               40 |
| maalfrid_kriminalitetsforebygging     |       138 |           5 |               27 |
| subtitles                             |       120 |           5 |               24 |
| maalfrid_konkursradet                 |       107 |           1 |              107 |
| maalfrid_designavgang                 |       103 |           1 |              103 |
| maalfrid_sykehusinnkjop               |       102 |           6 |               17 |
| maalfrid_traumebevisst                |        81 |           6 |               13 |
| maalfrid_xn--forskerfr-t8a            |        62 |           2 |               31 |
| maalfrid_feide                        |        59 |           1 |               59 |
| maalfrid_sshf                         |        56 |           2 |               28 |
| maalfrid_sykehuspartner               |        50 |           6 |                8 |
| maalfrid_uh-it                        |        44 |           2 |               22 |
| maalfrid_samfunnskunnskap             |        37 |           1 |               37 |
| maalfrid_vea-fs                       |        35 |           3 |               11 |
| wikipedia_huggingface                 |        34 |           2 |               17 |
| maalfrid_justervesenet                |        32 |           1 |               32 |
| maalfrid_pts                          |        29 |           2 |               14 |
| maalfrid_lokforerskolen               |         8 |           2 |                4 |
| maalfrid_geonorge                     |         8 |           2 |                4 |
| maalfrid_memu                         |         8 |           1 |                8 |
| maalfrid_romsenter                    |         6 |           1 |                6 |
| maalfrid_iearth                       |         6 |           1 |                6 |
| maalfrid_fordelingsutvalget           |         4 |           1 |                4 |

### Languages
| Language   |      Words |   Documents |   Words/Document |
|:-----------|-----------:|------------:|-----------------:|
| nn         | 1632641633 |     5736773 |              284 |

### Publish Periode
|   Decade |       Words |        Documents |   Words/Document |
|---------:|------------:|-----------------:|-----------------:|
|     2020 | 2.0556e+08  | 821261           |              623 |
|     2010 | 5.86038e+08 |      3.57512e+06 |             1951 |
|     2000 | 2.85951e+08 | 863172           |             5368 |
|     1990 | 2.68046e+08 | 208054           |            13053 |
|     1980 | 1.67883e+08 | 154901           |            10877 |
|     1970 | 1.19164e+08 | 114264           |            10120 |

