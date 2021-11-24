[<img align="right" width="150px" src="../images/nblogo.png">](https://ai.nb.no)
# Norwegian Colossal Corpus
This page summarizes the Norwegian Collossal Corpus. The corpus is a collection of multiple smaller Norwegian corpuses that are suitable for training large language models. We have done extensive cleaning on the datasets, and have made them available in a common format.


## Government Reports
A collection of documents and reports from the Norwegian government. The files are downloaded directly from the government API in a native xhtml-format that they use for creating both Word and pdf reports. In pre-processing typically headings, tables, footnotes etc are filtered out.

| License  | Size | Words | Documents | Avg words per doc  |
| -------- |   :-----|   -----:| -----:| -----:|
| [NLOD 2.0](https://data.norge.no/nlod/en/2.0/)|1.1 GB| 155,318,754 | 4,648       | 33,416           |

<details>
<summary>View dataset statistics</summary>
 
### Document Types
| Source        | Words       | Documents   | Words/Document   |
|--------------:|------------:|------------:|-----------------:|
| government_nb | 136,708,062 | 3,557       | 38,433           |
| government_nn | 18,610,692  | 1,091       | 17,058           |

### Languages
| Language   | Words       | Documents   | Words/Document   |
|-----------:|------------:|------------:|-----------------:|
| no         | 146,885,219 | 4,134       | 35,531           |
| nn         | 8,246,002   | 500         | 16,492           |
| da         | 182,720     | 13          | 14,055           |
| en         | 4,813       | 1           | 4,813            |

### Publish Periode
|   Decade | Words       | Documents   | Words/Document   |
|---------:|------------:|------------:|-----------------:|
|     2020 | 155,318,754 | 4,648       | 33,416           |

</details>


## Parliament Collections
**NEED MORE TEXT HERE - WHO HAS COLLECTED THIS** Also referred to as Stortingsforhandlingene. Collection of documents from the Norwegian Parliament. The corpus contains mainly OCRed reports. Part of the collection at the National Library. 
| License  | Size | Words | Documents | Avg words per doc  |
| -------- |   :-----|   -----:| -----:| -----:|
| [NLOD 2.0](https://data.norge.no/nlod/en/2.0/)| GB| 1,301,766,124 | 9,528       | 136,625          |

<details>
<summary>View dataset statistics</summary>

 ### Document Types
| Source     | Words         | Documents   | Words/Document   |
|-----------:|--------------:|------------:|-----------------:|
| parliament | 1,301,766,124 | 9,528       | 136,625          |

### Languages
| Language   | Words       | Documents   | Words/Document   |
|-----------:|------------:|------------:|-----------------:|
| no         | 885,007,390 | 6,478       | 136,617          |
| da         | 416,758,734 | 3,050       | 136,642          |

### Publish Periode
|   Decade | Words         | Documents   | Words/Document   |
|---------:|--------------:|------------:|-----------------:|
|     2020 | 1,301,766,124 | 9,528       | 136,625          |
 
</details>


## Pulic Reports
**NEED MORE TEXT HERE** Also referred to as __Evalueringsrapporter__. The corpus contains mainly OCRed reports. Part of the collection at the National Library. 

| License  | Size | Words | Documents | Avg words per doc  |
| -------- |   :-----|   -----:| -----:| -----:|
| [NLOD 2.0](https://data.norge.no/nlod/en/2.0/)|0.5 GB| 80,064,396 | 3,365       | 23,793           |

<details>
<summary>View dataset statistics</summary>

### Document Types
| Source        | Words      | Documents   | Words/Document   |
|--------------:|-----------:|------------:|-----------------:|
| publicreports | 80,064,396 | 3,365       | 23,793           |

### Languages
| Language   | Words      | Documents   | Words/Document   |
|-----------:|-----------:|------------:|-----------------:|
| no         | 65,026,196 | 2,721       | 23,897           |
| en         | 13,093,711 | 556         | 23,549           |
| nn         | 677,921    | 32          | 21,185           |
| sv         | 381,007    | 14          | 27,214           |
| da         | 290,817    | 12          | 24,234           |
| fr         | 158,454    | 4           | 39,613           |
| es         | 144,681    | 4           | 36,170           |
| et         | 109,339    | 8           | 13,667           |
| zh         | 88,848     | 3           | 29,616           |
| fi         | 68,910     | 4           | 17,227           |
| gu         | 16,739     | 1           | 16,739           |
| ru         | 7,356      | 1           | 7,356            |
| uk         | 268        | 1           | 268              |
| pt         | 113        | 1           | 113              |
| it         | 27         | 1           | 27               |
| de         | 5          | 1           | 5                |
| ja         | 4          | 1           | 4                |

### Publish Periode
|   Decade | Words      | Documents   | Words/Document   |
|---------:|-----------:|------------:|-----------------:|
|     2020 | 80,064,396 | 3,365       | 23,793           |
 
</details>


## LovData CD
CD/DVD last published in 2005. Contains a very complete collection of legal resources, including laws, NOUs etc. The collection is now out of database protextion. We have cleaned out resources that might contain personal information. 

| License  | Size | Words | Documents | Avg words per doc  |
| -------- |   :-----|   -----:| -----:| -----:|
| [NLOD 2.0](https://data.norge.no/nlod/en/2.0/)|0.4 GB| 54,923,432 | 51,920      | 1,057            |
<details>
<summary>View dataset statistics</summary>
 
### Document Types
| Source                                | Words      | Documents   | Words/Document   |
|--------------------------------------:|-----------:|------------:|-----------------:|
| lovdata_cd_odelsting_2005             | 37,295,277 | 1,987       | 18,769           |
| lovdata_cd_somb_rundskriv_2005        | 5,400,486  | 3,284       | 1,644            |
| lovdata_cd_sentrale_forskrifter_2005  | 5,178,057  | 11,745      | 440              |
| lovdata_cd_lokaleforskrifter_2005     | 2,233,543  | 22,824      | 97               |
| lovdata_cd_norgeslover_2005           | 1,802,578  | 1,419       | 1,270            |
| lovdata_cd_rtv_rundskriv_2005         | 1,392,547  | 9,831       | 141              |
| lovdata_cd_skatt_rundskriv_2005       | 1,138,339  | 411         | 2,769            |
| lovdata_cd_rundskriv_lovavdeling_2005 | 482,605    | 419         | 1,151            |

### Languages
| Language   | Words      | Documents   | Words/Document   |
|-----------:|-----------:|------------:|-----------------:|
| no         | 52,225,155 | 46,032      | 1,134            |
| nn         | 2,369,924  | 3,261       | 726              |
| da         | 173,296    | 1,146       | 151              |
| en         | 104,233    | 423         | 246              |
| sv         | 32,861     | 637         | 51               |
| es         | 4,744      | 49          | 96               |
| nl         | 3,818      | 212         | 18               |
| it         | 3,768      | 6           | 628              |
| de         | 3,179      | 58          | 54               |
| fr         | 1,801      | 7           | 257              |
| pl         | 513        | 57          | 9                |
| tr         | 22         | 1           | 22               |
| fi         | 14         | 4           | 3                |
| als        | 12         | 3           | 4                |
| et         | 11         | 2           | 5                |
| ca         | 11         | 3           | 3                |
| zh         | 11         | 3           | 3                |
| pt         | 11         | 1           | 11               |
| la         | 8          | 1           | 8                |
| eu         | 7          | 2           | 3                |
| hr         | 7          | 2           | 3                |
| ru         | 5          | 2           | 2                |
| sk         | 4          | 1           | 4                |
| lt         | 3          | 1           | 3                |
| ro         | 3          | 1           | 3                |
| sl         | 3          | 1           | 3                |
| eo         | 2          | 1           | 2                |
| am         | 2          | 1           | 2                |
| cy         | 2          | 1           | 2                |
| ms         | 2          | 1           | 2                |

### Publish Periode
|   Decade | Words      | Documents   | Words/Document   |
|---------:|-----------:|------------:|-----------------:|
|     2020 | 54,923,432 | 51,920      | 1,057            |
</details>


## Målfrid Collection
A collection of more than 9.2M public documents in pdf-format from 311 different sources. Collected from Språkbanken. We are using the part that is possible to read as text (roughly 6M documents). The largest sources are ssb (1.5M), regjeringen (1M), Uio (1M), fylkesmannen (0.7M), nve (0.4M), ntnu (0.3M), patentstyret (0.2M), vegvesenen (0.2M), fhi (0.2M).

| License  | Size | Words | Documents | Avg words per doc  |
| -------- |   :-----|   -----:| -----:| -----:|
| [NLOD 2.0](https://data.norge.no/nlod/en/2.0/)|14.0 GB| 1,905,481,776 | 6,735,367   |              282 |
<details>
<summary>View dataset statistics</summary>

### Document Types
| Source                                | Words       | Documents   |   Words/Document |
|--------------------------------------:|------------:|------------:|-----------------:|
| maalfrid_regjeringen                  | 368,581,046 | 940,936     |              391 |
| maalfrid_ssb                          | 286,024,711 | 871,262     |              328 |
| maalfrid_uio                          | 186,003,655 | 788,988     |              235 |
| maalfrid_fylkesmannen                 | 105,197,005 | 473,582     |              222 |
| maalfrid_nve                          | 68,194,530  | 308,924     |              220 |
| maalfrid_patentstyret                 | 66,482,941  | 218,930     |              303 |
| maalfrid_ntnu                         | 59,108,726  | 203,770     |              290 |
| maalfrid_vegvesen                     | 34,177,213  | 169,998     |              201 |
| maalfrid_fhi                          | 33,541,094  | 147,668     |              227 |
| maalfrid_norad                        | 33,454,341  | 95,191      |              351 |
| maalfrid_skatteetaten                 | 33,313,013  | 84,448      |              394 |
| maalfrid_uib                          | 29,049,820  | 118,328     |              245 |
| maalfrid_forskningsradet              | 24,647,599  | 75,104      |              328 |
| maalfrid_nasjonalparkstyre            | 21,795,981  | 95,990      |              227 |
| maalfrid_nmbu                         | 18,493,389  | 71,320      |              259 |
| maalfrid_oslomet                      | 18,140,360  | 48,140      |              376 |
| maalfrid_domstol                      | 17,073,430  | 52,233      |              326 |
| maalfrid_banenor                      | 16,805,767  | 71,933      |              233 |
| maalfrid_nav                          | 16,651,084  | 75,792      |              219 |
| maalfrid_landbruksdirektoratet        | 13,398,273  | 49,021      |              273 |
| maalfrid_helsedirektoratet            | 13,312,827  | 50,476      |              263 |
| maalfrid_nokut                        | 10,332,870  | 39,426      |              262 |
| maalfrid_hi                           | 10,272,572  | 39,923      |              257 |
| maalfrid_norges-bank                  | 10,135,291  | 37,988      |              266 |
| maalfrid_udir                         | 10,102,549  | 39,632      |              254 |
| maalfrid_vkm                          | 10,041,892  | 32,960      |              304 |
| maalfrid_nbim                         | 9,841,446   | 18,532      |              531 |
| maalfrid_miljodirektoratet            | 9,704,586   | 35,482      |              273 |
| maalfrid_distriktssenteret            | 9,598,021   | 39,415      |              243 |
| maalfrid_ngu                          | 9,454,229   | 35,414      |              266 |
| maalfrid_ptil                         | 9,416,592   | 35,024      |              268 |
| maalfrid_nord                         | 9,192,052   | 45,786      |              200 |
| maalfrid_fiskeridir                   | 8,482,774   | 34,167      |              248 |
| maalfrid_hivolda                      | 7,993,548   | 27,057      |              295 |
| maalfrid_difi                         | 7,971,205   | 36,605      |              217 |
| maalfrid_mattilsynet                  | 7,663,012   | 27,614      |              277 |
| maalfrid_havarikommisjonen            | 7,607,533   | 25,552      |              297 |
| maalfrid_kulturradet                  | 7,364,353   | 22,951      |              320 |
| maalfrid_ks                           | 7,065,314   | 28,029      |              252 |
| maalfrid_kystverket                   | 6,870,772   | 31,694      |              216 |
| maalfrid_udi                          | 6,566,701   | 19,529      |              336 |
| maalfrid_uia                          | 6,094,660   | 24,397      |              249 |
| maalfrid_hjelpemiddeldatabasen        | 6,029,920   | 34,946      |              172 |
| maalfrid_khrono                       | 5,993,140   | 20,431      |              293 |
| maalfrid_helsetilsynet                | 5,913,602   | 18,721      |              315 |
| maalfrid_moreforsk                    | 5,755,447   | 22,089      |              260 |
| maalfrid_jernbanedirektoratet         | 5,589,074   | 22,150      |              252 |
| maalfrid_veiviseren                   | 5,438,468   | 18,441      |              294 |
| maalfrid_dsb                          | 5,312,625   | 18,200      |              291 |
| maalfrid_husbanken                    | 4,810,203   | 15,375      |              312 |
| maalfrid_legemiddelverket             | 4,795,154   | 20,634      |              232 |
| maalfrid_vetinst                      | 4,776,782   | 14,839      |              321 |
| maalfrid_imdi                         | 4,744,408   | 15,642      |              303 |
| maalfrid_forsvarsbygg                 | 4,672,409   | 19,287      |              242 |
| maalfrid_sdir                         | 4,640,185   | 15,547      |              298 |
| maalfrid_konkurransetilsynet          | 4,618,588   | 12,912      |              357 |
| maalfrid_arkivverket                  | 4,603,524   | 16,899      |              272 |
| maalfrid_dsa                          | 4,595,530   | 16,242      |              282 |
| maalfrid_hiof                         | 4,580,991   | 23,675      |              193 |
| maalfrid_ehelse                       | 4,478,908   | 23,074      |              194 |
| maalfrid_inn                          | 4,420,070   | 26,840      |              164 |
| maalfrid_klagenemndssekretariatet     | 4,287,067   | 12,208      |              351 |
| maalfrid_sprakradet                   | 4,180,404   | 15,521      |              269 |
| maalfrid_nhh                          | 4,063,920   | 16,068      |              252 |
| maalfrid_dibk                         | 4,058,208   | 15,855      |              255 |
| maalfrid_kartverket                   | 3,814,376   | 19,110      |              199 |
| maalfrid_riksrevisjonen               | 3,783,728   | 11,216      |              337 |
| maalfrid_toll                         | 3,595,842   | 14,122      |              254 |
| maalfrid_nibio                        | 3,531,231   | 17,464      |              202 |
| maalfrid_met                          | 3,528,846   | 18,689      |              188 |
| maalfrid_bufdir                       | 3,425,362   | 11,720      |              292 |
| maalfrid_artsdatabanken               | 3,275,378   | 9,242       |              354 |
| maalfrid_politiet                     | 3,239,913   | 10,728      |              302 |
| maalfrid_nkom                         | 3,197,196   | 10,214      |              313 |
| maalfrid_vestlandfylke                | 3,127,665   | 12,337      |              253 |
| maalfrid_uis                          | 2,988,424   | 10,045      |              297 |
| maalfrid_sykkelbynettverket           | 2,880,916   | 12,086      |              238 |
| maalfrid_nlr                          | 2,702,753   | 16,178      |              167 |
| maalfrid_seniorporten                 | 2,672,667   | 8,295       |              322 |
| maalfrid_npd                          | 2,657,179   | 10,989      |              241 |
| maalfrid_custompublish                | 2,493,062   | 9,404       |              265 |
| maalfrid_aldringoghelse               | 2,475,601   | 6,927       |              357 |
| maalfrid_bioteknologiradet            | 2,450,272   | 6,135       |              399 |
| maalfrid_nyemetoder                   | 2,426,982   | 10,999      |              220 |
| maalfrid_arbeidstilsynet              | 2,426,255   | 7,030       |              345 |
| maalfrid_riksantikvaren               | 2,300,159   | 8,933       |              257 |
| maalfrid_sjt                          | 2,292,578   | 11,455      |              200 |
| maalfrid_hvl                          | 2,194,063   | 9,604       |              228 |
| maalfrid_luftfartstilsynet            | 2,149,215   | 10,092      |              212 |
| maalfrid_dfo                          | 2,123,792   | 9,383       |              226 |
| maalfrid_ldo                          | 2,093,301   | 7,471       |              280 |
| maalfrid_kompetansenorge              | 1,997,361   | 10,496      |              190 |
| maalfrid_forbrukerradet               | 1,992,302   | 7,493       |              265 |
| maalfrid_himolde                      | 1,959,626   | 10,200      |              192 |
| maalfrid_usn                          | 1,828,928   | 7,553       |              242 |
| maalfrid_naku                         | 1,786,086   | 5,328       |              335 |
| maalfrid_medietilsynet                | 1,648,462   | 6,758       |              243 |
| maalfrid_matematikksenteret           | 1,608,332   | 7,474       |              215 |
| maalfrid_diku                         | 1,579,996   | 6,383       |              247 |
| maalfrid_forskningsetikk              | 1,573,014   | 5,653       |              278 |
| maalfrid_godeidrettsanlegg            | 1,539,910   | 6,252       |              246 |
| maalfrid_dirmin                       | 1,500,122   | 5,427       |              276 |
| maalfrid_diskrimineringsnemnda        | 1,498,443   | 4,270       |              350 |
| maalfrid_naturfag                     | 1,481,316   | 6,108       |              242 |
| maalfrid_arbeidsretten                | 1,473,299   | 4,864       |              302 |
| maalfrid_fellesstudentsystem          | 1,392,117   | 10,553      |              131 |
| maalfrid_nupi                         | 1,322,743   | 5,628       |              235 |
| maalfrid_kriminalitetsforebygging     | 1,223,976   | 4,769       |              256 |
| maalfrid_anskaffelser                 | 1,214,995   | 5,602       |              216 |
| maalfrid_folketrygdfondet             | 1,212,747   | 4,347       |              278 |
| maalfrid_miljopakken                  | 1,195,869   | 5,634       |              212 |
| maalfrid_nih                          | 1,146,471   | 5,415       |              211 |
| maalfrid_statsbygg                    | 1,125,666   | 4,520       |              249 |
| maalfrid_nb                           | 1,085,457   | 4,251       |              255 |
| maalfrid_unit                         | 1,072,199   | 6,476       |              165 |
| maalfrid_npolar                       | 1,071,381   | 2,708       |              395 |
| maalfrid_valgdirektoratet             | 1,028,381   | 9,316       |              110 |
| maalfrid_barneombudet                 | 1,001,224   | 2,863       |              349 |
| maalfrid_datatilsynet                 | 990,582     | 3,018       |              328 |
| maalfrid_lottstift                    | 985,351     | 3,676       |              268 |
| maalfrid_aho                          | 977,116     | 4,637       |              210 |
| maalfrid_sykehuspartner               | 961,362     | 4,693       |              204 |
| maalfrid_naturfagsenteret             | 922,174     | 3,957       |              233 |
| maalfrid_khio                         | 869,917     | 3,457       |              251 |
| maalfrid_spesialenheten               | 845,989     | 2,188       |              386 |
| maalfrid_xn--miljlftet-o8ab           | 822,783     | 3,468       |              237 |
| maalfrid_samordnaopptak               | 805,644     | 2,415       |              333 |
| maalfrid_helsenorge                   | 802,003     | 3,116       |              257 |
| maalfrid_skrivesenteret               | 793,053     | 4,250       |              186 |
| maalfrid_mareano                      | 784,843     | 3,821       |              205 |
| maalfrid_fiskeridirektoratet          | 772,720     | 2,499       |              309 |
| maalfrid_sykehusinnkjop               | 754,616     | 4,440       |              169 |
| maalfrid_matportalen                  | 641,663     | 2,413       |              265 |
| maalfrid_spk                          | 621,687     | 2,181       |              285 |
| maalfrid_pasientsikkerhetsprogrammet  | 610,855     | 4,796       |              127 |
| maalfrid_justervesenet                | 607,767     | 1,946       |              312 |
| maalfrid_nhn                          | 594,591     | 3,665       |              162 |
| maalfrid_sshf                         | 589,448     | 1,950       |              302 |
| maalfrid_bibliotekutvikling           | 573,724     | 3,295       |              174 |
| maalfrid_nysgjerrigper                | 572,860     | 3,088       |              185 |
| maalfrid_nodnett                      | 549,483     | 2,743       |              200 |
| maalfrid_giek                         | 525,782     | 1,840       |              285 |
| maalfrid_une                          | 524,664     | 1,281       |              409 |
| maalfrid_samas                        | 512,469     | 2,610       |              196 |
| maalfrid_kriminalomsorgen             | 506,869     | 1,990       |              254 |
| maalfrid_kjonnsforskning              | 495,072     | 1,464       |              338 |
| maalfrid_kunstkultursenteret          | 478,748     | 1,460       |              327 |
| maalfrid_nynorsksenteret              | 472,484     | 2,147       |              220 |
| maalfrid_ceres                        | 457,001     | 1,988       |              229 |
| maalfrid_stami                        | 456,707     | 1,190       |              383 |
| maalfrid_nsm                          | 452,597     | 1,573       |              287 |
| maalfrid_gjenopptakelse               | 430,682     | 1,501       |              286 |
| maalfrid_nfi                          | 430,469     | 1,557       |              276 |
| maalfrid_nidsenter                    | 416,329     | 1,657       |              251 |
| maalfrid_nasjonalmuseet               | 396,739     | 1,106       |              358 |
| maalfrid_forbrukertilsynet            | 395,317     | 1,252       |              315 |
| maalfrid_natursekken                  | 389,147     | 3,657       |              106 |
| maalfrid_fordelingsutvalget           | 362,923     | 1,416       |              256 |
| maalfrid_digdir                       | 358,558     | 2,159       |              166 |
| maalfrid_forsvaret                    | 339,218     | 1,243       |              272 |
| maalfrid_beccle                       | 337,729     | 1,554       |              217 |
| maalfrid_romsenter                    | 335,107     | 1,154       |              290 |
| maalfrid_geonorge                     | 306,914     | 1,658       |              185 |
| maalfrid_universell                   | 269,369     | 2,206       |              122 |
| maalfrid_ovf                          | 267,941     | 950         |              282 |
| maalfrid_forbrukereuropa              | 264,366     | 1,043       |              253 |
| maalfrid_politihogskolen              | 264,192     | 1,253       |              210 |
| maalfrid_vinmonopolet                 | 250,998     | 689         |              364 |
| maalfrid_energimerking                | 243,288     | 1,061       |              229 |
| maalfrid_ombudsmann                   | 235,226     | 432         |              544 |
| maalfrid_vea-fs                       | 231,109     | 1,293       |              178 |
| maalfrid_traumebevisst                | 228,320     | 2,482       |               91 |
| maalfrid_npe                          | 208,768     | 1,018       |              205 |
| maalfrid_pkh                          | 206,925     | 814         |              254 |
| maalfrid_opplaringslovutvalget        | 198,545     | 561         |              353 |
| maalfrid_helfo                        | 197,334     | 1,005       |              196 |
| maalfrid_regionaleforskningsfond      | 191,416     | 1,010       |              189 |
| maalfrid_nafkam                       | 180,622     | 582         |              310 |
| maalfrid_jernbanemagasinet            | 178,723     | 422         |              423 |
| maalfrid_polarhistorie                | 176,126     | 393         |              448 |
| maalfrid_aasentunet                   | 165,549     | 543         |              304 |
| maalfrid_riksteatret                  | 161,970     | 809         |              200 |
| maalfrid_realfagsloyper               | 160,310     | 765         |              209 |
| maalfrid_koro                         | 156,518     | 584         |              268 |
| maalfrid_squarespace                  | 149,259     | 515         |              289 |
| maalfrid_politietssikkerhetstjeneste  | 146,346     | 478         |              306 |
| maalfrid_unknown                      | 142,298     | 715         |              199 |
| maalfrid_whocc                        | 122,839     | 664         |              184 |
| maalfrid_konfliktraadet               | 122,030     | 379         |              321 |
| maalfrid_okokrim                      | 119,794     | 381         |              314 |
| maalfrid_brreg                        | 115,114     | 583         |              197 |
| maalfrid_riksmekleren                 | 113,287     | 570         |              198 |
| maalfrid_sismo                        | 112,976     | 316         |              357 |
| maalfrid_akkreditert                  | 101,275     | 513         |              197 |
| maalfrid_sivilforsvaret               | 101,178     | 528         |              191 |
| maalfrid_radetfordyreetikk            | 100,021     | 446         |              224 |
| maalfrid_lanekassen                   | 97,196      | 309         |              314 |
| maalfrid_digidel                      | 96,967      | 621         |              156 |
| maalfrid_uit                          | 92,451      | 612         |              151 |
| maalfrid_generaladvokaten             | 91,998      | 297         |              309 |
| maalfrid_nyinorge                     | 90,938      | 204         |              445 |
| maalfrid_lokforerskolen               | 90,255      | 478         |              188 |
| maalfrid_varsom                       | 87,050      | 576         |              151 |
| maalfrid_ffi                          | 82,147      | 224         |              366 |
| maalfrid_kulturminnefondet            | 81,683      | 424         |              192 |
| maalfrid_unesco                       | 78,677      | 388         |              202 |
| maalfrid_yrkesfisker                  | 76,760      | 512         |              149 |
| maalfrid_dekom                        | 74,066      | 1,331       |               55 |
| maalfrid_omsorgsforskning             | 73,528      | 332         |              221 |
| maalfrid_lektor2                      | 70,477      | 561         |              125 |
| maalfrid_openaccess                   | 65,385      | 197         |              331 |
| maalfrid_ssn                          | 64,111      | 308         |              208 |
| maalfrid_lokalhistorie                | 61,885      | 250         |              247 |
| maalfrid_laudim                       | 59,669      | 402         |              148 |
| maalfrid_nlb                          | 58,927      | 206         |              286 |
| maalfrid_riksadvokaten                | 57,938      | 156         |              371 |
| maalfrid_denkulturelleskolesekken     | 46,768      | 248         |              188 |
| maalfrid_sivilrett                    | 45,214      | 145         |              311 |
| maalfrid_htu                          | 43,778      | 171         |              256 |
| maalfrid_yr                           | 41,565      | 575         |               72 |
| maalfrid_informasjonskompetanse       | 40,989      | 334         |              122 |
| maalfrid_finansportalen               | 40,333      | 187         |              215 |
| maalfrid_dep                          | 38,882      | 126         |              308 |
| maalfrid_kulturped                    | 37,718      | 99          |              380 |
| maalfrid_feide                        | 37,583      | 274         |              137 |
| maalfrid_fug                          | 35,253      | 123         |              286 |
| maalfrid_kulturoghelse                | 34,762      | 189         |              183 |
| maalfrid_helseklage                   | 33,612      | 127         |              264 |
| maalfrid_nbsk                         | 31,334      | 215         |              145 |
| maalfrid_matogindustri                | 31,232      | 207         |              150 |
| maalfrid_sinn                         | 28,114      | 154         |              182 |
| maalfrid_transport21                  | 25,691      | 91          |              282 |
| maalfrid_vergemal                     | 24,189      | 80          |              302 |
| maalfrid_konkursradet                 | 24,072      | 78          |              308 |
| maalfrid_norec                        | 22,496      | 78          |              288 |
| maalfrid_pts                          | 21,346      | 81          |              263 |
| maalfrid_nasjonaleturistveger         | 20,237      | 111         |              182 |
| maalfrid_hjelpelinjen                 | 19,476      | 86          |              226 |
| maalfrid_iearth                       | 19,418      | 150         |              129 |
| maalfrid_russamtalen                  | 19,035      | 69          |              275 |
| maalfrid_xn--kvinneligomskjring-1ub   | 18,607      | 79          |              235 |
| maalfrid_memu                         | 17,820      | 101         |              176 |
| maalfrid_nynorskbok                   | 17,769      | 98          |              181 |
| maalfrid_regjeringsadvokaten          | 17,416      | 55          |              316 |
| maalfrid_xn--forskerfr-t8a            | 16,827      | 177         |               95 |
| maalfrid_xn--tilbakefring-2jb         | 15,814      | 49          |              322 |
| maalfrid_ringerikefengsel             | 15,669      | 28          |              559 |
| maalfrid_skattefunn                   | 15,625      | 54          |              289 |
| maalfrid_skeivtarkiv                  | 15,537      | 69          |              225 |
| maalfrid_fordelingsutvalet            | 15,473      | 35          |              442 |
| maalfrid_samfunnskunnskap             | 15,110      | 60          |              251 |
| maalfrid_shiprep                      | 14,632      | 146         |              100 |
| maalfrid_sevuppt                      | 14,087      | 55          |              256 |
| maalfrid_haldenfengsel                | 13,655      | 38          |              359 |
| maalfrid_forbrukerklageutvalget       | 13,472      | 51          |              264 |
| maalfrid_mhfa                         | 12,591      | 146         |               86 |
| maalfrid_ah                           | 11,787      | 36          |              327 |
| maalfrid_nettvett                     | 11,353      | 44          |              258 |
| maalfrid_uh-it                        | 11,158      | 281         |               39 |
| maalfrid_fishgen                      | 10,318      | 29          |              355 |
| maalfrid_designavgang                 | 10,164      | 75          |              135 |
| maalfrid_global                       | 9,363       | 43          |              217 |
| maalfrid_valg                         | 8,797       | 48          |              183 |
| maalfrid_havmiljo                     | 8,734       | 69          |              126 |
| maalfrid_altinn                       | 7,945       | 50          |              158 |
| maalfrid_miljoklagenemnda             | 7,797       | 35          |              222 |
| maalfrid_spinn-inn                    | 7,699       | 48          |              160 |
| maalfrid_kantinekurset                | 7,397       | 54          |              136 |
| maalfrid_bastoyfengsel                | 7,142       | 56          |              127 |
| maalfrid_norskpetroleum               | 6,107       | 120         |               50 |
| maalfrid_voldsoffererstatning         | 6,079       | 27          |              225 |
| maalfrid_musikkbasertmiljobehandling  | 5,186       | 39          |              132 |
| maalfrid_prosjektveiviseren           | 5,154       | 15          |              343 |
| maalfrid_aldersvennlig                | 4,919       | 32          |              153 |
| maalfrid_barentswatch                 | 4,829       | 32          |              150 |
| maalfrid_fmfiavo@fylkesmannen         | 4,740       | 69          |               68 |
| maalfrid_kk-utvalget                  | 4,697       | 19          |              247 |
| maalfrid_agropub                      | 4,434       | 17          |              260 |
| maalfrid_utdanningiverden             | 4,369       | 14          |              312 |
| maalfrid_overgangsbolig               | 3,862       | 36          |              107 |
| maalfrid_forsvaretsmuseer             | 3,840       | 35          |              109 |
| maalfrid_okopark                      | 3,282       | 12          |              273 |
| maalfrid_pst                          | 2,866       | 14          |              204 |
| maalfrid_sikkerhverdag                | 2,786       | 19          |              146 |
| maalfrid_arkitektur                   | 2,436       | 15          |              162 |
| maalfrid_velgekte                     | 2,287       | 10          |              228 |
| maalfrid_addlab                       | 2,109       | 12          |              175 |
| maalfrid_romerikefengsel              | 2,088       | 19          |              109 |
| maalfrid_utdanning                    | 2,009       | 12          |              167 |
| maalfrid_grunderskolen                | 1,994       | 7           |              284 |
| maalfrid_umb                          | 1,958       | 9           |              217 |
| maalfrid_oslofengsel                  | 1,756       | 8           |              219 |
| maalfrid_hjorteviltregisteret         | 1,600       | 5           |              320 |
| maalfrid_alleteller                   | 1,511       | 7           |              215 |
| maalfrid_webhuset                     | 1,409       | 5           |              281 |
| maalfrid_lykillinn                    | 1,349       | 4           |              337 |
| maalfrid_kulturfag                    | 1,215       | 6           |              202 |
| maalfrid_unimus                       | 940         | 4           |              235 |
| maalfrid_anleggsregisteret            | 928         | 5           |              185 |
| maalfrid_mangfoldsprisen              | 597         | 3           |              199 |
| maalfrid_algae2future                 | 456         | 8           |               57 |
| maalfrid_mammapresenterer             | 447         | 2           |              223 |
| maalfrid_karriereveiledning           | 391         | 27          |               14 |
| maalfrid_nodsms                       | 351         | 4           |               87 |
| maalfrid_kildekompasset               | 302         | 1           |              302 |
| maalfrid_praksisfou                   | 297         | 1           |              297 |
| maalfrid_retttilaalese                | 246         | 3           |               82 |
| maalfrid_indreostfoldfengsel          | 215         | 3           |               71 |
| maalfrid_xn--kroppsvingsforskning-gcc | 205         | 2           |              102 |
| maalfrid_pahoyden                     | 154         | 1           |              154 |
| maalfrid_norren                       | 42          | 1           |               42 |

### Languages
| Language   | Words         | Documents   |   Words/Document |
|-----------:|--------------:|------------:|-----------------:|
| no         | 1,248,901,257 | 4,462,909   |              279 |
| en         | 422,678,950   | 1,456,480   |              290 |
| da         | 73,779,920    | 256,659     |              287 |
| nn         | 63,661,272    | 206,735     |              307 |
| fr         | 45,122,943    | 107,315     |              420 |
| de         | 11,584,819    | 60,772      |              190 |
| sv         | 10,007,099    | 50,064      |              199 |
| es         | 8,138,812     | 31,031      |              262 |
| pt         | 2,483,288     | 14,797      |              167 |
| fi         | 2,406,210     | 10,484      |              229 |
| oc         | 2,170,769     | 4,988       |              435 |
| nl         | 1,562,699     | 6,789       |              230 |
| uk         | 1,446,456     | 4,296       |              336 |
| zh         | 1,406,637     | 7,759       |              181 |
| ca         | 1,388,067     | 3,630       |              382 |
| ru         | 1,205,439     | 5,669       |              212 |
| it         | 950,452       | 6,689       |              142 |
| et         | 938,286       | 3,968       |              236 |
| cs         | 887,973       | 4,301       |              206 |
| eu         | 851,535       | 3,160       |              269 |
| pl         | 735,829       | 4,909       |              149 |
| fa         | 503,664       | 2,060       |              244 |
| ja         | 349,742       | 3,515       |               99 |
| is         | 309,524       | 995         |              311 |
| id         | 223,364       | 1,255       |              177 |
| ar         | 212,455       | 1,181       |              179 |
| so         | 131,743       | 605         |              217 |
| el         | 120,377       | 617         |              195 |
| hu         | 119,131       | 1,277       |               93 |
| vi         | 96,710        | 497         |              194 |
| sl         | 93,656        | 649         |              144 |
| tr         | 91,012        | 1,010       |               90 |
| ro         | 76,959        | 427         |              180 |
| lt         | 67,317        | 552         |              121 |
| sr         | 65,928        | 791         |               83 |
| gl         | 65,517        | 579         |              113 |
| la         | 62,069        | 461         |              134 |
| th         | 53,793        | 359         |              149 |
| hr         | 48,627        | 472         |              103 |
| am         | 46,475        | 326         |              142 |
| ko         | 44,264        | 884         |               50 |
| ml         | 35,492        | 151         |              235 |
| sq         | 31,182        | 148         |              210 |
| tl         | 30,964        | 163         |              189 |
| kk         | 27,686        | 69          |              401 |
| mn         | 21,540        | 22          |              979 |
| sw         | 18,626        | 64          |              291 |
| pnb        | 18,502        | 81          |              228 |
| eo         | 17,760        | 440         |               40 |
| sk         | 17,616        | 195         |               90 |
| bg         | 16,521        | 97          |              170 |
| ur         | 15,797        | 140         |              112 |
| sh         | 14,138        | 120         |              117 |
| mk         | 13,479        | 65          |              207 |
| lv         | 9,389         | 60          |              156 |
| ckb        | 9,350         | 44          |              212 |
| ku         | 9,058         | 54          |              167 |
| ast        | 7,910         | 63          |              125 |
| uz         | 6,883         | 35          |              196 |
| az         | 6,757         | 44          |              153 |
| ceb        | 5,492         | 227         |               24 |
| war        | 4,149         | 95          |               43 |
| ta         | 3,990         | 58          |               68 |
| ms         | 3,655         | 94          |               38 |
| hy         | 3,279         | 30          |              109 |
| fy         | 2,837         | 22          |              128 |
| hi         | 2,810         | 40          |               70 |
| ht         | 2,534         | 11          |              230 |
| jv         | 2,042         | 31          |               65 |
| cy         | 1,988         | 40          |               49 |
| su         | 1,840         | 23          |               80 |
| ps         | 1,832         | 15          |              122 |
| als        | 1,805         | 35          |               51 |
| af         | 1,703         | 20          |               85 |
| bs         | 1,524         | 24          |               63 |
| qu         | 1,484         | 13          |              114 |
| nds        | 1,328         | 75          |               17 |
| be         | 1,209         | 33          |               36 |
| my         | 1,115         | 16          |               69 |
| ga         | 955           | 25          |               38 |
| mt         | 940           | 12          |               78 |
| si         | 898           | 22          |               40 |
| te         | 853           | 17          |               50 |
| ilo        | 801           | 16          |               50 |
| io         | 689           | 10          |               68 |
| tt         | 675           | 20          |               33 |
| km         | 647           | 11          |               58 |
| jbo        | 621           | 27          |               23 |
| gn         | 595           | 7           |               85 |
| ug         | 581           | 6           |               96 |
| kv         | 562           | 3           |              187 |
| br         | 533           | 20          |               26 |
| kn         | 531           | 19          |               27 |
| bn         | 490           | 20          |               24 |
| pam        | 476           | 1           |              476 |
| pa         | 413           | 15          |               27 |
| he         | 396           | 14          |               28 |
| ka         | 326           | 17          |               19 |
| kw         | 324           | 4           |               81 |
| vep        | 296           | 11          |               26 |
| yo         | 261           | 5           |               52 |
| gu         | 234           | 12          |               19 |
| ky         | 232           | 11          |               21 |
| azb        | 216           | 1           |              216 |
| ba         | 203           | 5           |               40 |
| gom        | 164           | 9           |               18 |
| wa         | 130           | 18          |                7 |
| tg         | 129           | 3           |               43 |
| ia         | 125           | 11          |               11 |
| mr         | 122           | 6           |               20 |
| lmo        | 87            | 23          |                3 |
| lb         | 68            | 15          |                4 |
| vec        | 67            | 3           |               22 |
| rue        | 67            | 2           |               33 |
| pms        | 63            | 8           |                7 |
| min        | 60            | 6           |               10 |
| ne         | 51            | 5           |               10 |
| hsb        | 51            | 2           |               25 |
| cbk        | 46            | 2           |               23 |
| or         | 44            | 2           |               22 |
| ie         | 38            | 5           |                7 |
| tk         | 36            | 4           |                9 |
| eml        | 31            | 4           |                7 |
| arz        | 31            | 1           |               31 |
| sco        | 30            | 1           |               30 |
| gd         | 29            | 2           |               14 |
| bar        | 27            | 2           |               13 |
| li         | 22            | 3           |                7 |
| diq        | 20            | 2           |               10 |
| yue        | 19            | 1           |               19 |
| dsb        | 19            | 1           |               19 |
| as         | 17            | 1           |               17 |
| os         | 15            | 2           |                7 |
| wuu        | 14            | 1           |               14 |
| mg         | 14            | 2           |                7 |
| sd         | 14            | 1           |               14 |
| nah        | 14            | 2           |                7 |
| cv         | 12            | 1           |               12 |
| scn        | 9             | 2           |                4 |
| bh         | 8             | 1           |                8 |
| bcl        | 8             | 1           |                8 |
| ce         | 4             | 1           |                4 |
| new        | 4             | 1           |                4 |
| frr        | 3             | 1           |                3 |
| vo         | 3             | 2           |                1 |
| gv         | 3             | 1           |                3 |
| mzn        | 3             | 1           |                3 |
| lo         | 2             | 1           |                2 |

### Publish Periode
|   Decade | Words         | Documents   |   Words/Document |
|---------:|--------------:|------------:|-----------------:|
|     2020 | 1,905,481,776 | 6,735,367   |              282 |
</details>


## Newspapers
A large collection of out-of-copyright newspapers from the National Library of Norway. This collection both has OCR scanned newspapers, and newspapers that are delivered to the library as pdf and where we are able to extract the text directly.

| License  | Size | Words | Documents | Avg words per doc  |
| -------- |   :-----|   -----:| -----:| -----:|
| [CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/)|14.0 GB| 2,019,172,625 | 10,096,424  |              199 |
<details>
<summary>View dataset statistics</summary>

### Document Types
| Source        | Words         | Documents   |   Words/Document |
|--------------:|--------------:|------------:|-----------------:|
| newspaper_ocr | 2,019,172,625 | 10,096,424  |              199 |

### Languages
| Language   | Words         | Documents   |   Words/Document |
|-----------:|--------------:|------------:|-----------------:|
| no         | 1,854,790,815 | 9,011,769   |              205 |
| nn         | 126,257,684   | 526,902     |              239 |
| da         | 14,101,047    | 254,996     |               55 |
| en         | 9,187,689     | 93,497      |               98 |
| fi         | 4,264,629     | 37,132      |              114 |
| sv         | 3,011,755     | 63,999      |               47 |
| et         | 2,326,165     | 20,753      |              112 |
| cs         | 1,781,741     | 17,925      |               99 |
| es         | 1,639,849     | 10,848      |              151 |
| de         | 679,620       | 23,312      |               29 |
| hu         | 480,299       | 7,360       |               65 |
| fr         | 128,379       | 2,517       |               51 |
| nl         | 103,567       | 4,714       |               21 |
| pl         | 103,427       | 4,420       |               23 |
| sl         | 48,603        | 1,224       |               39 |
| pt         | 46,407        | 1,772       |               26 |
| it         | 33,927        | 1,646       |               20 |
| ru         | 29,604        | 1,029       |               28 |
| sk         | 22,246        | 814         |               27 |
| uk         | 21,106        | 792         |               26 |
| ca         | 17,842        | 912         |               19 |
| hr         | 14,090        | 586         |               24 |
| ja         | 10,886        | 1,519       |                7 |
| id         | 9,275         | 809         |               11 |
| sr         | 7,805         | 198         |               39 |
| zh         | 7,101         | 548         |               12 |
| is         | 5,428         | 234         |               23 |
| vi         | 4,631         | 376         |               12 |
| tr         | 3,703         | 634         |                5 |
| ms         | 3,528         | 395         |                8 |
| sq         | 3,088         | 88          |               35 |
| lt         | 3,074         | 316         |                9 |
| ga         | 3,024         | 157         |               19 |
| oc         | 2,784         | 42          |               66 |
| sh         | 2,259         | 93          |               24 |
| eu         | 2,229         | 106         |               21 |
| eo         | 2,002         | 389         |                5 |
| la         | 1,799         | 296         |                6 |
| ro         | 1,447         | 192         |                7 |
| gl         | 798           | 119         |                6 |
| bs         | 770           | 43          |               17 |
| ko         | 766           | 111         |                6 |
| lv         | 488           | 61          |                8 |
| war        | 443           | 40          |               11 |
| nds        | 437           | 83          |                5 |
| ceb        | 378           | 61          |                6 |
| ilo        | 325           | 9           |               36 |
| jv         | 297           | 59          |                5 |
| fy         | 277           | 43          |                6 |
| ur         | 243           | 37          |                6 |
| ml         | 190           | 10          |               19 |
| br         | 172           | 22          |                7 |
| fa         | 160           | 29          |                5 |
| ar         | 160           | 21          |                7 |
| kw         | 148           | 14          |               10 |
| be         | 145           | 20          |                7 |
| als        | 137           | 29          |                4 |
| el         | 120           | 15          |                8 |
| vep        | 117           | 21          |                5 |
| uz         | 107           | 24          |                4 |
| cy         | 86            | 13          |                6 |
| hy         | 73            | 11          |                6 |
| ast        | 73            | 12          |                6 |
| gn         | 70            | 5           |               14 |
| th         | 63            | 14          |                4 |
| su         | 62            | 7           |                8 |
| min        | 60            | 12          |                5 |
| tl         | 57            | 14          |                4 |
| af         | 53            | 14          |                3 |
| si         | 53            | 8           |                6 |
| lmo        | 47            | 4           |               11 |
| pms        | 45            | 7           |                6 |
| sw         | 44            | 8           |                5 |
| az         | 42            | 11          |                3 |
| lb         | 38            | 9           |                4 |
| te         | 35            | 1           |               35 |
| bg         | 34            | 5           |                6 |
| mt         | 34            | 4           |                8 |
| ka         | 33            | 4           |                8 |
| sco        | 31            | 5           |                6 |
| io         | 22            | 4           |                5 |
| ie         | 21            | 6           |                3 |
| os         | 21            | 1           |               21 |
| yo         | 20            | 4           |                5 |
| mg         | 16            | 4           |                4 |
| bar        | 16            | 4           |                4 |
| he         | 16            | 4           |                4 |
| nap        | 16            | 1           |               16 |
| mr         | 16            | 4           |                4 |
| pa         | 16            | 1           |               16 |
| ia         | 15            | 4           |                3 |
| wa         | 14            | 2           |                7 |
| qu         | 14            | 1           |               14 |
| ku         | 13            | 3           |                4 |
| kn         | 13            | 3           |                4 |
| rm         | 12            | 2           |                6 |
| frr        | 10            | 2           |                5 |
| gom        | 10            | 3           |                3 |
| bn         | 9             | 2           |                4 |
| tt         | 9             | 2           |                4 |
| kk         | 8             | 2           |                4 |
| li         | 7             | 3           |                2 |
| eml        | 7             | 2           |                3 |
| mk         | 7             | 2           |                3 |
| co         | 7             | 1           |                7 |
| hsb        | 6             | 1           |                6 |
| jbo        | 5             | 2           |                2 |
| ne         | 5             | 1           |                5 |
| pam        | 4             | 1           |                4 |
| ta         | 3             | 1           |                3 |
| hi         | 2             | 1           |                2 |

### Publish Periode
|   Decade | Words       | Documents   | Words/Document   |
|---------:|------------:|------------:|-----------------:|
|     2020 | 48,107      | 321         | 149              |
|     2010 | 345,461,597 | 2,469,655   | 1,414            |
|     2000 | 399,916,520 | 1,741,144   | 2,334            |
|     1990 | 668,123,800 | 2,563,932   | 2,589            |
|     1980 | 124,185,906 | 549,411     | 2,267            |
|     1970 | 168,128,159 | 847,524     | 1,973            |
|     1960 | 134,790,494 | 852,668     | 1,581            |
|     1950 | 82,534,163  | 489,139     | 1,677            |
|     1940 | 95,983,879  | 582,630     | 1,609            |
 
</details>



## Newspapers Online
 A Norwegian Newspaper Corpus with texts from online bokmål newspapers between 1998 and 2019 collected by Språkbanken. 

| License  | Size | Words | Documents | Avg words per doc  |
| -------- |   :-----|   -----:| -----:| -----:|
| [CC BY-NC 2.0](https://creativecommons.org/licenses/by-nc/2.0/)|3.7 GB| 541,481,947 | 3,695,943   |              146 |
<details>
<summary>View dataset statistics</summary>
 
 
### Document Types
| Source               | Words       | Documents   |   Words/Document |
|---------------------:|------------:|------------:|-----------------:|
| newspapers_online_nb | 498,332,371 | 3,524,770   |              141 |
| newspapers_online_nn | 43,149,576  | 171,173     |              252 |

### Languages
| Language   | Words       | Documents   |   Words/Document |
|-----------:|------------:|------------:|-----------------:|
| no         | 501,126,127 | 3,491,685   |              143 |
| nn         | 36,177,754  | 134,633     |              268 |
| da         | 3,686,792   | 55,966      |               65 |
| en         | 236,278     | 5,749       |               41 |
| sv         | 146,978     | 4,343       |               33 |
| es         | 57,860      | 954         |               60 |
| de         | 22,640      | 1,175       |               19 |
| nl         | 8,459       | 285         |               29 |
| ru         | 3,852       | 74          |               52 |
| it         | 3,397       | 219         |               15 |
| fr         | 2,639       | 185         |               14 |
| pl         | 2,064       | 132         |               15 |
| cs         | 1,395       | 60          |               23 |
| pt         | 1,220       | 74          |               16 |
| fi         | 1,016       | 30          |               33 |
| sh         | 707         | 4           |              176 |
| uk         | 476         | 27          |               17 |
| ja         | 372         | 65          |                5 |
| hr         | 216         | 19          |               11 |
| la         | 207         | 13          |               15 |
| tr         | 188         | 20          |                9 |
| hu         | 181         | 23          |                7 |
| ca         | 174         | 35          |                4 |
| sl         | 158         | 9           |               17 |
| id         | 142         | 20          |                7 |
| et         | 88          | 20          |                4 |
| ro         | 87          | 13          |                6 |
| wa         | 80          | 18          |                4 |
| eo         | 67          | 14          |                4 |
| eu         | 66          | 12          |                5 |
| vi         | 59          | 11          |                5 |
| zh         | 35          | 10          |                3 |
| is         | 26          | 4           |                6 |
| lt         | 16          | 4           |                4 |
| ms         | 14          | 5           |                2 |
| ko         | 13          | 3           |                4 |
| nds        | 10          | 4           |                2 |
| lb         | 9           | 2           |                4 |
| mg         | 8           | 2           |                4 |
| als        | 7           | 1           |                7 |
| ceb        | 7           | 3           |                2 |
| vep        | 6           | 2           |                3 |
| war        | 6           | 2           |                3 |
| ia         | 6           | 1           |                6 |
| mt         | 6           | 1           |                6 |
| pms        | 5           | 1           |                5 |
| be         | 4           | 1           |                4 |
| io         | 4           | 1           |                4 |
| sr         | 4           | 1           |                4 |
| fa         | 4           | 1           |                4 |
| gl         | 4           | 1           |                4 |
| kw         | 3           | 1           |                3 |
| sk         | 3           | 1           |                3 |
| bar        | 3           | 1           |                3 |
| jv         | 2           | 1           |                2 |
| ga         | 2           | 1           |                2 |
| ar         | 1           | 1           |                1 |

### Publish Periode
|   Decade | Words       | Documents   |   Words/Document |
|---------:|------------:|------------:|-----------------:|
|     2020 | 541,481,947 | 3,695,943   |              146 |
 
</details>

## Books
A large collection of out-of-copyright books from the National Library of Norway. This is OCR scanned documents only. 

| License  | Size | Words | Documents | Avg words per doc  |
| -------- |   :-----|   -----:| -----:| -----:|
| [CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/)|6.2 GB| ? | ? | ? |
<details>
<summary>View dataset statistics</summary>
 
### Document Types
| Source   | Words       | Documents   | Words/Document   |
|---------:|------------:|------------:|-----------------:|
| books    | 861,465,907 | 24,253      | 35,519           |

### Languages
| Language   | Words       | Documents   | Words/Document   |
|-----------:|------------:|------------:|-----------------:|
| da         | 451,088,972 | 8,443       | 53,427           |
| no         | 298,587,072 | 12,496      | 23,894           |
| nn         | 43,538,648  | 1,482       | 29,378           |
| en         | 39,155,566  | 1,249       | 31,349           |
| de         | 15,073,597  | 258         | 58,424           |
| sv         | 5,158,922   | 110         | 46,899           |
| fr         | 4,882,246   | 96          | 50,856           |
| fi         | 1,496,060   | 30          | 49,868           |
| la         | 1,217,184   | 36          | 33,810           |
| nl         | 321,846     | 8           | 40,230           |
| it         | 302,329     | 7           | 43,189           |
| es         | 230,586     | 19          | 12,136           |
| lv         | 96,409      | 1           | 96,409           |
| hu         | 68,266      | 2           | 34,133           |
| eo         | 57,660      | 1           | 57,660           |
| hr         | 55,655      | 2           | 27,827           |
| pt         | 54,009      | 1           | 54,009           |
| cs         | 44,232      | 3           | 14,744           |
| pl         | 14,783      | 1           | 14,783           |
| uk         | 11,272      | 6           | 1,878            |
| et         | 10,591      | 1           | 10,591           |
| als        | 2           | 1           | 2                |

### Publish Periode
|   Decade | Words       | Documents   | Words/Document   |
|---------:|------------:|------------:|-----------------:|
|     2020 | 1,986,034   | 64          | 32,559           |
|     2010 | 17,750,006  | 972         | 142,591          |
|     2000 | 57,854,935  | 2,975       | 199,443          |
|     1990 | 116,865,204 | 6,029       | 196,895          |
|     1980 | 40,494,244  | 1,532       | 265,011          |
|     1970 | 22,111,500  | 861         | 252,218          |
|     1960 | 18,124,576  | 480         | 376,502          |
|     1950 | 17,603,940  | 350         | 480,234          |
|     1940 | 29,395,155  | 546         | 509,948          |
|     1930 | 36,535,860  | 716         | 507,173          |
|     1920 | 52,070,672  | 1,087       | 483,201          |
|     1910 | 63,920,279  | 1,255       | 501,227          |
|     1900 | 61,593,361  | 1,164       | 525,050          |
|     1890 | 88,616,464  | 1,814       | 485,506          |
|     1880 | 59,549,395  | 1,087       | 550,945          |
|     1870 | 26,541,488  | 634         | 406,854          |
|     1860 | 39,854,070  | 710         | 543,956          |
|     1850 | 55,078,195  | 864         | 635,165          |
|     1840 | 31,307,769  | 534         | 583,077          |
|     1830 | 18,377,415  | 374         | 479,400          |
|     1820 | 4,821,598   | 147         | 339,040          |
|     1810 | 1,013,747   | 58          | 130,214          |
</details>

## Subtitles
Norwegian subtitles from OpenSubtitles.
| License  | Size | Words | Documents | Avg words per doc  |
| -------- |   :-----|   -----:| -----:| -----:|
| [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/)|0.2 GB| 54,133,135 | 13,416      | 4,034            |
<details>
<summary>View dataset statistics</summary>
 
 ### Languages
| Language   | Words      | Documents   | Words/Document   |
|-----------:|-----------:|------------:|-----------------:|
| no         | 32,485,846 | 8,252       | 3,936            |
| da         | 21,646,096 | 5,117       | 4,230            |
| sv         | 876        | 14          | 62               |
| nn         | 120        | 5           | 24               |
| en         | 81         | 9           | 9                |
| ru         | 46         | 2           | 23               |
| fr         | 21         | 5           | 4                |
| de         | 11         | 2           | 5                |
| ro         | 10         | 2           | 5                |
| pt         | 8          | 2           | 4                |
| es         | 6          | 1           | 6                |
| sh         | 4          | 1           | 4                |
| oc         | 3          | 1           | 3                |
| ja         | 3          | 1           | 3                |
| eo         | 2          | 1           | 2                |
| nl         | 2          | 1           | 2                |

### Publish Periode
|   Decade | Words      | Documents   | Words/Document   |
|---------:|-----------:|------------:|-----------------:|
|     2020 | 13,412     | 9           | 1,490            |
|     2010 | 27,638,493 | 7,289       | 30,488           |
|     2000 | 14,104,886 | 3,546       | 39,812           |
|     1990 | 5,298,273  | 1,178       | 44,776           |
|     1980 | 2,194,461  | 515         | 42,851           |
|     1970 | 1,661,891  | 356         | 48,088           |
|     1960 | 1,269,907  | 233         | 56,574           |
|     1950 | 1,166,250  | 169         | 68,309           |
|     1940 | 537,825    | 77          | 69,822           |
|     1930 | 238,155    | 35          | 63,086           |
|     1920 | 9,582      | 9           | 4,473            |
 
</details>

## Wikipedia
A dump of Wikipedia downloaded 2021.06.20. The text is cleaned. The dump contains both Bokmål and Nynorsk, however this is marked in the corpus in the doc_type-tag. In addition there is automatic language detection by Fasttext that in most cases will overlap.

| License  | Size | Words | Documents | Avg words per doc  |
| -------- |   :-----|   -----:| -----:| -----:|
| [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/)|1.0 GB| 140,992,663 | 681,973     |              206 |
<details>
<summary>View dataset statistics</summary>

### Document Types
| Source                 | Words       | Documents   |   Words/Document |
|-----------------------:|------------:|------------:|-----------------:|
| wikipedia_download_nbo | 113,329,119 | 535,461     |              211 |
| wikipedia_download_nno | 27,663,544  | 146,512     |              188 |

### Languages
| Language   | Words       | Documents   | Words/Document   |
|-----------:|------------:|------------:|-----------------:|
| no         | 112,570,496 | 529,279     | 212              |
| nn         | 25,606,369  | 136,572     | 187              |
| en         | 1,138,003   | 3,550       | 320              |
| da         | 565,459     | 6,928       | 81               |
| de         | 340,884     | 1,555       | 219              |
| sv         | 313,287     | 2,197       | 142              |
| fr         | 118,657     | 360         | 329              |
| war        | 52,692      | 139         | 379              |
| es         | 47,415      | 274         | 173              |
| vi         | 40,237      | 123         | 327              |
| ceb        | 30,173      | 43          | 701              |
| it         | 23,144      | 116         | 199              |
| ru         | 20,264      | 162         | 125              |
| nl         | 19,572      | 88          | 222              |
| pl         | 13,917      | 75          | 185              |
| ko         | 11,857      | 33          | 359              |
| uk         | 11,347      | 94          | 120              |
| pt         | 9,425       | 105         | 89               |
| hr         | 7,126       | 19          | 375              |
| fi         | 6,225       | 29          | 214              |
| hu         | 5,236       | 28          | 187              |
| eo         | 5,084       | 36          | 141              |
| ro         | 3,977       | 13          | 305              |
| la         | 2,908       | 8           | 363              |
| cs         | 2,901       | 19          | 152              |
| pa         | 2,870       | 1           | 2,870            |
| bo         | 2,551       | 1           | 2,551            |
| ca         | 2,489       | 12          | 207              |
| min        | 2,095       | 1           | 2,095            |
| is         | 1,977       | 5           | 395              |
| bn         | 1,309       | 1           | 1,309            |
| be         | 1,262       | 9           | 140              |
| az         | 1,242       | 6           | 207              |
| sq         | 1,058       | 6           | 176              |
| th         | 878         | 4           | 219              |
| et         | 844         | 7           | 120              |
| sh         | 841         | 5           | 168              |
| fy         | 730         | 4           | 182              |
| bg         | 621         | 1           | 621              |
| as         | 567         | 1           | 567              |
| lt         | 525         | 7           | 75               |
| sr         | 496         | 1           | 496              |
| sl         | 398         | 7           | 56               |
| gl         | 384         | 10          | 38               |
| zh         | 358         | 4           | 89               |
| el         | 349         | 3           | 116              |
| lv         | 347         | 2           | 173              |
| ja         | 236         | 5           | 47               |
| fa         | 214         | 1           | 214              |
| hy         | 196         | 3           | 65               |
| ur         | 189         | 2           | 94               |
| ta         | 187         | 1           | 187              |
| tr         | 181         | 1           | 181              |
| kk         | 133         | 1           | 133              |
| tl         | 130         | 1           | 130              |
| nds        | 112         | 1           | 112              |
| wa         | 61          | 3           | 20               |
| km         | 43          | 1           | 43               |
| ar         | 35          | 1           | 35               |
| id         | 23          | 2           | 11               |
| lrc        | 20          | 1           | 20               |
| sk         | 15          | 1           | 15               |
| eu         | 15          | 1           | 15               |
| ga         | 12          | 1           | 12               |
| pms        | 8           | 1           | 8                |
| ms         | 7           | 2           | 3                |

### Publish Periode
|   Decade | Words       | Documents   |   Words/Document |
|---------:|------------:|------------:|-----------------:|
|     2020 | 140,992,663 | 681,973     |              206 |
</details>

## Web Corpora
Please also note that there are Norwegian Web Corpora available, most notably the [OSCAR](https://huggingface.co/datasets/oscar) and the [MC4](https://huggingface.co/datasets/mc4) dataset.  Both these sets have a Norwegian Bokmål and a Norwegian Nynorsk subset. MC4 is the largest set (70GB) but is fairly uncleaned with a significant part of machine generated text. The OSCAR set is smaller (**?**) but is better clened. Almost the entire OSCAR corpus is contained in MC4, so it is not recommented adding both. It might also be an alternative to add just a portion of MC4 because of its size and relatively low quality.

We are unable to redistribute these sets but the datasets are in the same HuggingFace Dataset format and can easily be combined with these sets. 
